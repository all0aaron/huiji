# -*- coding: utf-8 -*-
"""
自动整合 index3.html 的详细内容到 index2.html
"""
import re
import sys
import io

# 设置输出编码为 utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 80)
print("开始整合 index3.html 内容到 index2.html")
print("=" * 80)

# 读取文件
try:
    with open('index3.html', 'r', encoding='utf-8') as f:
        index3 = f.read()
    print("[OK] 读取 index3.html 成功")
except Exception as e:
    print(f"[ERROR] 读取 index3.html 失败: {e}")
    sys.exit(1)

try:
    with open('index2.html', 'r', encoding='utf-8') as f:
        index2 = f.read()
    print("[OK] 读取 index2.html 成功")
except Exception as e:
    print(f"[ERROR] 读取 index2.html 失败: {e}")
    sys.exit(1)

print()
print("=" * 80)
print("提取 index3.html 中的章节内容")
print("=" * 80)

# ============================================================
# 提取 index3.html 中的章节内容
# ============================================================

# 提取 4.2 盈利能力分析 (index3中是 id="profitability")
# 从 <div class="chapter" id="profitability"> 到 4.3章节之前
profitability_start = index3.find('<div class="chapter" id="profitability">')
profitability_end = index3.find('<!-- 4.3 营运能力分析 -->', profitability_start)

if profitability_start > 0 and profitability_end > profitability_start:
    profitability_content = index3[profitability_start:profitability_end].strip()
    # 移除最外层的 div
    profitability_content = re.sub(r'<div class="chapter" id="profitability">\s*', '', profitability_content, count=1)
    profitability_content = re.sub(r'</div>\s*$', '', profitability_content, count=1)
    print("[OK] 提取 4.2 盈利能力分析 (约 {} 字符)".format(len(profitability_content)))
else:
    profitability_content = None
    print("[ERROR] 提取 4.2 盈利能力分析失败")

# 提取 4.3 营运能力分析
operating_start = index3.find('<div class="chapter" id="operating-capability">')
operating_end = index3.find('<!-- 4.4 发展能力分析 -->', operating_start)

if operating_start > 0 and operating_end > operating_start:
    operating_content = index3[operating_start:operating_end].strip()
    operating_content = re.sub(r'<div class="chapter" id="operating-capability">\s*', '', operating_content, count=1)
    operating_content = re.sub(r'</div>\s*$', '', operating_content, count=1)
    print("[OK] 提取 4.3 营运能力分析 (约 {} 字符)".format(len(operating_content)))
else:
    operating_content = None
    print("[ERROR] 提取 4.3 营运能力分析失败")

# 提取 4.4 发展能力分析
growth_start = index3.find('<div class="chapter" id="growth-capability">')
growth_end = index3.find('<!-- 第5章 借鉴及启示 -->', growth_start)

if growth_start > 0 and growth_end > growth_start:
    growth_content = index3[growth_start:growth_end].strip()
    growth_content = re.sub(r'<div class="chapter" id="growth-capability">\s*', '', growth_content, count=1)
    growth_content = re.sub(r'</div>\s*$', '', growth_content, count=1)
    print("[OK] 提取 4.4 发展能力分析 (约 {} 字符)".format(len(growth_content)))
else:
    growth_content = None
    print("[ERROR] 提取 4.4 发展能力分析失败")

# 提取第5章
lessons_start = index3.find('<div class="chapter" id="lessons-insights">')
# 找到第5章的结束位置（章节div结束前）
lessons_temp = index3[lessons_start:]
# 计算配对的div
div_count = 0
lessons_end = -1
i = lessons_start
while i < len(index3):
    if index3[i:i+5] == '<div ':
        div_count += 1
    elif index3[i:i+6] == '</div>':
        div_count -= 1
        if div_count == 0:
            lessons_end = i
            break
    i += 1

if lessons_start > 0 and lessons_end > lessons_start:
    lessons_content = index3[lessons_start:lessons_end].strip()
    lessons_content = re.sub(r'<div class="chapter" id="lessons-insights">\s*', '', lessons_content, count=1)
    print("[OK] 提取第5章 (约 {} 字符)".format(len(lessons_content)))
else:
    lessons_content = None
    print("[ERROR] 提取第5章失败")

print()
print("=" * 80)
print("开始替换 index2.html 中的内容")
print("=" * 80)

# ============================================================
# 在 index2.html 中进行替换
# ============================================================
result_index2 = index2

# 1. 替换 4.3 盈利能力分析（index2中编号错误，应该是4.2）
if profitability_content:
    # 找到开始和结束位置
    start_marker = '<h2 class="section-title" id="c4s3">4.3 盈利能力分析</h2>'
    end_marker = '<h2 class="section-title" id="c4s4">4.4 发展能力分析</h2>'
    
    start_pos = result_index2.find(start_marker)
    end_pos = result_index2.find(end_marker, start_pos)
    
    if start_pos > 0 and end_pos > start_pos:
        # 构建新内容
        new_content = start_marker + '\n                    \n' + profitability_content + '\n                    \n                    '
        # 替换
        result_index2 = result_index2[:start_pos] + new_content + result_index2[end_pos:]
        print("[OK] 替换 4.3 盈利能力分析成功")
    else:
        print("[ERROR] 未找到 4.3 盈利能力分析章节位置")

# 2. 替换 4.2 营运能力分析（index2中编号错误，应该是4.3）
if operating_content:
    start_marker = '<h2 class="section-title" id="c4s2">4.2 营运能力分析</h2>'
    end_marker = '<h2 class="section-title" id="c4s3">4.3 盈利能力分析</h2>'
    
    start_pos = result_index2.find(start_marker)
    end_pos = result_index2.find(end_marker, start_pos)
    
    if start_pos > 0 and end_pos > start_pos:
        new_content = start_marker + '\n                    \n' + operating_content + '\n                    \n                    '
        result_index2 = result_index2[:start_pos] + new_content + result_index2[end_pos:]
        print("[OK] 替换 4.2 营运能力分析成功")
    else:
        print("[ERROR] 未找到 4.2 营运能力分析章节位置")

# 3. 替换 4.4 发展能力分析
if growth_content:
    start_marker = '<h2 class="section-title" id="c4s4">4.4 发展能力分析</h2>'
    # 找到第5章的开始作为结束标记
    end_marker_patterns = [
        '<!-- 第5章',
        '<h1 class="chapter-title" id="c5">第5章'
    ]
    
    start_pos = result_index2.find(start_marker)
    end_pos = -1
    for pattern in end_marker_patterns:
        temp_pos = result_index2.find(pattern, start_pos)
        if temp_pos > start_pos:
            end_pos = temp_pos
            break
    
    if start_pos > 0 and end_pos > start_pos:
        new_content = start_marker + '\n                    \n' + growth_content + '\n                    \n                '
        result_index2 = result_index2[:start_pos] + new_content + result_index2[end_pos:]
        print("[OK] 替换 4.4 发展能力分析成功")
    else:
        print("[ERROR] 未找到 4.4 发展能力分析章节位置")

# 4. 替换第5章
if lessons_content:
    # 找到第5章的开始
    start_marker = '<h1 class="chapter-title" id="c5">第5章'
    # 找到第6章的开始作为结束
    end_marker = '<!-- 第6章'
    
    start_pos = result_index2.find(start_marker)
    # 需要找到h1标签之前的div开始
    if start_pos > 0:
        # 向前查找<div class="chapter">
        temp_pos = start_pos
        while temp_pos > 0:
            if result_index2[temp_pos:temp_pos+19] == '<div class="chapter">':
                start_pos = temp_pos
                break
            temp_pos -= 1
    
    end_pos = result_index2.find(end_marker, start_pos)
    
    if start_pos > 0 and end_pos > start_pos:
        # 保持缩进
        indent = '                '
        new_content = indent + '<div class="chapter">\n                    ' + lessons_content + '\n                </div>\n\n                '
        result_index2 = result_index2[:start_pos] + new_content + result_index2[end_pos:]
        print("[OK] 替换第5章成功")
    else:
        print("[ERROR] 未找到第5章位置 (start: {}, end: {})".format(start_pos, end_pos))

# 保存结果
print()
print("=" * 80)
print("保存更新后的文件...")

try:
    with open('index2_updated.html', 'w', encoding='utf-8') as f:
        f.write(result_index2)
    print("[OK] 文件已保存为 index2_updated.html")
except Exception as e:
    print(f"[ERROR] 保存文件失败: {e}")
    sys.exit(1)

print("=" * 80)
print("[SUCCESS] 整合完成!")
print()
print("提示：请检查 index2_updated.html 确认内容正确后，")
print("     再将其重命名为 index2.html 替换原文件。")
print("=" * 80)
