import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('alayande.csv')
df1=pd.read_csv('alayande1.csv')

df['date']=pd.to_datetime(df['date'])
df1['date']=pd.to_datetime(df1['date'])
print(df.head(4),"\n",df1.head(4))

print(df.isnull().sum(),"\n",df1.isnull().sum())
df=df.fillna(method='bfill')
print(df)
print(df.isnull().sum())

df_merg=df.merge(df1)
print(df_merg)

numeric_df = df_merg.select_dtypes(include='number')
df_cor=numeric_df.corr()['respiratory']
print(df_cor)
df_cor=numeric_df.corr()

plt.Figure(figsize=(10,10))
sns.heatmap(df_cor,annot=True,cmap='coolwarm')
plt.show()

polluted_day=df_merg[df_merg['SO2']>40]
polluted_count=polluted_day.groupby(['date','SO2']).size().reset_index()
print(polluted_count.sort_values(by='SO2',ascending=False))

plt.figure(figsize=(10,10))
sns.barplot(df_merg['SO2'],palette='Reds')
plt.title('pollutedDays')
plt.show()

plt.Figure(figsize=(10,20))
sns.scatterplot(data=df_merg,x='SO2',y='respiratory')
plt.show()


