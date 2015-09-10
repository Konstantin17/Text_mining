def LD(Dictionary_Name, DataFrame, Location_Number, debug=False):

    for x in range(0, len(DataFrame)):
        dummy = DataFrame[x].loc[[Location_Number]].drop('Locations', axis=1).sum()
        Dictionary_Name.append(dummy)
