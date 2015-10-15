###Count Tweets simply counts all tweets that are in these dataframes
def CT(DataFrame_FloodTags, DataFrame_HealthTags, debug=False):

    #Count Tweets
    floodtest = []

    for x in range(0, len(DataFrame_FloodTags)):
        ft = (DataFrame_FloodTags[x].drop('Locations', axis=1).sum()).sum(axis=0)
        print(ft)
        floodtest.append(ft)

    print(" ")
    print("total:")
    print(sum(floodtest))
    print(" ")

    healthtest = []

    for x in range(0, len(DataFrame_HealthTags)):
        ht = (DataFrame_HealthTags[x].drop('Locations', axis=1).sum()).sum(axis=0)
        print(ht)
        healthtest.append(ht)

    print(" ")
    print("total:")
    print(sum(healthtest))
    
    #CT(FT,HT)
#Flood Tweet Count Bar
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)

ind = np.arange(len(CFT['Class']))
width = 1
ax.bar(ind, CFT['Flood_Tweet'], width, align='center')

ax.set_xlim(-width,len(ind))
ax.set_ylim(0,310000)
ax.set_ylabel('Tweets')
ax.set_title('Flood Tweet Count')
xTickMarks = [CFT['Class'][x] for x in range(len(CFT['Class']))]
ax.set_xticks(ind)
xTickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xTickNames, rotation=90, fontsize=12)

#Health Tweet Count Bar
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)

ind = np.arange(len(CHT['Class']))
ax.bar(ind, CHT['Health_Tweet'], width, align='center',color='r')

ax.set_xlim(-width,len(ind))
ax.set_ylim(0,60000)
ax.set_ylabel('Tweets')
ax.set_title('Health Tweet Count')
xTickMarks1 = [CHT['Class'][x] for x in range(len(CHT['Class']))]
ax.set_xticks(ind)
xTickNames1 = ax.set_xticklabels(xTickMarks1)
plt.setp(xTickNames1, rotation=90, fontsize=12)

###Count Tweets according to location
#Function to seperate locations
def LD(Dictionary_Name, DataFrame, Location_Number, debug=False):

    for x in range(0, len(DataFrame)):
        dummy = DataFrame[x].loc[[Location_Number]].drop('Locations', axis=1).sum()
        Dictionary_Name.append(dummy)
        
        #.loc selects a specific row
        #.drop drops the column locations (since there is no need for it anymore, the dataframe itself gives the information)
        #append everything to the new dictionaries/dataframes
