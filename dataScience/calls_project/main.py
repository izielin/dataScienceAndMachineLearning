import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../calls_project/input/911.csv')
print(df.info())
print(df.head())

print(df['zip'].value_counts().head(5))
print(df['twp'].value_counts().head(5))
print(len(df['title'].unique()))  # df['title'].unique()

# x = df['title'].iloc[0]
# print(x.split(':')[0])
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df['Reason'])
print(df['Reason'].value_counts())

# sns.countplot(x='Reason', data=df, palette='viridis')

print(df.info())
print(type(df['timeStamp'].iloc[0]))

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
print(type(df['timeStamp'].iloc[0]))

time = df['timeStamp'].iloc[0]
print(time)
print(time.hour)
print(time.year)
print(time.dayofweek)

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

print(df.head())

day_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

df['Day of week'] = df['Day of week'].map(day_map)

print(df.head())

# sns.countplot(x='Day of week', data=df, hue='Reason')
by_month = df.groupby('Month').count()
by_month['lat'].plot()
plt.show()
print(by_month.head())

sns.lmplot(x='Month', y='twp', data=by_month.reset_index())
plt.show()

sns.countplot(x='Month', data=df, hue='Reason')
# to relocate the legend
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad = 0.)
plt.show()

t = df['timeStamp'].iloc[0]
df['Date'] = df['timeStamp'].apply(lambda t: t.date())
print(df.head())

df.groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.show()

df[df['Reason'] == 'Traffic'].groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.title('Traffic')
plt.show()

df[df['Reason'] == 'Fire'].groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.title('Fire')
plt.show()

df[df['Reason'] == 'EMS'].groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.title('EMS')
plt.show()

day_hour = df.groupby(by=['Day of week', 'Hour']).count()['Reason'].unstack()
plt.figure(figsize=(12,6))
sns.heatmap(day_hour, cmap='viridis')
plt.show()

sns.clustermap(day_hour, cmap='viridis')
plt.show()

day_month = df.groupby(by=['Day of week', 'Month']).count()['Reason'].unstack()
print(day_hour.head())
plt.figure(figsize=(12,6))
sns.heatmap(day_month, cmap='viridis')
plt.show()