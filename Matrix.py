#This is PM:
FT_Peak_Matrix = []
HT_Peak_Matrix = []
#Peak_Average_StandardDev Detection (Resample possible)
def Peak(XT, XT_, Resample_Value, Location_Name, DF_Matrix, Debug='False'):
    test = sum(XT).reset_index()
    test.columns = ['Dates',Location_Name+'_Tweets']
    test.index = pd.to_datetime(test['Dates'], format="%d-%m-%Y")
    del test['Dates']
    test = test.resample(Resample_Value,how='sum')
    test[Location_Name+'_Tweets'] = test[Location_Name+'_Tweets'].fillna(0)

    meanT = np.mean(test[Location_Name+'_Tweets'])
    stdT = np.std(test[Location_Name+'_Tweets'])
    peak = stdT + (2*meanT)

    test.loc[:,Location_Name+'_Peak'] = 0
    for x in range(0, len(test[Location_Name+'_Tweets'])):
        if test[Location_Name+'_Tweets'][x] < peak:
            test.loc[:,Location_Name+'_Peak'][x] = 0
        else:
            test.loc[:,Location_Name+'_Peak'][x] = 1
    
    DF_Matrix.append(test)
    
    #test.to_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/'+XT_+File_Name+'_Peak'+'_'+Resample_Value+'.csv')

for x in range(0, len(LC)):
    Peak(FTL[x],'FT_','2D',LC[x], FT_Peak_Matrix)
    
for x in range(0, len(LC)):
    Peak(HTL[x],'HT_','2D',LC[x], HT_Peak_Matrix)
    
#Simalarity_Calculation (OR/AND) XTM:
FT_Matrix = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Matrix/FT_Matrix.csv')
HT_Matrix = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Matrix/HT_Matrix.csv')
Old_HT_Matrix = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Matrix/Old_HT_Matrix.csv')

def SC(PM, XTM): #PM=FT_Peak_Matrix XTM=FT_Matrix
    temp_calc = []
    i=0
    for i in range(0, len(LC)):
        print(i)
        for y in range(0, len(LC)):
            temp_calc = pd.merge(PM[i],PM[y], right_index=True, left_index=True)
            temp_calc.loc[:,'OR'] = 0
            temp_calc.loc[:,'AND'] = 0
                    
            for x in range(0, len(temp_calc['OR'])):
                if temp_calc.iloc[x][1] == 0 and temp_calc.iloc[x][3] == 0:
                    temp_calc.loc[:,'OR'][x] = 0
                else:
                    temp_calc.loc[:,'OR'][x] = 1
            
                if temp_calc.iloc[x][1] == 1 and temp_calc.iloc[x][3] == 1:
                    temp_calc.loc[:,'AND'][x] = 1
                else:
                    temp_calc.loc[:,'AND'][x] = 0
                
            temp_AND = sum(temp_calc['AND']) * 1.0
            temp_OR = sum(temp_calc['OR']) * 1.0
            temp_sim = temp_AND/temp_OR*100            
            XTM.set_value(i,LC[y],temp_sim)
            
        i = i+1   
