import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('class/data/graph.csv',sep='\s+')

# df.plot(x='A', y=['B', 'C', 'D'], kind='line')
# plt.title('Line Graph')
# plt.xlabel('A')
# plt.ylabel('Values of B, C, D')
# plt.grid()
# plt.show()

# df.plot(x='A', y=['B', 'C', 'D'], kind='bar')
# plt.title('Bar Graph')
# plt.xlabel('A')
# plt.ylabel('Values of B, C, D')
# plt.grid()
# plt.show()

# df.plot(x='A', y=['B', 'C', 'D'], kind='scatter')
# plt.title('Scatter Plot')
# plt.xlabel('A')
# plt.ylabel('Values of B, C, D')
# plt.grid()
# plt.show()

# df.plot(x='A', y=['B', 'C', 'D'], kind='hist', bins=10)
# plt.title('Histogram')
# plt.xlabel('A')
# plt.ylabel('Values of B, C, D')
# plt.grid()
# plt.show()      

plt.figure(figsize=(10, 6) )

plt.plot(df['A'], df['B'], marker='o', label='B', color='blue')
plt.plot(df['A'], df['C'], marker='s', label='C', color='orange')
plt.plot(df['A'], df['D'], marker='^', label='D', color='green')


plt.title('Line Graph with Multiple Lines')
plt.xlabel('A')
plt.ylabel('Values of B, C, D')
plt.xticks(df['A'])  # Set x-ticks to the values in column A
plt.grid()
plt.legend()
plt.show()      
#Bar
plt.figure(figsize=(10, 6))

plt.bar(df['A'], df['B'], label='B', color='blue', alpha=0.6, width=0.2, align='center')
plt.bar(df['A'] + 0.2, df['C'], label='C', color='orange', alpha=0.6, width=0.2, align='center')
plt.bar(df['A'] + 0.4, df['D'], label='D', color='green', alpha=0.6, width=0.2, align='center')

plt.title('Bar Graph with Multiple Bars')
plt.xlabel('A')
plt.ylabel('Values of B, C, D')
plt.xticks(df['A'] + 0.2)  # Adjust x-ticks to center the bars
plt.grid(axis='y')
plt.legend()
plt.show()      