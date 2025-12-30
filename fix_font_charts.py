# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
import sys
import io
import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 查找系统中的中文字体
def find_chinese_font():
    """查找系统中可用的中文字体"""
    font_list = []
    for font in fm.fontManager.ttflist:
        font_name = font.name
        # 检查是否是中文字体
        if any(name in font_name for name in ['Microsoft YaHei', 'SimHei', 'SimSun', 'KaiTi', 'FangSong', 'STSong', 'STHeiti']):
            font_list.append(font_name)
    
    if font_list:
        print(f"找到中文字体: {font_list[0]}")
        return font_list[0]
    else:
        print("未找到中文字体，尝试使用默认设置")
        return None

# 设置字体
chinese_font = find_chinese_font()
if chinese_font:
    plt.rcParams['font.sans-serif'] = [chinese_font]
else:
    # 尝试直接设置Windows常见字体
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# 读取Excel文件
excel_file = '达仁堂营运能力分析.xlsx'
print(f"\n正在读取文件: {excel_file}")

try:
    # 读取第一个工作表
    df = pd.read_excel(excel_file, sheet_name=0, header=0)
    
    # 第一行是标题行，提取年份
    years = df.iloc[0, 1:].values.tolist()
    year_labels = [y.replace('年', '') for y in years]
    
    # 提取数据行
    data_dict = {}
    for idx, row in df.iterrows():
        if idx == 0:
            continue
        key = str(row.iloc[0]).strip()
        values = row.iloc[1:].values.tolist()
        data_dict[key] = values
    
    # 提取需要的指标
    revenue = data_dict['营业收入（元）']
    revenue_billion = [float(str(x).replace(',', '')) / 100000000 if pd.notna(x) else 0 for x in revenue]
    ar_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['应收账款周转率%']]
    inv_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['存货资产周转率%']]
    ca_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['流动资产周转率%']]
    fa_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['固定资产周转率%']]
    ta_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['总资产周转率%']]
    
    # 反转数据顺序（从2020到2024）
    year_labels = year_labels[::-1]
    revenue_billion = revenue_billion[::-1]
    ar_turnover = ar_turnover[::-1]
    inv_turnover = inv_turnover[::-1]
    ca_turnover = ca_turnover[::-1]
    fa_turnover = fa_turnover[::-1]
    ta_turnover = ta_turnover[::-1]
    
    fig_size = (12, 6)
    
    # ========== 图表1：应收账款周转率和存货周转率 ==========
    fig1, ax1 = plt.subplots(figsize=fig_size)
    
    line1 = ax1.plot(year_labels, ar_turnover, marker='o', linewidth=2.5, markersize=8, 
                     label='应收账款周转率', color='#667eea', markerfacecolor='white', markeredgewidth=2)
    line2 = ax1.plot(year_labels, inv_turnover, marker='s', linewidth=2.5, markersize=8, 
                     label='存货周转率', color='#764ba2', markerfacecolor='white', markeredgewidth=2)
    
    ax1.set_title('达仁堂应收账款周转率与存货周转率趋势', fontsize=16, fontweight='bold', pad=20)
    ax1.set_xlabel('年份', fontsize=12, fontweight='bold')
    ax1.set_ylabel('周转率（次）', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # 设置图例，确保中文显示
    legend1 = ax1.legend(loc='best', fontsize=11, framealpha=0.9, prop={'family': chinese_font if chinese_font else 'sans-serif'})
    
    # 添加数值标签
    for i, (ar, inv) in enumerate(zip(ar_turnover, inv_turnover)):
        ax1.annotate(f'{ar:.2f}', (i, ar), textcoords="offset points", xytext=(0,10), 
                    ha='center', fontsize=9, color='#667eea', fontweight='bold')
        ax1.annotate(f'{inv:.2f}', (i, inv), textcoords="offset points", xytext=(0,-15), 
                    ha='center', fontsize=9, color='#764ba2', fontweight='bold')
    
    plt.tight_layout()
    chart1_name = '达仁堂图表1_应收账款和存货周转率.png'
    plt.savefig(chart1_name, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ 图表1已保存: {chart1_name}")
    plt.close()
    
    # ========== 图表2：资产周转率 ==========
    fig2, ax2 = plt.subplots(figsize=fig_size)
    
    line3 = ax2.plot(year_labels, ca_turnover, marker='o', linewidth=2.5, markersize=8, 
                     label='流动资产周转率', color='#f093fb', markerfacecolor='white', markeredgewidth=2)
    line4 = ax2.plot(year_labels, fa_turnover, marker='s', linewidth=2.5, markersize=8, 
                     label='固定资产周转率', color='#4facfe', markerfacecolor='white', markeredgewidth=2)
    line5 = ax2.plot(year_labels, ta_turnover, marker='^', linewidth=2.5, markersize=8, 
                     label='总资产周转率', color='#43e97b', markerfacecolor='white', markeredgewidth=2)
    
    ax2.set_title('达仁堂资产周转率趋势分析', fontsize=16, fontweight='bold', pad=20)
    ax2.set_xlabel('年份', fontsize=12, fontweight='bold')
    ax2.set_ylabel('周转率（次）', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    legend2 = ax2.legend(loc='best', fontsize=11, framealpha=0.9, prop={'family': chinese_font if chinese_font else 'sans-serif'})
    
    for i, (ca, fa, ta) in enumerate(zip(ca_turnover, fa_turnover, ta_turnover)):
        ax2.annotate(f'{ca:.2f}', (i, ca), textcoords="offset points", xytext=(0,10), 
                    ha='center', fontsize=9, color='#f093fb', fontweight='bold')
        ax2.annotate(f'{fa:.2f}', (i, fa), textcoords="offset points", xytext=(0,10), 
                    ha='center', fontsize=9, color='#4facfe', fontweight='bold')
        ax2.annotate(f'{ta:.2f}', (i, ta), textcoords="offset points", xytext=(0,-15), 
                    ha='center', fontsize=9, color='#43e97b', fontweight='bold')
    
    plt.tight_layout()
    chart2_name = '达仁堂图表2_资产周转率.png'
    plt.savefig(chart2_name, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ 图表2已保存: {chart2_name}")
    plt.close()
    
    # ========== 图表3：营业收入 ==========
    fig3, ax3 = plt.subplots(figsize=fig_size)
    
    line6 = ax3.plot(year_labels, revenue_billion, marker='o', linewidth=3, markersize=10, 
                     label='营业收入', color='#ff6b6b', markerfacecolor='white', markeredgewidth=3)
    
    ax3.set_title('达仁堂营业收入趋势（2020-2024年）', fontsize=16, fontweight='bold', pad=20)
    ax3.set_xlabel('年份', fontsize=12, fontweight='bold')
    ax3.set_ylabel('营业收入（亿元）', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3, linestyle='--')
    
    legend3 = ax3.legend(loc='best', fontsize=11, framealpha=0.9, prop={'family': chinese_font if chinese_font else 'sans-serif'})
    
    for i, rev in enumerate(revenue_billion):
        ax3.annotate(f'{rev:.2f}亿', (i, rev), textcoords="offset points", xytext=(0,15), 
                    ha='center', fontsize=10, color='#ff6b6b', fontweight='bold')
    
    ax3.fill_between(year_labels, revenue_billion, alpha=0.2, color='#ff6b6b')
    
    plt.tight_layout()
    chart3_name = '达仁堂图表3_营业收入.png'
    plt.savefig(chart3_name, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ 图表3已保存: {chart3_name}")
    plt.close()
    
    print(f"\n✅ 所有图表重新生成完成！")
    
except Exception as e:
    print(f"处理文件时出错: {e}")
    import traceback
    traceback.print_exc()

