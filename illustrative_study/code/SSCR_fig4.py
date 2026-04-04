import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import json
import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess

# 黑白学术风格
def set_academic_style():
    try:
        plt.style.use('seaborn-white')
    except OSError:
        plt.style.use('default')
    matplotlib.rcParams['grid.linestyle'] = '--'
    matplotlib.rcParams['grid.alpha'] = 0.4
    matplotlib.rcParams['axes.grid'] = True
    matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler('color', ['black', 'gray'])

# 读取 JSONLines 文件
def read_jsonlines(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

# 转为DataFrame
def jsonlines_to_dataframe(data):
    records = []
    for entry in data:
        created_at = entry['created_at']
        average_wce = entry['score']['average_wce']
        average_ca = entry['score']['average_ca']
        records.append({
            'created_at': created_at,
            'average_wce': average_wce,
            'average_ca': average_ca
        })
    df = pd.DataFrame(records)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df_grouped = df.groupby('created_at').mean(numeric_only=True).reset_index()
    return df_grouped

# 7天窗口均值、std、n
def aggregate_biweekly(df_grouped):
    df_biweekly = (
        df_grouped.set_index('created_at')
        .resample('7D')
        .agg(['mean', 'std', 'count'])
        .reset_index()
    )
    return df_biweekly

# LOWESS平滑CI带
def lowess_confidence_interval(x, y_mean, y_ci, frac=0.3):
    not_nan_mask = ~np.isnan(y_mean) & ~np.isnan(y_ci)
    x_idx = np.arange(len(x))[not_nan_mask]
    y_mean = y_mean[not_nan_mask]
    y_ci = y_ci[not_nan_mask]
    y_upper = y_mean + y_ci
    y_lower = y_mean - y_ci
    upper_smooth = lowess(y_upper, x_idx, frac=frac)[:,1]
    lower_smooth = lowess(y_lower, x_idx, frac=frac)[:,1]
    x_new = x[not_nan_mask]
    return x_new, lower_smooth, upper_smooth

# LOWESS平滑均值线
def plot_lowess(df, metric, color, linestyle, label, ax, frac=0.3):
    not_nan_mask = df[metric]['mean'].notna()
    x = np.arange(len(df[not_nan_mask]))
    y = df[metric]['mean'][not_nan_mask].values
    lowess_smoothed = lowess(y, x, frac=frac)
    smoothed_x = df['created_at'][not_nan_mask]
    smoothed_y = lowess_smoothed[:, 1]
    ax.plot(smoothed_x, smoothed_y, color=color, linestyle=linestyle, linewidth=2, label=label)

# 合并对比图（95%CI）- 上下子图布局
def plot_combined_comparison(df_biweekly_1, df_biweekly_2):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 10))
    
    # 上方子图：WCE对比
    # Data1
    mean1 = df_biweekly_1['average_wce']['mean'].values
    std1 = df_biweekly_1['average_wce']['std'].values
    n1 = df_biweekly_1['average_wce']['count'].values
    ci1 = 1.96 * std1 / np.sqrt(n1)
    # Data2
    mean2 = df_biweekly_2['average_wce']['mean'].values
    std2 = df_biweekly_2['average_wce']['std'].values
    n2 = df_biweekly_2['average_wce']['count'].values
    ci2 = 1.96 * std2 / np.sqrt(n2)
    # LOWESS平滑CI带
    x1, lower1, upper1 = lowess_confidence_interval(df_biweekly_1['created_at'].values, mean1, ci1)
    x2, lower2, upper2 = lowess_confidence_interval(df_biweekly_2['created_at'].values, mean2, ci2)
    ax1.fill_between(x1, lower1, upper1, color='grey', alpha=0.20, label='95% CI (Chinese)', zorder=1)
    ax1.fill_between(x2, lower2, upper2, color='lightgrey', alpha=0.30, label='95% CI (Japanese)', zorder=1)
    plot_lowess(df_biweekly_1, 'average_wce', color='black', linestyle='-', label='Mean (Chinese)', ax=ax1)
    plot_lowess(df_biweekly_2, 'average_wce', color='gray', linestyle='--', label='Mean (Japanese)', ax=ax1)
    
    ax1.set_title(r'Comparison of Average WCE Scores (95% CI)')
    ax1.set_ylabel('Average WCE Score')
    ax1.tick_params(axis='x', rotation=45)
    ax1.legend(frameon=False, loc='upper right')  # 统一设置为右侧
    ax1.grid(True, linestyle='--', alpha=0.4)
    
    # 添加子图标签 (a)
    ax1.text(0.5, -0.2, '(a) Warmth-Communion-Evaluation (WCE) Dimension', 
             transform=ax1.transAxes, ha='center', va='top', fontsize=12, fontweight='bold')
    
    # 下方子图：CA对比
    mean1_ca = df_biweekly_1['average_ca']['mean'].values
    std1_ca = df_biweekly_1['average_ca']['std'].values
    n1_ca = df_biweekly_1['average_ca']['count'].values
    ci1_ca = 1.96 * std1_ca / np.sqrt(n1_ca)
    mean2_ca = df_biweekly_2['average_ca']['mean'].values
    std2_ca = df_biweekly_2['average_ca']['std'].values
    n2_ca = df_biweekly_2['average_ca']['count'].values
    ci2_ca = 1.96 * std2_ca / np.sqrt(n2_ca)
    x1_ca, lower1_ca, upper1_ca = lowess_confidence_interval(df_biweekly_1['created_at'].values, mean1_ca, ci1_ca)
    x2_ca, lower2_ca, upper2_ca = lowess_confidence_interval(df_biweekly_2['created_at'].values, mean2_ca, ci2_ca)
    ax2.fill_between(x1_ca, lower1_ca, upper1_ca, color='grey', alpha=0.20, label='95% CI (Chinese)', zorder=1)
    ax2.fill_between(x2_ca, lower2_ca, upper2_ca, color='lightgrey', alpha=0.30, label='95% CI (Japanese)', zorder=1)
    plot_lowess(df_biweekly_1, 'average_ca', color='black', linestyle='-', label='Mean (Chinese)', ax=ax2)
    plot_lowess(df_biweekly_2, 'average_ca', color='gray', linestyle='--', label='Mean (Japanese)', ax=ax2)
    
    ax2.set_title(r'Comparison of Average CA Scores (95% CI)')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Average CA Score')
    ax2.tick_params(axis='x', rotation=45)
    ax2.legend(frameon=False, loc='upper right')  # 统一设置为右侧
    ax2.grid(True, linestyle='--', alpha=0.4)
    
    # 添加子图标签 (b)
    ax2.text(0.5, -0.2, '(b) Competence-Agency (CA) Dimension', 
             transform=ax2.transAxes, ha='center', va='top', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.35)  # 增加子图间距以容纳标签
    plt.savefig('Integrating_SCM_SD/illustrative_study/results/score_processing/combined_comparison_wce_ca.png', dpi=300)

    plt.show()

# 主函数
def main(file_path_1, file_path_2):
    set_academic_style()
    data_1 = read_jsonlines(file_path_1)
    data_2 = read_jsonlines(file_path_2)
    df_grouped_1 = jsonlines_to_dataframe(data_1)
    df_grouped_2 = jsonlines_to_dataframe(data_2)
    df_biweekly_1 = aggregate_biweekly(df_grouped_1)
    df_biweekly_2 = aggregate_biweekly(df_grouped_2)
    plot_combined_comparison(df_biweekly_1, df_biweekly_2)

# 替换为你的数据文件路径
file_path_1 = 'Integrating_SCM_SD/illustrative_study/results/score_processing/sscr/chn_sscr_score.jsonl'
file_path_2 = 'Integrating_SCM_SD/illustrative_study/results/score_processing/sscr/jap_sscr_score.jsonl'
main(file_path_1, file_path_2)