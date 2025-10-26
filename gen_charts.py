# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

years = ['2020', '2021', '2022', '2023', '2024']

# Chart 1
fig, ax = plt.subplots(figsize=(10, 6))
liu_ratio = [1.66, 1.20, 2.41, 2.37, 2.62]
su_ratio = [0.98, 0.55, 1.85, 1.70, 1.93]
asset_liability = [48.09, 41.35, 26.29, 25.44, 23.62]

ax2 = ax.twinx()
line1 = ax.plot(years, liu_ratio, marker='o', linewidth=2, label='流动比率', color='#667eea')
line2 = ax.plot(years, su_ratio, marker='s', linewidth=2, label='速动比率', color='#764ba2')
line3 = ax2.plot(years, asset_liability, marker='^', linewidth=2, label='资产负债率(%)', color='#f093fb')

ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('流动比率/速动比率', fontsize=12)
ax2.set_ylabel('资产负债率(%)', fontsize=12)
ax.set_title('安井食品2020-2024年偿债能力指标趋势图', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc='upper right')

plt.tight_layout()
plt.savefig('chart1.png', dpi=150, bbox_inches='tight')
print("Chart 1 done")

# Chart 2
fig, ax = plt.subplots(figsize=(10, 6))
inventory_turnover = [3.06, 2.99, 3.03, 3.03, 3.53]
receivable_turnover = [19.91, 17.11, 16.54, 24.63, 24.16]
asset_turnover = [0.98, 1.06, 0.75, 0.81, 0.87]

ax2 = ax.twinx()
line1 = ax.plot(years, inventory_turnover, marker='o', linewidth=2, label='存货周转率', color='#667eea')
line2 = ax.plot(years, asset_turnover, marker='s', linewidth=2, label='总资产周转率', color='#764ba2')
line3 = ax2.plot(years, receivable_turnover, marker='^', linewidth=2, label='应收账款周转率', color='#f093fb')

ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('周转率(次)', fontsize=12)
ax2.set_ylabel('应收账款周转率(次)', fontsize=12)
ax.set_title('安井食品2020-2024年营运能力指标趋势图', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc='upper left')

plt.tight_layout()
plt.savefig('chart2.png', dpi=150, bbox_inches='tight')
print("Chart 2 done")

# Chart 3
fig, ax = plt.subplots(figsize=(10, 6))
net_margin = [8.67, 7.41, 9.17, 10.69, 10.01]
roe = [16.39, 13.45, 9.25, 11.50, 11.35]
roa = [8.51, 7.83, 6.92, 8.68, 8.71]

ax.plot(years, net_margin, marker='o', linewidth=2, label='销售净利率(%)', color='#667eea')
ax.plot(years, roe, marker='s', linewidth=2, label='净资产收益率ROE(%)', color='#764ba2')
ax.plot(years, roa, marker='^', linewidth=2, label='总资产收益率ROA(%)', color='#f093fb')

ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('百分比(%)', fontsize=12)
ax.set_title('安井食品2020-2024年盈利能力指标趋势图', fontsize=14, fontweight='bold')
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('chart3.png', dpi=150, bbox_inches='tight')
print("Chart 3 done")

# Chart 4
fig, ax = plt.subplots(figsize=(10, 6))
revenue_growth = [33.12, 31.35, 15.29, 7.70]
profit_growth = [13.75, 61.72, 34.36, 0.83]
years_growth = ['2021', '2022', '2023', '2024']

x = np.arange(len(years_growth))
width = 0.35

bars1 = ax.bar(x - width/2, revenue_growth, width, label='营业收入增长率(%)', color='#667eea')
bars2 = ax.bar(x + width/2, profit_growth, width, label='净利润增长率(%)', color='#764ba2')

ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('增长率(%)', fontsize=12)
ax.set_title('安井食品2021-2024年发展能力指标对比图', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years_growth)
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('chart4.png', dpi=150, bbox_inches='tight')
print("Chart 4 done")

# Chart 5
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

receivables = [3.50, 5.42, 7.37, 5.69, 6.26]
ax1.plot(years, receivables, marker='o', linewidth=2, color='#dc3545', markersize=8)
ax1.fill_between(years, receivables, alpha=0.3, color='#dc3545')
ax1.set_xlabel('年份', fontsize=12)
ax1.set_ylabel('应收账款(亿元)', fontsize=12)
ax1.set_title('应收账款变化趋势（问题1）', fontsize=13, fontweight='bold', color='#dc3545')
ax1.grid(True, alpha=0.3)

for i, v in enumerate(receivables):
    ax1.text(i, v + 0.3, f'{v:.2f}亿', ha='center', va='bottom', fontsize=10)

inventory = [16.91, 24.14, 31.37, 35.67, 32.85]
ax2.plot(years, inventory, marker='s', linewidth=2, color='#dc3545', markersize=8)
ax2.fill_between(years, inventory, alpha=0.3, color='#dc3545')
ax2.set_xlabel('年份', fontsize=12)
ax2.set_ylabel('存货(亿元)', fontsize=12)
ax2.set_title('存货变化趋势（问题2）', fontsize=13, fontweight='bold', color='#dc3545')
ax2.grid(True, alpha=0.3)

for i, v in enumerate(inventory):
    ax2.text(i, v + 1, f'{v:.2f}亿', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('chart5.png', dpi=150, bbox_inches='tight')
print("Chart 5 done")

print("\nAll charts generated!")

