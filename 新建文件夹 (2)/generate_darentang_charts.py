# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
import sys
import io
import numpy as np
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 强制设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'SimSun', 'KaiTi', 'FangSong', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 读取Excel文件
excel_file = '达仁堂营运能力分析.xlsx'
print(f"正在读取文件: {excel_file}")

try:
    # 读取第一个工作表
    df = pd.read_excel(excel_file, sheet_name=0, header=0)
    
    # 第一行是标题行，提取年份
    years = df.iloc[0, 1:].values.tolist()  # 2024年, 2023年, 2022年, 2021年, 2020年
    # 提取年份数字用于排序（从2020到2024）
    year_labels = [y.replace('年', '') for y in years]
    year_nums = [int(y) for y in year_labels]
    
    # 提取数据行
    data_dict = {}
    for idx, row in df.iterrows():
        if idx == 0:  # 跳过标题行
            continue
        key = str(row.iloc[0]).strip()
        values = row.iloc[1:].values.tolist()
        data_dict[key] = values
    
    # 提取需要的指标
    # 营业收入（亿元）
    revenue = data_dict['营业收入（元）']
    revenue_billion = [float(str(x).replace(',', '')) / 100000000 if pd.notna(x) else 0 for x in revenue]
    
    # 应收账款周转率
    ar_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['应收账款周转率%']]
    
    # 存货周转率（注意Excel中是"存货资产周转率%"）
    inv_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['存货资产周转率%']]
    
    # 流动资产周转率
    ca_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['流动资产周转率%']]
    
    # 固定资产周转率
    fa_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['固定资产周转率%']]
    
    # 总资产周转率
    ta_turnover = [float(str(x)) if pd.notna(x) else 0 for x in data_dict['总资产周转率%']]
    
    # 反转数据顺序（从2020到2024）
    year_labels = year_labels[::-1]
    revenue_billion = revenue_billion[::-1]
    ar_turnover = ar_turnover[::-1]
    inv_turnover = inv_turnover[::-1]
    ca_turnover = ca_turnover[::-1]
    fa_turnover = fa_turnover[::-1]
    ta_turnover = ta_turnover[::-1]
    
    print(f"\n年份顺序: {year_labels}")
    print(f"营业收入(亿元): {revenue_billion}")
    print(f"应收账款周转率: {ar_turnover}")
    print(f"存货周转率: {inv_turnover}")
    print(f"流动资产周转率: {ca_turnover}")
    print(f"固定资产周转率: {fa_turnover}")
    print(f"总资产周转率: {ta_turnover}")
    
    # 设置图表样式
    plt.style.use('default')
    fig_size = (12, 6)
    
    # ========== 图表1：应收账款周转率和存货周转率 ==========
    fig1, ax1 = plt.subplots(figsize=fig_size)
    
    # 绘制折线图
    line1 = ax1.plot(year_labels, ar_turnover, marker='o', linewidth=2.5, markersize=8, 
                     label='应收账款周转率', color='#667eea', markerfacecolor='white', markeredgewidth=2)
    line2 = ax1.plot(year_labels, inv_turnover, marker='s', linewidth=2.5, markersize=8, 
                     label='存货周转率', color='#764ba2', markerfacecolor='white', markeredgewidth=2)
    
    # 设置标题和标签
    ax1.set_title('达仁堂应收账款周转率与存货周转率趋势', fontsize=16, fontweight='bold', pad=20)
    ax1.set_xlabel('年份', fontsize=12, fontweight='bold')
    ax1.set_ylabel('周转率（次）', fontsize=12, fontweight='bold')
    
    # 添加网格
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # 添加图例 - 确保中文显示
    legend = ax1.legend(loc='best', fontsize=11, framealpha=0.9)
    # 设置图例文字
    for text in legend.get_texts():
        text.set_fontfamily('Microsoft YaHei')
    
    # 添加数值标签
    for i, (ar, inv) in enumerate(zip(ar_turnover, inv_turnover)):
        ax1.annotate(f'{ar:.2f}', (i, ar), textcoords="offset points", xytext=(0,10), 
                    ha='center', fontsize=9, color='#667eea', fontweight='bold')
        ax1.annotate(f'{inv:.2f}', (i, inv), textcoords="offset points", xytext=(0,-15), 
                    ha='center', fontsize=9, color='#764ba2', fontweight='bold')
    
    plt.tight_layout()
    chart1_name = '达仁堂图表1_应收账款和存货周转率.png'
    plt.savefig(chart1_name, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"\n✅ 图表1已保存: {chart1_name}")
    plt.close()
    
    # ========== 图表2：流动资产、固定资产、总资产周转率 ==========
    fig2, ax2 = plt.subplots(figsize=fig_size)
    
    # 绘制折线图
    line3 = ax2.plot(year_labels, ca_turnover, marker='o', linewidth=2.5, markersize=8, 
                     label='流动资产周转率', color='#f093fb', markerfacecolor='white', markeredgewidth=2)
    line4 = ax2.plot(year_labels, fa_turnover, marker='s', linewidth=2.5, markersize=8, 
                     label='固定资产周转率', color='#4facfe', markerfacecolor='white', markeredgewidth=2)
    line5 = ax2.plot(year_labels, ta_turnover, marker='^', linewidth=2.5, markersize=8, 
                     label='总资产周转率', color='#43e97b', markerfacecolor='white', markeredgewidth=2)
    
    # 设置标题和标签
    ax2.set_title('达仁堂资产周转率趋势分析', fontsize=16, fontweight='bold', pad=20)
    ax2.set_xlabel('年份', fontsize=12, fontweight='bold')
    ax2.set_ylabel('周转率（次）', fontsize=12, fontweight='bold')
    
    # 添加网格
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    # 添加图例 - 确保中文显示
    legend2 = ax2.legend(loc='best', fontsize=11, framealpha=0.9)
    for text in legend2.get_texts():
        text.set_fontfamily('Microsoft YaHei')
    
    # 添加数值标签
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
    
    # ========== 图表3：营业收入折线图 ==========
    fig3, ax3 = plt.subplots(figsize=fig_size)
    
    # 绘制折线图
    line6 = ax3.plot(year_labels, revenue_billion, marker='o', linewidth=3, markersize=10, 
                     label='营业收入', color='#ff6b6b', markerfacecolor='white', markeredgewidth=3)
    
    # 设置标题和标签
    ax3.set_title('达仁堂营业收入趋势（2020-2024年）', fontsize=16, fontweight='bold', pad=20)
    ax3.set_xlabel('年份', fontsize=12, fontweight='bold')
    ax3.set_ylabel('营业收入（亿元）', fontsize=12, fontweight='bold')
    
    # 添加网格
    ax3.grid(True, alpha=0.3, linestyle='--')
    
    # 添加图例 - 确保中文显示
    legend3 = ax3.legend(loc='best', fontsize=11, framealpha=0.9)
    for text in legend3.get_texts():
        text.set_fontfamily('Microsoft YaHei')
    
    # 添加数值标签
    for i, rev in enumerate(revenue_billion):
        ax3.annotate(f'{rev:.2f}亿', (i, rev), textcoords="offset points", xytext=(0,15), 
                    ha='center', fontsize=10, color='#ff6b6b', fontweight='bold')
    
    # 填充区域
    ax3.fill_between(year_labels, revenue_billion, alpha=0.2, color='#ff6b6b')
    
    plt.tight_layout()
    chart3_name = '达仁堂图表3_营业收入.png'
    plt.savefig(chart3_name, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"✅ 图表3已保存: {chart3_name}")
    plt.close()
    
    # ========== 营业收入数据输出 ==========
    print(f"\n{'='*60}")
    print("营业收入数据（亿元）:")
    print(f"{'='*60}")
    for year, rev in zip(year_labels, revenue_billion):
        print(f"{year}年: {rev:.2f} 亿元")
    
    print(f"\n✅ 所有图表生成完成！")
    
except Exception as e:
    print(f"处理文件时出错: {e}")
    import traceback
    traceback.print_exc()
