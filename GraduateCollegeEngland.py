# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:50:18 2024

@author: Zahin
"""

import matplotlib.pyplot as plt
plt.ion()
revenue_streams = {
    "Tuition Fees": 11675000,
    "Grants and Funding": 850000,
    "Partnerships and Collaborations": 750000,
    "Online Learning Platforms": 950000,
    "Consulting and Custom Training": 650000,
    "Ancillary Services": 125000
}
cost_categories = {
    "Operational Costs": 2950000,
    "Technology and Infrastructure": 1750000,
    "Course Development and Delivery": 2805000,
    "Marketing and Student Acquisition": 555600,
    "Partnerships and Collaborations": 156000,
    "Student Support Services": 800000,
    "Recruitment Services": 120000
}
total_revenue = 15000000
total_costs = 8436600
estimated_profit = total_revenue - total_costs
payback_time_years = 1.52
fig1, ax1 = plt.subplots(figsize=(10, 6))
bars = ax1.bar(revenue_streams.keys(), revenue_streams.values(), color='skyblue')
ax1.set_xlabel('Revenue Stream')
ax1.set_ylabel('Revenue (£)')
ax1.set_title('Revenue Breakdown by Stream')
plt.xticks(rotation=45, ha="right")
def on_click(event):
    for bar in bars:
        if bar.contains(event)[0]:
            plt.text(event.xdata, event.ydata, f'Revenue: £{bar.get_height():,.0f}', fontsize=10, color='red')
            plt.draw()

fig1.canvas.mpl_connect('button_press_event', on_click)

plt.tight_layout()
plt.show()

fig2, ax2 = plt.subplots(figsize=(10, 6))
bars = ax2.bar(cost_categories.keys(), cost_categories.values(), color='lightcoral')
ax2.set_xlabel('Cost Category')
ax2.set_ylabel('Costs (£)')
ax2.set_title('Cost Breakdown by Category')
plt.xticks(rotation=45, ha="right")


def on_click(event):
    for bar in bars:
        if bar.contains(event)[0]:
            plt.text(event.xdata, event.ydata, f'Cost: £{bar.get_height():,.0f}', fontsize=10, color='red')
            plt.draw()

fig2.canvas.mpl_connect('button_press_event', on_click)

plt.tight_layout()
plt.show()

fig3, ax3 = plt.subplots(figsize=(8, 5))
bars = ax3.bar(['Total Revenue', 'Total Costs'], [total_revenue, total_costs], color=['skyblue', 'lightcoral'])
ax3.set_xlabel('Financial Overview')
ax3.set_ylabel('Amount (£)')
ax3.set_title('Total Revenue vs Total Costs')

def on_click(event):
    for bar in bars:
        if bar.contains(event)[0]:
            plt.text(event.xdata, event.ydata, f'Value: £{bar.get_height():,.0f}', fontsize=10, color='red')
            plt.draw()

fig3.canvas.mpl_connect('button_press_event', on_click)

plt.tight_layout()
plt.show()

fig4, ax4 = plt.subplots(figsize=(8, 5))

# Estimated Profit Bar
bars = ax4.bar(['Estimated Annual Profit'], [estimated_profit], color='lightgreen')
ax4.set_ylabel('Profit (£)')
ax4.set_title('Estimated Annual Profit and Payback Time')

def on_click(event):
    for bar in bars:
        if bar.contains(event)[0]:
            payback_time_text = f'Payback Time: {payback_time_years:.2f} years (approx. {payback_time_years * 12:.1f} months)'
            plt.text(event.xdata, event.ydata / 2, payback_time_text, fontsize=10, color='black')
            plt.draw()

fig4.canvas.mpl_connect('button_press_event', on_click)

plt.tight_layout()
plt.show()

fig5, ax5 = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax5.pie(revenue_streams.values(), labels=revenue_streams.keys(), autopct='%1.1f%%', startangle=140)
ax5.set_title('Revenue Streams Proportional Breakdown')

def on_click(event):
    for wedge in wedges:
        if wedge.contains(event)[0]:
            wedge.set_edgecolor('red')
            plt.draw()

fig5.canvas.mpl_connect('button_press_event', on_click)

plt.tight_layout()
plt.show()

fig6, ax6 = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax6.pie(cost_categories.values(), labels=cost_categories.keys(), autopct='%1.1f%%', startangle=140)
ax6.set_title('Cost Categories Proportional Breakdown')

def on_click(event):
    for wedge in wedges:
        if wedge.contains(event)[0]:
            wedge.set_edgecolor('red')
            plt.draw()

fig6.canvas.mpl_connect('button_press_event', on_click)

plt.tight_layout()
plt.show()

