import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv(r'C:\Users\Yogesh\Desktop\covid\country_wise_latest.csv')

# top 10 rows
# print(df.head())

# data information
# print(df.info())

# countrywise top 10 largest confirmed case
# ndf = df.groupby('Country/Region')['Confirmed','Country/Region','Deaths','Recovered','Active'].sum().sort_values('Active',ascending=False).head(10)
# ndf.reset_index(inplace=True)
# plt.plot(ndf['Country/Region'],ndf['Confirmed'],color='orange',marker='o',label='Confirmed')
# plt.plot(ndf['Country/Region'],ndf['Deaths'],color='black',marker='o',label='Deaths')
# plt.plot(ndf['Country/Region'],ndf['Recovered'],color='green',marker='o',label='Recovery')
# plt.plot(ndf['Country/Region'],ndf['Active'],color='blue',marker='o',label='Active')
# plt.title('Country wise top 10 largest covid confirmed,deaths,recovery,Active case')
# plt.xlabel('Country')
# plt.ylabel('Count')
# plt.legend()
# plt.grid()
# plt.show()


# countrywise top 10 lowset confirmed case
# ndf = df.groupby('Country/Region')['Confirmed','Country/Region','Deaths','Recovered','Active'].sum().sort_values('Confirmed',ascending=True).head(10)
# ndf.reset_index(inplace=True)
# plt.plot(ndf['Country/Region'],ndf['Confirmed'],color='orange',marker='o',label='Confirmed')
# plt.plot(ndf['Country/Region'],ndf['Deaths'],color='black',marker='o',label='Deaths')
# plt.plot(ndf['Country/Region'],ndf['Recovered'],color='green',marker='o',label='Recovery')
# plt.plot(ndf['Country/Region'],ndf['Active'],color='blue',marker='o',label='Active')
# plt.title('Country wise top 10 lowest covid confirmed,deaths,recovery case,Active')
# plt.xlabel('Country')
# plt.ylabel('Count')
# plt.legend()
# plt.grid()
# plt.show()


# WHO Region wise confirmed,deaths,recovery case,Active

# ndf = df.groupby('WHO Region')['WHO Region','Confirmed','Deaths','Recovered','Active'].sum().sort_values('Confirmed',ascending=False)
# ndf.reset_index(inplace=True)
# plt.plot(ndf['WHO Region'],ndf['Confirmed'],color='orange',marker='o',label='Confirmed')
# plt.plot(ndf['WHO Region'],ndf['Deaths'],color='black',marker='o',label='Deaths')
# plt.plot(ndf['WHO Region'],ndf['Recovered'],color='green',marker='o',label='Recovery')
# plt.plot(ndf['WHO Region'],ndf['Active'],color='blue',marker='o',label='Active')
# plt.title('WHO Region covid confirmed,deaths,recovery case,Active')
# plt.xlabel('Country')
# plt.ylabel('Count')
# plt.legend()
# plt.grid()
# plt.show()


# case increment in a weak
# ndf1 = df[['1 week change','Country/Region']].sort_values('1 week change',ascending=False).head(10)
# plt.plot(ndf1['Country/Region'],ndf1['1 week change'],color='orange',marker='o')
# plt.title('case increment in a weak')
# plt.xlabel('Country')
# plt.ylabel('cases')
# plt.grid()
# plt.show

# ndf1 = df[['Confirmed last week','Country/Region']].sort_values('Confirmed last week',ascending=False).head(10)
# plt.plot(ndf1['Country/Region'],ndf1['Confirmed last week'],color='orange',marker='o')
# plt.title('confirmed case in a weak')
# plt.xlabel('Country')
# plt.ylabel('cases')
# plt.grid()
# plt.show()

# weekly increment casese in %

# ndf = df[['1 week % increase','Country/Region']].sort_values('1 week % increase',ascending=False).head(10)
# plt.bar(ndf['Country/Region'],ndf['1 week % increase'])
# plt.grid()
# plt.title('% case increase in a weak')
# plt.xlabel('Country')
# plt.ylabel('% cases')
# plt.show()

# day wise new cases,deaths,recovery

# ndf = df[['Country/Region','New cases','New deaths', 'New recovered']].sort_values('New cases',ascending=False).head(10)
# plt.plot(ndf['Country/Region'],ndf['New cases'],marker='*',label='New Cases')
# plt.plot(ndf['Country/Region'],ndf['New deaths'],marker='*',label='New deaths')
# plt.plot(ndf['Country/Region'],ndf['New recovered'],marker='*',label='New recovery')
# plt.legend()
# plt.grid()
# plt.title('day wise new cases,deaths,recovery')
# plt.xlabel('Country')
# plt.ylabel('cases')
# plt.show()



# df['death per 100 cases'] = df['Deaths / 100 Cases'] * 100
# df['recovery per 100 cases'] = df['Recovered / 100 Cases'] * 100
# ndf = df[['Country/Region','death per 100 cases','recovery per 100 cases']].sort_values('death per 100 cases',ascending=False).head(10)
#
# plt.plot(ndf['Country/Region'],ndf['death per 100 cases'],marker='o',linestyle='--',label='Deaths/100 cases')
# plt.plot(ndf['Country/Region'],ndf['recovery per 100 cases'],marker='o',linestyle='--',label='Recovery/100 cases')
# plt.legend()
# plt.grid()
# plt.title('top 10 country death per 100 cases')
# plt.xlabel('Country/Region')
# plt.ylabel('death/recovery per 100 cases')
# plt.show()



# df['Deaths / 100 Recovered'] = df['Deaths / 100 Recovered'].fillna(0)
# df['Deaths / 100 Recovered'] = df['Deaths / 100 Recovered'].replace(np.inf , np.nan)
# # print(df['Deaths / 100 Recovered'].sort_values(ascending=False).head(10))
# df['deaths / 100 recovery'] = df['Deaths / 100 Recovered'] * 100

# ndf = df[['Country/Region','deaths / 100 recovery']].sort_values('deaths / 100 recovery',ascending=False).head(10)
# ndf.reset_index(drop=True,inplace=True)
# plt.plot(ndf['Country/Region'],ndf['deaths / 100 recovery'],marker='o')
# plt.grid()
# plt.title('top 10 country death per 100 recovery')
# plt.xlabel('Country/Region')
# plt.ylabel('death/100 recovery')
# plt.show()
