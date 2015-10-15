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
