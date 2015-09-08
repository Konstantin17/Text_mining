#Loading modules and functions
import json
import pandas as pd

#Filepath
FP = "H:/Master Thesis/json/100.json"

#Database
data = [] #dict

#Append .json file
with open(FP) as data_file:    
    for line in data_file:    
        data.append(json.loads(line, encoding="ISO-8859-1")) #Encode to read all characters

#Tweet messages
header = data[0].keys()

tweet_db = []
for i in range(0, len(data)):
    tweet = data[i].values()[2].encode("ISO-8859-1") #Encode to convert unicode to str
    tweet_db.append(tweet)

#Split tweet_db sentences into words
from nltk.tokenize import word_tokenize
tweet_token = [word_tokenize(i) for i in tweet_db]

tweet_list = reduce(lambda x, y: x+y, tweet_token)

tweets = pd.DataFrame(data = tweet_list)
print(tweets)

#for i in tweet_list:
#    print i 
    


#print(type(tweet_db[0]))
#print(tweet_db)
    
#from collections import Counter
#wordcount = Counter(tweet_db)
#print(wordcount)
