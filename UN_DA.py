#Konstantin Löser ©
#Windows 7 - 64bit

#Modules
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Functions
from f_CountTweets import CT

#Filepath
FloodPath ='E:/Konstantin/School - Nijmegen/Master Thesis/UN Project/Floodtags/'
HealthPath ='E:/Konstantin/School - Nijmegen/Master Thesis/UN Project/Healthtags/'

#CSV Files
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

#FloodTags Dictionary
FT = [ConcernedCitizen_Flood, ConcernedCitizen_Forecast, ConcernedCitizen_Mixed, ConcernedCitizen_Postflood,
      EyeWitness_Flood, EyeWitness_Forecast, EyeWitness_Mixed, EyeWitness_Postflood, Flood_Mixed, 
      Flood_News, Flood_NGO, Forecast_Mixed, Forecast_News, Forecast_NGO, Flood_Mixed_Mixed, 
      Flood_Mixed_News, Flood_Mixed_NGO, Flood_Mixed_Postflood, News_Postflood, NGO_Postflood]

#HealthTags Dictionary
HT = [Dengue_Mixed, Dengue_Organisation, Dengue_Other, Dengue_Self, Maybe_Dengue_Mixed, 
      Maybe_Dengue_Organisation, Maybe_Dengue_Other, Maybe_Dengue_Self, Health_Mixed_Mixed, 
      Health_Mixed_Organisation, Health_Mixed_Other, Health_Mixed_Self, Health_Mixed_Stomach,
      Organisation_Stomach, Other_Stomach, Self_Stomach]
      
#Locations Dictionary
LC = ['Bekasi', 'Bandung', 'Bogor', 'Subang', 'Indramayu', 'Karawang', 'Cirebon', 'Sukabumi', 'Kuningan', 'Depok',
      'Cianjur', 'Tangerang', 'Serang', 'Garut', 'Lebak', 'Banjar', 'Jakarta Timur', 'Kota Tangerang',
      'Kota Bekasi', 'Purwakarta', 'Jakarta Utara', 'Cimahi', 'Jakarta Pusat', 'Jakarta Selatan', 'Jakarta Barat',
      'Majalengka', 'Cilegon', 'Pandeglang', 'Kota Bogor', 'Sumedang', 'Ciamis', 'Kota Bandung', 'Tasikmalaya',
      'Kota Sukabumi', 'Kota Cirebon', 'Kota Tasikmalaya']

#Count Tweets
CT(FT,HT)

#Count Tweets according to location
FT_Bekasi = []
i = 0

for x in range(0, len(FT)):
    ftb = FT[x].loc[[i]]
    test = (ftb.drop('Locations', axis=1).sum()).sum(axis=0)
    FT_Bekasi.append(test)
    #for j in range(0, 35):       
    #    i = j+1
        
        
#print(FT_Bekasi)
