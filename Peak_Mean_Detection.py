#Peak_Mean Detection (Resample possible)
def PeakM(XT, XT_, Location_Name, Debug='False'):
    test = sum(XT).reset_index()
    test.columns = ['Dates','Tweets']
    test.index = pd.to_datetime(test['Dates'], format="%d-%m-%Y")
    del test['Dates']
    test = test.resample('2D',how='sum')
    test['Tweets'] = test['Tweets'].fillna(0)
    
    meanT = np.mean(test['Tweets'])
    
    test.loc[:,'Peak_Value'] = 0
    for x in range(0, len(test['Tweets'])):
        if test['Tweets'][x] > meanT:
            test.loc[:,'Peak_Value'][x] = (test['Tweets'][x]/meanT)
        else:
            test.loc[:,'Peak_Value'][x] = 0 
     
        test.to_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/'+XT_+Location_Name+'_PeakM'+'.csv')
