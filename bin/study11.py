# -*- encoding: utf-8 -*-
'''
@file: study10.py
@Author: Xuanlong
@emaial: qxlpku@gmail.com
''' 
# some other scripts for drawing

# list1 = ['good', 'pleasant' ,'pleasant' ,'sympathetic' ,'friendly', 'right' ,'love',
#  'agree', 'trustworthy' ,'honest', 'honest', 'honest', 'tolerant' ,'helpful',
#  'clean' ,'fair' ,'sincere', 'sincere', 'warm', 'public', 'happy', 'truthful',
#  'honesty' ,'considerate', 'considerate' ,'nice' ,'open' ,'nice' ,'caring',
#  'caring']

# list2 = ['good','sympathetic' ,'agree' ,'public', 'pleasant' ,'pleasant' ,'right',
#  'friendly' ,'love','warm', 'open', 'happy' ,'clean', 'tolerant', 'shared',
#  'helpful','trustworthy' ,'bright' ,'entertaining', 'sincere', 'sincere',
#  'honesty' ,'kindly', 'honest' ,'honest' ,'honest' ,'morality' ,'generous',
#  'generous' ,'warmth']

# # Convert lists to sets
# set1 = set(list1)
# set2 = set(list2)
# print(len(set1),len(set2))
# # Find common elements
# common_elements = set1.intersection(set2)

# # Calculate the number of common elements
# number_of_common_words = len(common_elements)

# # Print the result
# print("Number of repeated words:", number_of_common_words)
# print("Repeated words:", common_elements)

import matplotlib.pyplot as plt
import numpy as np

# 定义单词向量
cold = np.array([2.5, 0.1])
friendly = np.array([1, 1])
warm = np.array([2, 1])
hot = np.array([2.2, 0.75])

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制单词向量
# ax.scatter([0, 1, 2, 3], [0, 1, 1, 0])
ax.annotate('cold', (cold + (0.1,0.1)),fontsize=14)
ax.annotate('friendly', (friendly + (0.1,0.1)),fontsize=14)
ax.annotate('warm', (warm + (0.1,0.1)),fontsize=14)
ax.annotate('hot', (hot + (0.1,0.1)),fontsize=14)

# 绘制从原点指向词向量的箭头
ax.arrow(0, 0, cold[0], cold[1], head_width=0.05, head_length=0.05, fc='b', ec='b')
ax.arrow(0, 0, friendly[0], friendly[1], head_width=0.05, head_length=0.05, fc='b', ec='b')
ax.arrow(0, 0, warm[0], warm[1], head_width=0.05, head_length=0.05, fc='b', ec='b')
ax.arrow(0, 0, hot[0], hot[1], head_width=0.05, head_length=0.05, fc='b', ec='b')

# 设置坐标轴范围和标签
ax.set_xlim([- 0.5, 3.5])
ax.set_ylim([- 0.2, 1.5])
ax.set_xlabel('Dimension 1')
ax.set_ylabel('Dimension 2')
ax.set_title('Hypothetical Two-dimensional Semantic Space')

# 添加网格
ax.grid(True)

plt.show()