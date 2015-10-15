#Konstantin Löser ©
#Windows 7 - 64bit

###Modules
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot') #premade style for graphs
from itertools import cycle, islice #color cycle for graphs

#Write CSV
def CSV(DataFrame, Name, debug=False):
    pd.DataFrame(DataFrame).to_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/'+Name+'.csv')
    
def SAVEFIG(Name, debug=False):
    plt.savefig('E:/Konstantin/School - Nijmegen/Master Thesis/Plots/'+Name+'.png', bbox_inches='tight', DPI=300)

def SAVEFIGn(Name, debug=False):
    plt.savefig('E:/Konstantin/School - Nijmegen/Master Thesis/Plots/'+Name+'.png', DPI=300)

###Filepath
FloodPath ='E:/Konstantin/School - Nijmegen/Master Thesis/UN Project/Floodtags/'
HealthPath ='E:/Konstantin/School - Nijmegen/Master Thesis/UN Project/Old_Healthtags/'
Field_Data = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/UN Project/Fielddata/Diarrhea2014.csv')
Field_DH = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Field_Diarrhea.csv')
Field_DN = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Field_Dengue.csv')
CFT = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Count_FT.csv')
CHT = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Count_HT.csv')

###CSV Files
#FloodTags:                 Path:                                                           Tweet Count:
ConcernedCitizen_Flood      = pd.read_csv(FloodPath + "concerned_citizen,flood.csv")        #2024
ConcernedCitizen_Forecast   = pd.read_csv(FloodPath + "concerned_citizen,forecast.csv")     #1
ConcernedCitizen_Mixed      = pd.read_csv(FloodPath + "concerned_citizen,mixed.csv")        #36
ConcernedCitizen_Postflood  = pd.read_csv(FloodPath + "concerned_citizen,postflood.csv")    #0
EyeWitness_Flood            = pd.read_csv(FloodPath + "eyewitness,flood.csv")               #1765
EyeWitness_Forecast         = pd.read_csv(FloodPath + "eyewitness,forecast.csv")            #0
EyeWitness_Mixed            = pd.read_csv(FloodPath + "eyewitness,mixed.csv")               #1363
EyeWitness_Postflood        = pd.read_csv(FloodPath + "eyewitness,postflood.csv")           #0
Flood_Mixed                 = pd.read_csv(FloodPath + "flood,mixed.csv")                    #28650
Flood_News                  = pd.read_csv(FloodPath + "flood,news.csv")                     #94873
Flood_NGO                   = pd.read_csv(FloodPath + "flood,ngo.csv")                      #0
Forecast_Mixed              = pd.read_csv(FloodPath + "forecast,mixed.csv")                 #406
Forecast_News               = pd.read_csv(FloodPath + "forecast,news.csv")                  #16172
Forecast_NGO                = pd.read_csv(FloodPath + "forecast,ngo.csv")                   #0
Flood_Mixed_Mixed           = pd.read_csv(FloodPath + "mixed,mixed.csv")                    #304679
Flood_Mixed_News            = pd.read_csv(FloodPath + "mixed,news.csv")                     #172131
Flood_Mixed_NGO             = pd.read_csv(FloodPath + "mixed,ngo.csv")                      #0
Flood_Mixed_Postflood       = pd.read_csv(FloodPath + "mixed,postflood.csv")                #156
News_Postflood              = pd.read_csv(FloodPath + "news,postflood.csv")                 #658
NGO_Postflood               = pd.read_csv(FloodPath + "ngo,postflood.csv")                  #0       +
                                                                                            #---------
                                                                                            #622914

#HealthTags                 Path:                                                           Tweet Count:
Dengue_Mixed                = pd.read_csv(HealthPath + "dengue,mixed.csv")                  #0
Dengue_Organisation         = pd.read_csv(HealthPath + "dengue,organisation.csv")           #0
Dengue_Other                = pd.read_csv(HealthPath + "dengue,other.csv")                  #0
Dengue_Self                 = pd.read_csv(HealthPath + "dengue,self.csv")                   #26
Maybe_Dengue_Mixed          = pd.read_csv(HealthPath + "maybe_dengue,mixed.csv")            #359
Maybe_Dengue_Organisation   = pd.read_csv(HealthPath + "maybe_dengue,organisation.csv")     #2169
Maybe_Dengue_Other          = pd.read_csv(HealthPath + "maybe_dengue,other.csv")            #2
Maybe_Dengue_Self           = pd.read_csv(HealthPath + "maybe_dengue,self.csv")             #2962
Health_Mixed_Mixed          = pd.read_csv(HealthPath + "mixed,mixed.csv")                   #7846
Health_Mixed_Organisation   = pd.read_csv(HealthPath + "mixed,organisation.csv")            #59290
Health_Mixed_Other          = pd.read_csv(HealthPath + "mixed,other.csv")                   #6
Health_Mixed_Self           = pd.read_csv(HealthPath + "mixed,self.csv")                    #6224
Health_Mixed_Stomach        = pd.read_csv(HealthPath + "mixed,stomach.csv")                 #269
Organisation_Stomach        = pd.read_csv(HealthPath + "organisation,stomach.csv")          #343
Other_Stomach               = pd.read_csv(HealthPath + "other,stomach.csv")                 #4
Self_Stomach                = pd.read_csv(HealthPath + "self,stomach.csv")                  #1032    +
                                                                                            #---------
                                                                                            #80532

###FloodTags Dictionary #20
FT = [ConcernedCitizen_Flood, ConcernedCitizen_Forecast, ConcernedCitizen_Mixed, ConcernedCitizen_Postflood,
      EyeWitness_Flood, EyeWitness_Forecast, EyeWitness_Mixed, EyeWitness_Postflood, Flood_Mixed, 
      Flood_News, Flood_NGO, Forecast_Mixed, Forecast_News, Forecast_NGO, Flood_Mixed_Mixed, 
      Flood_Mixed_News, Flood_Mixed_NGO, Flood_Mixed_Postflood, News_Postflood, NGO_Postflood]

###HealthTags Dictionary #16
HT = [Dengue_Mixed, Dengue_Organisation, Dengue_Other, Dengue_Self, Maybe_Dengue_Mixed, 
      Maybe_Dengue_Organisation, Maybe_Dengue_Other, Maybe_Dengue_Self, Health_Mixed_Mixed, 
      Health_Mixed_Organisation, Health_Mixed_Other, Health_Mixed_Self, Health_Mixed_Stomach,
      Organisation_Stomach, Other_Stomach, Self_Stomach]
      
###Locations Dictionary #36
LC = ['Bekasi', 'Bandung', 'Bogor', 'Subang', 'Indramayu', 'Karawang', 'Cirebon', 'Sukabumi', 'Kuningan', 'Depok',
      'Cianjur', 'Tangerang', 'Serang', 'Garut', 'Lebak', 'Banjar', 'Jakarta_Timur', 'Kota_Tangerang',
      'Kota_Bekasi', 'Purwakarta', 'Jakarta_Utara', 'Cimahi', 'Jakarta_Pusat', 'Jakarta_Selatan', 'Jakarta_Barat',
      'Majalengka', 'Cilegon', 'Pandeglang', 'Kota_Bogor', 'Sumedang', 'Ciamis', 'Kota_Bandung', 'Tasikmalaya',
      'Kota_Sukabumi', 'Kota_Cirebon', 'Kota_Tasikmalaya']

###FT_/HT_+location simply gives FT_ + Bekasi = FT_Bekasi and HT_Bekasi (for later uses)
FT_LC = []
for x in range(0, len(LC)):
     FTLC = ('FT_'+LC[x])
     FT_LC.append(FTLC)
 
HT_LC = []
for x in range(0, len(LC)):
     HTLC = ('HT_'+LC[x])
     HT_LC.append(HTLC)

add_peak = '_Peak'
add_db = ' = []'

for x in range(0, len(FT_LC)):
    te = HT_LC[x]+add_peak+','
    #print(te)

FT_LC_Peak = []
for x in range(0, len(LC)):
     FTLCP = ('FT_'+LC[x]+'_Peak')
     FT_LC_Peak.append(FTLCP)
 
HT_LC_Peak = []
for x in range(0, len(LC)):
     HTLCP = ('HT_'+LC[x]+'_Peak')
     HT_LC_Peak.append(HTLCP)

###Database all locations that are within the floodtweets and healthtweets each is a dataframe try: FT_Bekasi[0]
FT_Bekasi = []
FT_Bandung = []
FT_Bogor = []
FT_Subang = []
FT_Indramayu = []
FT_Karawang = []
FT_Cirebon = []
FT_Sukabumi = []
FT_Kuningan = []
FT_Depok = []
FT_Cianjur = []
FT_Tangerang = []
FT_Serang = []
FT_Garut = []
FT_Lebak = []
FT_Banjar = []
FT_Jakarta_Timur = []
FT_Kota_Tangerang = []
FT_Kota_Bekasi = []
FT_Purwakarta = []
FT_Jakarta_Utara = []
FT_Cimahi = []
FT_Jakarta_Pusat = []
FT_Jakarta_Selatan = []
FT_Jakarta_Barat = []
FT_Majalengka = []
FT_Cilegon = []
FT_Pandeglang = []
FT_Kota_Bogor = []
FT_Sumedang = []
FT_Ciamis = []
FT_Kota_Bandung = []
FT_Tasikmalaya = []
FT_Kota_Sukabumi = []
FT_Kota_Cirebon = []
FT_Kota_Tasikmalaya = []

HT_Bekasi = []
HT_Bandung = []
HT_Bogor = []
HT_Subang = []
HT_Indramayu = []
HT_Karawang = []
HT_Cirebon = []
HT_Sukabumi = []
HT_Kuningan = []
HT_Depok = []
HT_Cianjur = []
HT_Tangerang = []
HT_Serang = []
HT_Garut = []
HT_Lebak = []
HT_Banjar = []
HT_Jakarta_Timur = []
HT_Kota_Tangerang = []
HT_Kota_Bekasi = []
HT_Purwakarta = []
HT_Jakarta_Utara = []
HT_Cimahi = []
HT_Jakarta_Pusat = []
HT_Jakarta_Selatan = []
HT_Jakarta_Barat = []
HT_Majalengka = []
HT_Cilegon = []
HT_Pandeglang = []
HT_Kota_Bogor = []
HT_Sumedang = []
HT_Ciamis = []
HT_Kota_Bandung = []
HT_Tasikmalaya = []
HT_Kota_Sukabumi = []
HT_Kota_Cirebon = []
HT_Kota_Tasikmalaya = []

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
#==============================================================================
# fig = plt.figure(figsize=(16,8))
# ax = fig.add_subplot(111)
# 
# ind = np.arange(len(CFT['Class']))
# width = 1
# ax.bar(ind, CFT['Flood_Tweet'], width, align='center')
# 
# ax.set_xlim(-width,len(ind))
# ax.set_ylim(0,310000)
# ax.set_ylabel('Tweets')
# ax.set_title('Flood Tweet Count')
# xTickMarks = [CFT['Class'][x] for x in range(len(CFT['Class']))]
# ax.set_xticks(ind)
# xTickNames = ax.set_xticklabels(xTickMarks)
# plt.setp(xTickNames, rotation=90, fontsize=12)
#==============================================================================

#Health Tweet Count Bar
#==============================================================================
# fig = plt.figure(figsize=(16,8))
# ax = fig.add_subplot(111)
# 
# ind = np.arange(len(CHT['Class']))
# ax.bar(ind, CHT['Health_Tweet'], width, align='center',color='r')
# 
# ax.set_xlim(-width,len(ind))
# ax.set_ylim(0,60000)
# ax.set_ylabel('Tweets')
# ax.set_title('Health Tweet Count')
# xTickMarks1 = [CHT['Class'][x] for x in range(len(CHT['Class']))]
# ax.set_xticks(ind)
# xTickNames1 = ax.set_xticklabels(xTickMarks1)
# plt.setp(xTickNames1, rotation=90, fontsize=12)
#==============================================================================

###Count Tweets according to location
#Function to seperate locations
def LD(Dictionary_Name, DataFrame, Location_Number, debug=False):

    for x in range(0, len(DataFrame)):
        dummy = DataFrame[x].loc[[Location_Number]].drop('Locations', axis=1).sum()
        Dictionary_Name.append(dummy)
        
        #.loc selects a specific row
        #.drop drops the column locations (since there is no need for it anymore, the dataframe itself gives the information)
        #append everything to the new dictionaries/dataframes

LD(FT_Bekasi,FT,0)
LD(FT_Bandung,FT,1)
LD(FT_Bogor,FT,2)
LD(FT_Subang,FT,3)
LD(FT_Indramayu,FT,4)
LD(FT_Karawang,FT,5)
LD(FT_Cirebon,FT,6)
LD(FT_Sukabumi,FT,7)
LD(FT_Kuningan,FT,8)
LD(FT_Depok,FT,9)
LD(FT_Cianjur,FT,10)
LD(FT_Tangerang,FT,11)
LD(FT_Serang,FT,12)
LD(FT_Garut,FT,13)
LD(FT_Lebak,FT,14)
LD(FT_Banjar,FT,15)
LD(FT_Jakarta_Timur,FT,16)
LD(FT_Kota_Tangerang,FT,17)
LD(FT_Kota_Bekasi,FT,18)
LD(FT_Purwakarta,FT,19)
LD(FT_Jakarta_Utara,FT,20)
LD(FT_Cimahi,FT,21)
LD(FT_Jakarta_Pusat,FT,22)
LD(FT_Jakarta_Selatan,FT,23)
LD(FT_Jakarta_Barat,FT,24)
LD(FT_Majalengka,FT,25)
LD(FT_Cilegon,FT,26)
LD(FT_Pandeglang,FT,27)
LD(FT_Kota_Bogor,FT,28)
LD(FT_Sumedang,FT,29)
LD(FT_Ciamis,FT,30)
LD(FT_Kota_Bandung,FT,31)
LD(FT_Tasikmalaya,FT,32)
LD(FT_Kota_Sukabumi,FT,33)
LD(FT_Kota_Cirebon,FT,34)
LD(FT_Kota_Tasikmalaya,FT,35)

LD(HT_Bekasi,HT,0)
LD(HT_Bandung,HT,1)
LD(HT_Bogor,HT,2)
LD(HT_Subang,HT,3)
LD(HT_Indramayu,HT,4)
LD(HT_Karawang,HT,5)
LD(HT_Cirebon,HT,6)
LD(HT_Sukabumi,HT,7)
LD(HT_Kuningan,HT,8)
LD(HT_Depok,HT,9)
LD(HT_Cianjur,HT,10)
LD(HT_Tangerang,HT,11)
LD(HT_Serang,HT,12)
LD(HT_Garut,HT,13)
LD(HT_Lebak,HT,14)
LD(HT_Banjar,HT,15)
LD(HT_Jakarta_Timur,HT,16)
LD(HT_Kota_Tangerang,HT,17)
LD(HT_Kota_Bekasi,HT,18)
LD(HT_Purwakarta,HT,19)
LD(HT_Jakarta_Utara,HT,20)
LD(HT_Cimahi,HT,21)
LD(HT_Jakarta_Pusat,HT,22)
LD(HT_Jakarta_Selatan,HT,23)
LD(HT_Jakarta_Barat,HT,24)
LD(HT_Majalengka,HT,25)
LD(HT_Cilegon,HT,26)
LD(HT_Pandeglang,HT,27)
LD(HT_Kota_Bogor,HT,28)
LD(HT_Sumedang,HT,29)
LD(HT_Ciamis,HT,30)
LD(HT_Kota_Bandung,HT,31)
LD(HT_Tasikmalaya,HT,32)
LD(HT_Kota_Sukabumi,HT,33)
LD(HT_Kota_Cirebon,HT,34)
LD(HT_Kota_Tasikmalaya,HT,35)

###Create database for all smaller dataframes
FTL = [FT_Bekasi, FT_Bandung, FT_Bogor, FT_Subang, FT_Indramayu, FT_Karawang, FT_Cirebon, FT_Sukabumi, 
       FT_Kuningan, FT_Depok, FT_Cianjur, FT_Tangerang, FT_Serang, FT_Garut, FT_Lebak, FT_Banjar, FT_Jakarta_Timur, 
       FT_Kota_Tangerang, FT_Kota_Bekasi, FT_Purwakarta, FT_Jakarta_Utara, FT_Cimahi, FT_Jakarta_Pusat, 
       FT_Jakarta_Selatan, FT_Jakarta_Barat, FT_Majalengka, FT_Cilegon, FT_Pandeglang, FT_Kota_Bogor, FT_Sumedang, 
       FT_Ciamis, FT_Kota_Bandung, FT_Tasikmalaya, FT_Kota_Sukabumi, FT_Kota_Cirebon, FT_Kota_Tasikmalaya]
       
HTL = [HT_Bekasi, HT_Bandung, HT_Bogor, HT_Subang, HT_Indramayu, HT_Karawang, HT_Cirebon, HT_Sukabumi, HT_Kuningan, 
       HT_Depok, HT_Cianjur, HT_Tangerang, HT_Serang, HT_Garut, HT_Lebak, HT_Banjar, HT_Jakarta_Timur, 
       HT_Kota_Tangerang, HT_Kota_Bekasi, HT_Purwakarta, HT_Jakarta_Utara, HT_Cimahi, HT_Jakarta_Pusat, 
       HT_Jakarta_Selatan, HT_Jakarta_Barat, HT_Majalengka, HT_Cilegon, HT_Pandeglang, HT_Kota_Bogor, 
       HT_Sumedang, HT_Ciamis, HT_Kota_Bandung, HT_Tasikmalaya, HT_Kota_Sukabumi, HT_Kota_Cirebon, HT_Kota_Tasikmalaya]

#Function Healthtweet plot
def htPLT(FT, HT, Location_Name, debug=False):
       
    Flood1 = pd.Series(sum(FT)).reset_index()
    Disease1 = pd.Series(sum(HT)).reset_index()
    Flood1.columns = ['Dates','Flood Tweets']
    Disease1.columns = ['Dates','Health Tweets']
    
    PLOT1 = pd.merge(Flood1, Disease1, on='Dates', how='outer')

    g1 = PLOT1.plot(figsize=(16,8), x='Dates', y='Flood Tweets', title=Location_Name, color='b')
    g1.set_xlabel('Time in Days')
    g1.set_ylabel('Tweets')
    PLOT1['Health Tweets'].plot()
    g1.legend(['Flood Tweets', 'Health Tweets'])
    
    fig = g1.get_figure()
    ln = Location_Name
    fig.savefig('E:/Konstantin/School - Nijmegen/Master Thesis/Plots/'+ln+'.png',bbox_inches='tight')

#Function Flood vs Health Tweets #FT-FT[2]-FT[6]
def htPLTy(FT, HT, Location_Name, debug=False):
    Flood1 = pd.Series((sum(FT)-FT[2]-FT[6])).reset_index()
    Disease1 = pd.Series(sum(HT)).reset_index()
    Flood1.columns = ['Dates','Flood Tweets']
    Disease1.columns = ['Dates','Health Tweets']
        
    PLOT1 = pd.merge(Flood1, Disease1, on='Dates', how='outer')
    
    g1 = PLOT1.plot(figsize=(16,8), x='Dates', y='Flood Tweets', title=Location_Name, color='b')
    g1.set_xlabel('Time in Days')
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
    
    
      
#    g1 = PLOT1.plot(figsize=(16,8), x=PLOT1.index, y='Flood Tweets', title=Location_Name, color='b')
#    g1.set_xlabel('Time in '+resample_format)
#    y2 = PLOT1['Health Tweets'].plot(secondary_y=True)
#    g1.right_ax.set_ylabel('Health Tweets')
#    maxf = max(np.nanmax(PLOT1['Flood Tweets']))
#    maxh = max(np.nanmax(PLOT1['Health Tweets']))
#    factor = 10
#    g1.set_ylim(0,maxf+(np.mean(maxf)/factor))
#    g1.right_ax.set_ylim(0, maxh+(np.mean(maxh)/factor))
#    g1.set_ylabel('Flood Tweets')
#    lines = g1.get_lines() + g1.right_ax.get_lines()
#    g1.legend(lines, [l.get_label() for l in lines], loc='upper left')
#    
#    fig = g1.get_figure()
#    ln = Location_Name
#    fig.savefig('E:/Konstantin/School - Nijmegen/Master Thesis/Plots/'+ln+'.png',bbox_inches='tight')
    
#PLOT
###Plot all graphs! Flood vs Health (Tweets only) in a loop running this will create 36 graphs for each location
#for x in range(0, len(FTL)):
#    htPLTr(FTL[x],HTL[x],LC[x],'W')

CSV_W = []
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

for x in range(0, len(FTL)):
   htCSV(FTL[x],HTL[x],LC[x],'W')



###Plot Flood vs Field data diarrhea (Daily vs Monthly)
#Function Health Field Data plot
def hfPLT(FT, FD, Location_Name, debug=False):

    Flood2 = pd.Series(sum(FT)).reset_index()
    Field = FD.T.reset_index()
    Flood2.columns = ['Dates','Flood Tweets']
    Field.columns = ['Dates','Field Data']
    
    PLOT2 = pd.merge(Flood2, Field, on='Dates', how='outer')

    g1 = PLOT2.plot(figsize=(16,8), x='Dates', y='Flood Tweets', title=Location_Name, color='b')
    g1.set_xlabel('Time in Days')
    g1.set_ylabel('Flood Tweets')
    PLOT2['Field Data'].plot()
    g1.legend(['Flood Tweets', 'Health FD'])
    
    #fig = g1.get_figure()
    #ln = Location_Name
    #fig.savefig('E:/Konstantin/School - Nijmegen/Master Thesis/Plots/'+ln+'.png',bbox_inches='tight')
    
#hfPLT(FT_Bandung, Field_Data, 'Bandung') #This is the plot

Flood = pd.Series(sum(FT_Bandung)).reset_index() #All classes summarized and reset the index try: Flood
Flood.columns = ['Dates','Flood Tweets'] #Give columns to Flood

#==============================================================================
# ###This will slow down python because it will convert the field data to the same format as Flood
# #Therefore this process has been saved as CSV -> Field_Diarrhea.csv (this is loaded in the start of the script)
# Field_DH = Field_Data.T.reset_index()
# Field_DH.columns = ['Dates','Field Data']
# for x in range(0, len(Field_DH['Dates'])):
#     Field_DH['Dates'][x] = Field_DH['Dates'][x].replace('/','-')
#==============================================================================

FT_FD_DH = pd.merge(Flood, Field_DH, on='Dates', how='outer') #Merge Floodtweets with field data diarrhea

###Plot Flood vs Field data (Diarrhea) (Monthly vs Monthly)
MFlood = Flood
MFlood.index = pd.to_datetime(MFlood['Dates'])
del MFlood['Dates']
M1 = MFlood.resample('M',how='sum')

MField = Field_DH
MField.index = pd.to_datetime(MField['Dates'])
del MField['Dates']
M2 = MField.resample('M',how='sum')

FT_FD_DH_Month = pd.concat([M1,M2], axis=1).reset_index()
FT_FD_DH_Month['Dates'] = pd.to_datetime(FT_FD_DH_Month['Dates'])

#PLOT
#==============================================================================
# #Add bar plot
# my_colors = list(islice(cycle(['b', 'r']), None, len(FT_FD_DH_Month)))
# g2 = FT_FD_DH_Month.plot(kind='bar',x='Dates',figsize=(16,8), color=my_colors, title='Bandung', )
# g2.set_xlabel('Time in Months')
# g2.set_ylabel('Tweets')
#==============================================================================

#==============================================================================
# #PLOT
# #Add scatter plot
# plt.figure(figsize=(16,8))
# test = FT_FD_DH_Month[2:12]
# plt.scatter(x=test['Flood Tweets'], y=test['Field Data'])
# plt.ylabel('Field Data (Health)')
# plt.xlabel('Flood Tweets')
# plt.title('Scatter Health vs Flood-Tweets Diarrhea')
# SAVEFIG('Scatter Health vs Flood-Tweets Diarrhea')
#==============================================================================

###Correlation Floodtweet vs Healthtweet per location (not added NaN yet, if we use this do so)
FHS = []
def LD(x,y, debug=False):
    x = pd.Series(sum(x)).reset_index()
    y = pd.Series(sum(y)).reset_index()
    x.columns = ['Dates','Flood Tweets']
    y.columns = ['Dates','Health Tweets']

    x = pd.merge(x, y, on='Dates', how='outer')
    del x['Dates']
    FHS.append(x)
    
#for x in range(0, len(FTL)):
#    LD(FTL[x],HTL[x])

#PLOT
#==============================================================================
# for x in range(0, len(FHS)):
#     ln = LC[x] 
#     PLOT = FHS[x]
#     g1 = PLOT.plot(figsize=(16,8), x='Flood Tweets', y='Health Tweets', title=ln, kind='scatter')
#     g1.set_xlabel('Flood Tweets')
#     g1.set_ylabel('Health Tweets')
#     g1.legend(['Points'])
#     
#     fig = g1.get_figure()
#     fig.savefig('E:/Konstantin/School - Nijmegen/Master Thesis/Plots/'+ln+'.png',bbox_inches='tight')
#==============================================================================

#==============================================================================
# #Correlation Floodtweet vs Healthtweet together
# for x in range(0, len(FHS)):
#     FHS[x] = FHS[x].replace('0', np.nan)
#    
# #PLOT
# plt.figure(figsize=(16,8))
# for x in range(0, len(FHS)):
#     plt.scatter(x=FHS[x]['Flood Tweets'], y=FHS[x]['Health Tweets'])
# plt.ylim(0,300)
# plt.xlim(0,300)
# plt.xlabel('Health Tweets')
# plt.ylabel('Flood Tweets')
# plt.title('Scatter Health vs Flood-Tweets')
#==============================================================================

#Field_DN.columns = ['Dates','Field Data']
#for x in range(0, len(Field_DH['Dates'])):
#     Field_DH['Dates'][x] = Field_DH['Dates'][x].replace('/','-')

#MField_DN = Field_DN
#MField_DN.index = pd.to_datetime(MField_DN['Dates'])
#del MField_DN['Dates']

#FT_FD_DN_Month = pd.concat([M1,MField_DN], axis=1).reset_index()

#==============================================================================
# #PLOT
# plt.figure(figsize=(16,8))
# plt.scatter(x=FT_FD_DN_Month['Flood Tweets'], y=FT_FD_DN_Month['Field Data'])
# plt.ylabel('Field Data (Health)')
# plt.xlabel('Flood Tweets')
# plt.title('Scatter Health vs Flood-Tweets Dengue')
# SAVEFIG('Scatter Health vs Flood-Tweets Dengue')
# 
#==============================================================================

#PLOT
#==============================================================================
##PLot both bar graphs for dengue and diarrhea
# my_colors = list(islice(cycle(['b', 'r']), None, len(FT_FD_DN_Month)))
# g2 = FT_FD_DN_Month.plot(kind='bar',x='Dates',figsize=(16,8), color=my_colors, title='Bandung Dengue', )
# g2.set_xlabel('Time in Months')
# g2.set_ylabel('Tweets')
# g2.set_ylim(0,15000)
# 
# my_colors = list(islice(cycle(['b', 'r']), None, len(FT_FD_DH_Month)))
# g2 = FT_FD_DH_Month.plot(kind='bar',x='Dates',figsize=(16,8), color=my_colors, title='Bandung Diarrhea', )
# g2.set_xlabel('Time in Months')
# g2.set_ylabel('Tweets')
# g2.set_ylim(0,15000)
#==============================================================================

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

#for x in range(0, len(LC)):
#    PeakM(HTL[x],'HT_',LC[x])

#FT_Bekasi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Bekasi_Peak.csv')
#FT_Bandung_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Bandung_Peak.csv')
#FT_Bogor_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Bogor_Peak.csv')
#FT_Subang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Subang_Peak.csv')
#FT_Indramayu_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Indramayu_Peak.csv')
#FT_Karawang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Karawang_Peak.csv')
#FT_Cirebon_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Cirebon_Peak.csv')
#FT_Sukabumi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Sukabumi_Peak.csv')
#FT_Kuningan_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Kuningan_Peak.csv')
#FT_Depok_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Depok_Peak.csv')
#FT_Cianjur_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Cianjur_Peak.csv')
#FT_Tangerang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Tangerang_Peak.csv')
#FT_Serang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Serang_Peak.csv')
#FT_Garut_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Garut_Peak.csv')
#FT_Lebak_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Lebak_Peak.csv')
#FT_Banjar_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Banjar_Peak.csv')
#FT_Jakarta_Timur_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Jakarta_Timur_Peak.csv')
#FT_Kota_Tangerang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Kota_Tangerang_Peak.csv')
#FT_Kota_Bekasi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Kota_Bekasi_Peak.csv')
#FT_Purwakarta_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Purwakarta_Peak.csv')
#FT_Jakarta_Utara_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Jakarta_Utara_Peak.csv')
#FT_Cimahi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Cimahi_Peak.csv')
#FT_Jakarta_Pusat_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Jakarta_Pusat_Peak.csv')
#FT_Jakarta_Selatan_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Jakarta_Selatan_Peak.csv')
#FT_Jakarta_Barat_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Jakarta_Barat_Peak.csv')
#FT_Majalengka_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Majalengka_Peak.csv')
#FT_Cilegon_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Cilegon_Peak.csv')
#FT_Pandeglang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Pandeglang_Peak.csv')
#FT_Kota_Bogor_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Kota_Bogor_Peak.csv')
#FT_Sumedang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Sumedang_Peak.csv')
#FT_Ciamis_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Ciamis_Peak.csv')
#FT_Kota_Bandung_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Kota_Bandung_Peak.csv')
#FT_Tasikmalaya_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Tasikmalaya_Peak.csv')
#FT_Kota_Sukabumi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Kota_Sukabumi_Peak.csv')
#FT_Kota_Cirebon_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Kota_Cirebon_Peak.csv')
#FT_Kota_Tasikmalaya_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/FT_Kota_Tasikmalaya_Peak.csv')

#HT_Bekasi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Bekasi_Peak.csv')
#HT_Bandung_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Bandung_Peak.csv')
#HT_Bogor_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Bogor_Peak.csv')
#HT_Subang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Subang_Peak.csv')
#HT_Indramayu_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Indramayu_Peak.csv')
#HT_Karawang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Karawang_Peak.csv')
#HT_Cirebon_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Cirebon_Peak.csv')
#HT_Sukabumi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Sukabumi_Peak.csv')
#HT_Kuningan_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Kuningan_Peak.csv')
#HT_Depok_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Depok_Peak.csv')
#HT_Cianjur_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Cianjur_Peak.csv')
#HT_Tangerang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Tangerang_Peak.csv')
#HT_Serang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Serang_Peak.csv')
#HT_Garut_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Garut_Peak.csv')
#HT_Lebak_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Lebak_Peak.csv')
#HT_Banjar_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Banjar_Peak.csv')
#HT_Jakarta_Timur_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Jakarta_Timur_Peak.csv')
#HT_Kota_Tangerang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Kota_Tangerang_Peak.csv')
#HT_Kota_Bekasi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Kota_Bekasi_Peak.csv')
#HT_Purwakarta_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Purwakarta_Peak.csv')
#HT_Jakarta_Utara_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Jakarta_Utara_Peak.csv')
#HT_Cimahi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Cimahi_Peak.csv')
#HT_Jakarta_Pusat_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Jakarta_Pusat_Peak.csv')
#HT_Jakarta_Selatan_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Jakarta_Selatan_Peak.csv')
#HT_Jakarta_Barat_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Jakarta_Barat_Peak.csv')
#HT_Majalengka_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Majalengka_Peak.csv')
#HT_Cilegon_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Cilegon_Peak.csv')
#HT_Pandeglang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Pandeglang_Peak.csv')
#HT_Kota_Bogor_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Kota_Bogor_Peak.csv')
#HT_Sumedang_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Sumedang_Peak.csv')
#HT_Ciamis_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Ciamis_Peak.csv')
#HT_Kota_Bandung_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Kota_Bandung_Peak.csv')
#HT_Tasikmalaya_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Tasikmalaya_Peak.csv')
#HT_Kota_Sukabumi_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Kota_Sukabumi_Peak.csv')
#HT_Kota_Cirebon_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Kota_Cirebon_Peak.csv')
#HT_Kota_Tasikmalaya_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/Peak/HT_Kota_Tasikmalaya_Peak.csv')

#==============================================================================
# FT_Peak = [FT_Bekasi_Peak+FT_Bandung_Peak+FT_Bogor_Peak+FT_Subang_Peak+FT_Indramayu_Peak+FT_Karawang_Peak+
# FT_Cirebon_Peak+FT_Sukabumi_Peak+FT_Kuningan_Peak+FT_Depok_Peak+FT_Cianjur_Peak+FT_Tangerang_Peak+FT_Serang_Peak+
# FT_Garut_Peak+FT_Lebak_Peak+FT_Banjar_Peak+FT_Jakarta_Timur_Peak+FT_Kota_Tangerang_Peak+FT_Kota_Bekasi_Peak+
# FT_Purwakarta_Peak+FT_Jakarta_Utara_Peak+FT_Cimahi_Peak+FT_Jakarta_Pusat_Peak+FT_Jakarta_Selatan_Peak+
# FT_Jakarta_Barat_Peak+FT_Majalengka_Peak+FT_Cilegon_Peak+FT_Pandeglang_Peak+FT_Kota_Bogor_Peak+
# FT_Sumedang_Peak+FT_Ciamis_Peak+FT_Kota_Bandung_Peak+FT_Tasikmalaya_Peak+FT_Kota_Sukabumi_Peak+FT_Kota_Cirebon_Peak+
# FT_Kota_Tasikmalaya_Peak]
# 
# FT_Peak = FT_Peak[0]
# FT_Peak['Dates'] = FT_Bekasi_Peak['Dates']
# 
# HT_Peak = [HT_Bekasi_Peak+HT_Bandung_Peak+HT_Bogor_Peak+HT_Subang_Peak+HT_Indramayu_Peak+HT_Karawang_Peak+
# HT_Cirebon_Peak+HT_Sukabumi_Peak+HT_Kuningan_Peak+HT_Depok_Peak+HT_Cianjur_Peak+HT_Tangerang_Peak+HT_Serang_Peak+
# HT_Garut_Peak+HT_Lebak_Peak+HT_Banjar_Peak+HT_Jakarta_Timur_Peak+HT_Kota_Tangerang_Peak+HT_Kota_Bekasi_Peak+
# HT_Purwakarta_Peak+HT_Jakarta_Utara_Peak+HT_Cimahi_Peak+HT_Jakarta_Pusat_Peak+HT_Jakarta_Selatan_Peak+
# HT_Jakarta_Barat_Peak+HT_Majalengka_Peak+HT_Cilegon_Peak+HT_Pandeglang_Peak+HT_Kota_Bogor_Peak+
# HT_Sumedang_Peak+HT_Ciamis_Peak+HT_Kota_Bandung_Peak+HT_Tasikmalaya_Peak+HT_Kota_Sukabumi_Peak+HT_Kota_Cirebon_Peak+
# HT_Kota_Tasikmalaya_Peak]
# 
# HT_Peak = HT_Peak[0]
# HT_Peak['Dates'] = HT_Bekasi_Peak['Dates']
#==============================================================================

FT_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/FT_Peak.csv')
HT_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/HT_Peak.csv')

#Flood Peak Bar
#g1 = FT_Peak.plot(figsize=(16,8), x='Dates', y='Peak', title='Health vs Flood Peaks', color='b')
#g1.set_xlabel('Time in Weeks')
#g1.set_ylabel('Peaks')
#HT_Peak['Peak'].plot()
#g1.legend(['Flood Peak','Health Peak'])
#SAVEFIG('Health vs Flood Peaks')

FTHT_Peak = pd.read_csv('E:/Konstantin/School - Nijmegen/Master Thesis/CSV/FTHT_Peak.csv')

#PLOT
#==============================================================================
# plt.figure(figsize=(16,8))
# plt.scatter(x=FTHT_Peak['FT_Peak'], y=FTHT_Peak['HT_Peak'])
# plt.ylabel('Health Tweet Peaks)')
# plt.xlabel('Flood Tweet Peaks')
# plt.title('Scatter Health vs Flood-Peaks')
# #SAVEFIG('Scatter Health vs Flood-Tweets Diarrhea')
#==============================================================================
