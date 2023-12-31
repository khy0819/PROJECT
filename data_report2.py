import matplotlib.pyplot as plt
import pandas as pd

# 주어진 데이터
data = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
    'Total Sales': [5280000, 5501000, 5469000, 5480000, 5533000, 5554000],
    'Target Sales': [5280000, 5500000, 5729000, 5968000, 6217000, 6476000],
}

# 데이터프레임 생성
df_sales = pd.DataFrame(data)
df_sales.set_index('Month', inplace=True)

# 그래프 생성
plt.figure(figsize=(10, 6))

# Total Sales 및 Target Sales 그래프
df_sales[['Total Sales', 'Target Sales']].plot(kind='bar', ax=plt.gca())
plt.title('총 매출과 목표 매출 비교')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

# 그래프 표시
plt.show()
