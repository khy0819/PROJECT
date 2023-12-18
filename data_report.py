import matplotlib.pyplot as plt
import pandas as pd

# 주어진 데이터
data = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
    'Total Sales': [5280000, 5501000, 5469000, 5480000, 5533000, 5554000],
    'Target Sales': [5280000, 5500000, 5729000, 5968000, 6217000, 6476000],
    'Advertising Costs': [1056000, 950400, 739200, 528000, 316800, 316800],
    'Social Network Costs': [0, 105600, 316800, 528000, 739200, 739200],
    'Unit Price per Ounce': [2.00, 2.00, 2.00, 1.90, 1.90, 1.90]
}

# 데이터프레임 생성
df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# 그래프 생성
plt.figure(figsize=(12, 8))

# Total Sales 및 Target Sales 그래프
plt.subplot(2, 2, 1)
df[['Total Sales', 'Target Sales']].plot(kind='bar', ax=plt.gca())
plt.title('Total Sales vs Target Sales')

# Advertising Costs 그래프
plt.subplot(2, 2, 2)
df['Advertising Costs'].plot(kind='line', marker='o', color='r', ax=plt.gca())
plt.title('Advertising Costs')

# Social Network Costs 그래프
plt.subplot(2, 2, 3)
df['Social Network Costs'].plot(kind='line', marker='o', color='b', ax=plt.gca())
plt.title('Social Network Costs')

# Unit Price per Ounce 그래프
plt.subplot(2, 2, 4)
df['Unit Price per Ounce'].plot(kind='line', marker='o', color='g', ax=plt.gca())
plt.title('Unit Price per Ounce')

# 레이아웃 조정
plt.tight_layout()
plt.show()
