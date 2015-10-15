#Creating CSV for both Flood/Health Tweets (FT[2] and FT[6] don't count, because they are bad classified)

def htCSV(FT, HT, Location_Name, resample_format, debug=False):
    Flood1 = pd.Series((sum(FT)-FT[2]-FT[6])).reset_index()
    Disease1 = pd.Series(sum(HT)).reset_index()
    Flood1.columns = ['Dates','Flood Tweets']
    Disease1.columns = ['Dates','Health Tweets']
        
    PLOT1 = pd.merge(Flood1, Disease1, on='Dates', how='outer')
    PLOT1.index = pd.to_datetime(PLOT1['Dates'], format="%d-%m-%Y")
    PLOT1 = PLOT1.resample(resample_format,how='sum')
    PLOT1.index = PLOT1.index.to_pydatetime()
    pd.DataFrame(PLOT1).to_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/float/'+Location_Name+'_'+resample_format+'.csv')

#Runs all at once
for x in range(0, len(FTL)):
   htCSV(FTL[x],HTL[x],LC[x],'W')
