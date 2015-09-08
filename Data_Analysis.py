#Modules
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Filepath
path ='E:/Konstantin/School - Nijmegen/Master Thesis/Healthtags2015/'

#CSV Files (Total: 66161 Tweets)
#Important 
mDSel = pd.read_csv(path + "mDengueSelf.csv") #2284
MSel = pd.read_csv(path + "MixedSelf.csv") #5024
MMix = pd.read_csv(path + "MixedMixed.csv") #6633
MOrg = pd.read_csv(path + "MixedOrganisation.csv") #48646

#Rest
DSel = pd.read_csv(path + "DengueSelf.csv")
DMix = pd.read_csv(path + "DengueMixed.csv")
DOrg = pd.read_csv(path + "DengueOrganisation.csv")
DOth = pd.read_csv(path + "DengueOther.csv")
mDMix = pd.read_csv(path + "mDengueMixed.csv")
mDOrg = pd.read_csv(path + "mDengueOrganisation.csv")
mDOth = pd.read_csv(path + "mDengueOther.csv")
Moth = pd.read_csv(path + "MixedOther.csv")
MSto = pd.read_csv(path + "MixedStomach.csv")
OSto = pd.read_csv(path + "OrganisationStomach.csv")
OTsto = pd.read_csv(path + "OtherStomach.csv")
SSto = pd.read_csv(path + "SelfStomach.csv")

#Clean & combine files

D1 = mDSel.drop('Locations', axis=1).sum()
D2 = MSel.drop('Locations', axis=1).sum()
D3 = MMix.drop('Locations', axis=1).sum()
D4 = MOrg.drop('Locations', axis=1).sum()

Data = D1+D2+D3+D4
mData = Data.mean()
sData = Data.std()
print(mData)
print(sData)
usData = mData + (sData * 1)
lsData = mData - (sData * 1)

#Plot
plt.figure(figsize=(20, 10))

plt.axhline(Data.mean(), color='b', linestyle='dashed',linewidth=2)
plt.axhline(usData, color='g', linestyle='dashed',linewidth=2)
plt.axhline(lsData, color='g', linestyle='dashed',linewidth=2)
Data.plot()
