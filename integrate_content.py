# -*- coding: utf-8 -*-
"""
将 index3.html 的详细内容整合到 index2.html
"""
from bs4 import BeautifulSoup
import re

print("开始读取文件...")

# 读取 index3.html
with open('index3.html', 'r', encoding='utf-8') as f:
    index3_content = f.read()

# 读取 index2.html
with open('index2.html', 'r', encoding='utf-8') as f:
    index2_content = f.read()

print("文件读取完成")
print("="*80)

# 使用 BeautifulSoup 解析
soup3 = BeautifulSoup(index3_content, 'html.parser')
soup2 = BeautifulSoup(index2_content, 'html.parser')

print("开始提取 index3.html 的内容...")

# 提取 index3 中的各章节
profitability = soup3.find('div', id='profitability')  # 4.2 盈利能力
operating = soup3.find('div', id='operating-capability')  # 4.3 营运能力
growth = soup3.find('div', id='growth-capability')  # 4.4 发展能力
lessons = soup3.find('div', id='lessons-insights')  # 第5章

print(f"提取完成:")
print(f"  - 4.2 盈利能力: {'✓' if profitability else '✗'}")
print(f"  - 4.3 营运能力: {'✓' if operating else '✗'}")
print(f"  - 4.4 发展能力: {'✓' if growth else '✗'}")
print(f"  - 第5章: {'✓' if lessons else '✗'}")
print("="*80)

# 找到 index2 中需要替换的位置
print("查找 index2.html 中需要替换的章节...")
chapter4_3 = soup2.find('h2', string=re.compile(r'4\.3.*盈利能力'))
chapter4_2 = soup2.find('h2', string=re.compile(r'4\.2.*营运能力'))  
chapter4_4 = soup2.find('h2', string=re.compile(r'4\.4.*发展能力'))
chapter5 = soup2.find('h1', string=re.compile(r'第5章'))

print(f"找到章节:")
print(f"  - 4.3 (应该是盈利能力): {'✓' if chapter4_3 else '✗'}")
print(f"  - 4.2 (应该是营运能力): {'✓' if chapter4_2 else '✗'}")
print(f"  - 4.4 发展能力: {'✓' if chapter4_4 else '✗'}")
print(f"  - 第5章: {'✓' if chapter5 else '✗'}")

print("="*80)
print("提示：由于内容结构复杂，建议手动替换")
print("建议操作步骤：")
print("1. 备份 index2.html")
print("2. 从 index3.html 复制 4.2盈利能力 的完整内容")
print("3. 替换 index2.html 中的 4.3盈利能力 内容")
print("4. 从 index3.html 复制 4.3营运能力 的完整内容")
print("5. 替换 index2.html 中的 4.2营运能力 内容")
print("6. 同样处理 4.4 和第5章")
print("="*80)

