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
a=row=df.loc[0, ['A']]  # Accessing the first row and column 'A'
b=row=df.loc[1, ['A']]  # Accessing the second row and column 'A'
c=row=df.loc[2, ['A']]  # Accessing the third row and column 'A'
d=row=df.loc[3, ['A']]  # Accessing the fourth row and column 'A'   

avg=a = (a + b) / 2 # Calculating the average of the values in column 'A'
# avg = (c + d) / 2 # Calculating the average of the values in column 'A'   

print(f"Average of column A: {avg}")



# row
# row1_avg = df.loc[0, ['A']]  
# row2_avg = df.loc[1, ['A']]
# average = row1

# print(f"Average of row 1 (B, C, D): {row1_avg}")
# print(f"Average of row 2 (B, C, D): {row2_avg}")

# average = (df['B'].mean() + df['C'].mean() + df['D'].mean()) / 3
     

# plt.figure(figsize=(10, 6) )

# average_a = df[['A']].mean().mean()
# average_b = df[['B']].mean().mean()
# average_c = df[['C']].mean().mean()
# average_d = df[['D']].mean().mean()  

# average_1 = (average_a + average_b ) / 2


# plt.plot(df['A'], df['B'], marker='o', label='B', color='blue')
# plt.plot(df['A'], df['C'], marker='s', label='C', color='orange')
# plt.plot(df['A'], df['D'], marker='^', label='D', color='green')        
# plt.axhline(y=average, color='red', linestyle='--', label='Average')    

# # plt.plot(df['A'], df['B'], marker='o', label='B', color='blue')
# # plt.plot(df['A'], df['C'], marker='s', label='C', color='orange')
# # plt.plot(df['A'], df['D'], marker='^', label='D', color='green')


# plt.title('Line Graph with Multiple Lines')
# plt.xlabel('A')
# plt.ylabel('Values of B, C, D')
# plt.xticks(df['A'])  # Set x-ticks to the values in column A
# plt.grid()
# plt.legend()
# plt.show()      
# #Bar
# plt.figure(figsize=(10, 6))

# plt.bar(df['A'], df['B'], label='B', color='blue', alpha=0.6, width=0.2, align='center')
# plt.bar(df['A'] + 0.2, df['C'], label='C', color='orange', alpha=0.6, width=0.2, align='center')
# plt.bar(df['A'] + 0.4, df['D'], label='D', color='green', alpha=0.6, width=0.2, align='center')

# plt.title('Bar Graph with Multiple Bars')
# plt.xlabel('A')
# plt.ylabel('Values of B, C, D')
# plt.xticks(df['A'] + 0.2)  # Adjust x-ticks to center the bars
# plt.grid(axis='y')
# plt.legend()
# plt.show()      