# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 读取文件
with open('index3.html', 'r', encoding='utf-8') as f:
    index3 = f.read()

with open('index2_updated.html', 'r', encoding='utf-8') as f:
    index2 = f.read()

# 从 index3 提取第5章
start_pos = index3.find('<h1 class="chapter-title">第5章 安井食品并购新宏业借鉴及启示</h1>')
end_pos = index3.find('</div>\n        \n        <!-- 右侧固定导航 -->', start_pos)

if start_pos > 0 and end_pos > start_pos:
    chapter5_content = index3[start_pos:end_pos].strip()
    print(f"[OK] 提取第5章内容 ({len(chapter5_content)} 字符)")
else:
    print("[ERROR] 提取第5章失败")
    sys.exit(1)

# 在 index2 中替换第5章
start_marker = '<h1 class="chapter-title">第5章 安井食品并购新宏业借鉴及启示</h1>'
end_marker = '<!-- 第6章'

start_pos2 = index2.find(start_marker)
end_pos2 = index2.find(end_marker, start_pos2)

if start_pos2 > 0 and end_pos2 > start_pos2:
    # 替换内容
    result = index2[:start_pos2] + chapter5_content + '\n                \n                ' + index2[end_pos2:]
    print("[OK] 替换第5章成功")
    
    # 保存文件
    with open('index2.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print("[OK] 已保存到 index2.html")
else:
    print(f"[ERROR] 未找到替换位置 (start:{start_pos2}, end:{end_pos2})")
    sys.exit(1)

print("[SUCCESS] 完成！")

