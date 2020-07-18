# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total': 'Total_Medals'}, inplace=True)

print(data.head(10))


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 

better_event = data['Better_Event'].value_counts().index.values[0]

print('Better_Event= ',better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries = top_countries.iloc[:-1,:]

def top_ten(top_countries, col):
    country_list = top_countries.nlargest(n=10, columns=col)['Country_Name'].tolist()
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
    
common = list(set.intersection(*map(set, [top_10, top_10_summer, top_10_winter])))
print(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1,figsize=(5,15), sharex=True)

ax_1.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
ax_1.set_title('Total Summer Medals', fontweight='semibold')
ax_2.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
ax_2.set_title('Total Winter Medals', fontweight='semibold')
ax_3.bar(top_df['Country_Name'], top_df['Total_Medals'])
ax_3.set_title('Total Medals', fontweight='semibold')

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = round(summer_df['Golden_Ratio'].max(), 2)
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = round(winter_df['Golden_Ratio'].max(), 2)
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']



# --------------
#Code starts here
data_1 = data.iloc[:-1,:]



data_1['Total_Points'] = data_1['Gold_Total'].mul(3).add(data_1['Silver_Total'].mul(2)).add(data_1['Bronze_Total'])

most_points = data_1['Total_Points'].max()
best_country= data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind='bar', stacked=True);
plt.xlabel('United States')
plt.ylabel('Medals')
plt.xticks(rotation=45)
plt.show()


