import json

def calculate_avg_text_length(file_path):
    total_words = 0
    total_lines = 0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            data = json.loads(line)
            
            # 获取 text 字段（需要先获取 author_id 下的内容）
            for author_id, content in data.items():
                text = content.get('text', '')
                word_count = len(text.split())
                total_words += word_count
                total_lines += 1
    
    if total_lines == 0:
        return 0
    print(f"总行数: {total_lines}")
    print(f"总单词数: {total_words}")
    avg = total_words / total_lines
    return avg

# 使用示例
file_path = 'Integrating_SCM_SD/illustrative_study/results/post_precessing/chn_sscr_output.json'  # 替换成你的文件路径
avg_length = calculate_avg_text_length(file_path)


print(f"平均每行单词数: {avg_length:.2f}")