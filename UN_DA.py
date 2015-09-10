#Konstantin Löser ©
#Windows 7 - 64bit

#Modules
import pandas as pd
import ast
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Functions
from f_CountTweets import CT
from f_LocationDictionary import LD

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

#FloodTags Dictionary #20
FT = [ConcernedCitizen_Flood, ConcernedCitizen_Forecast, ConcernedCitizen_Mixed, ConcernedCitizen_Postflood,
      EyeWitness_Flood, EyeWitness_Forecast, EyeWitness_Mixed, EyeWitness_Postflood, Flood_Mixed, 
      Flood_News, Flood_NGO, Forecast_Mixed, Forecast_News, Forecast_NGO, Flood_Mixed_Mixed, 
      Flood_Mixed_News, Flood_Mixed_NGO, Flood_Mixed_Postflood, News_Postflood, NGO_Postflood]

#HealthTags Dictionary #16
HT = [Dengue_Mixed, Dengue_Organisation, Dengue_Other, Dengue_Self, Maybe_Dengue_Mixed, 
      Maybe_Dengue_Organisation, Maybe_Dengue_Other, Maybe_Dengue_Self, Health_Mixed_Mixed, 
      Health_Mixed_Organisation, Health_Mixed_Other, Health_Mixed_Self, Health_Mixed_Stomach,
      Organisation_Stomach, Other_Stomach, Self_Stomach]
      
#Locations Dictionary #36
LC = ['Bekasi', 'Bandung', 'Bogor', 'Subang', 'Indramayu', 'Karawang', 'Cirebon', 'Sukabumi', 'Kuningan', 'Depok',
      'Cianjur', 'Tangerang', 'Serang', 'Garut', 'Lebak', 'Banjar', 'Jakarta_Timur', 'Kota_Tangerang',
      'Kota_Bekasi', 'Purwakarta', 'Jakarta_Utara', 'Cimahi', 'Jakarta_Pusat', 'Jakarta_Selatan', 'Jakarta_Barat',
      'Majalengka', 'Cilegon', 'Pandeglang', 'Kota_Bogor', 'Sumedang', 'Ciamis', 'Kota_Bandung', 'Tasikmalaya',
      'Kota_Sukabumi', 'Kota_Cirebon', 'Kota_Tasikmalaya']

FT_LC = []
for x in range(0, len(LC)):
    FTLC = ('FT_'+LC[x])
    FT_LC.append(FTLC)

HT_LC = []
for x in range(0, len(LC)):
    HTLC = ('HT_'+LC[x])
    HT_LC.append(HTLC)

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

#Count Tweets
#CT(FT,HT)

#Count Tweets according to location


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

#Plot
plt.figure(figsize=(15, 8))
#plt.axhline(FT_Bekasi[0], color='b', linestyle='dashed',linewidth=2)
#plt.axhline(HT_Bekasi[0], color='g', linestyle='dashed',linewidth=2)
#plt.plot(FT_Bekasi[0])
plt.plot(FT_Bekasi[14])
plt.plot(HT_Bekasi[9])
