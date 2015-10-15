#Function Flood vs Health Tweets #FT-FT[2]-FT[6] #resample
def htPLTr(FT, HT, Location_Name, resample_format, debug=False):
    Flood1 = pd.Series((sum(FT)-FT[2]-FT[6])).reset_index()
    Disease1 = pd.Series(sum(HT)).reset_index()
    Flood1.columns = ['Dates','Flood Tweets']
    Disease1.columns = ['Dates','Health Tweets']
        
    PLOT1 = pd.merge(Flood1, Disease1, on='Dates', how='outer')
    PLOT1.index = pd.to_datetime(PLOT1['Dates'], format="%d-%m-%Y")
    PLOT1 = PLOT1.resample(resample_format,how='sum')
    PLOT1.index = PLOT1.index.to_pydatetime()
          
    g1 = PLOT1.plot(figsize=(16,8), x=PLOT1.index, y='Flood Tweets', title=Location_Name, color='b')
    g1.set_xlabel('Time in '+resample_format)
    y2 = PLOT1['Health Tweets'].plot(secondary_y=True)
    g1.right_ax.set_ylabel('Health Tweets')
    maxf = max(np.nanmax(PLOT1['Flood Tweets']))
    maxh = max(np.nanmax(PLOT1['Health Tweets']))
    factor = 10
    g1.set_ylim(0,maxf+(np.mean(maxf)/factor))
    g1.right_ax.set_ylim(0, maxh+(np.mean(maxh)/factor))
    g1.set_ylabel('Flood Tweets')
    lines = g1.get_lines() + g1.right_ax.get_lines()
    g1.legend(lines, [l.get_label() for l in lines], loc='upper left')
    
    fig = g1.get_figure()
    ln = Location_Name
    fig.savefig('E:/Konstantin/School - Nijmegen/Master Thesis/Plots/'+ln+'.png',bbox_inches='tight')
    
#PLOT
###Plot all graphs! Flood vs Health (Tweets only) in a loop running this will create 36 graphs for each location
#for x in range(0, len(FTL)):
#    htPLTr(FTL[x],HTL[x],LC[x],'W')
