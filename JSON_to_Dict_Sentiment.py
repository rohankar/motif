import json
from pprint import pprint
from operator import itemgetter
import csv

writer = open('Sentiment\\All_Sentiments.txt','w') 
	#with open('Sentiment\\All_Sentiments.csv','w') as SentimentFile:
#writer = csv.writer(SentimentFile)

for i in range(123):
	print(i+1)
	data = json.load(open('Sentiment\\'+str(i+1)+'.json'))
	
	Sentiment = []
	SentimentOnly = []
	
	data = json.load(open('Sentiment\\'+str(i+1)+'.json'))
	
	#Entities = []
	
	#pprint(len(data["entities"]))
	#for i in range(len(data["entities"])):
	#	print(i)
	#	ent = data["entities"][i]["name"]
	#	sal = data["entities"][i]["salience"]
	#	Entities.append([ent,sal])
	
	mag = data["documentSentiment"]["magnitude"]
	score = data["documentSentiment"]["score"]
	print(str(score))
	
	#Entities = sorted(Entities, key=itemgetter(1))
	
	#print(Entities)
	
	#EntLen = len(Entities)
	#EntitiesTop5 = [Entities[EntLen-1],Entities[EntLen-2],Entities[EntLen-3],Entities[EntLen-4],Entities[EntLen-5]]
	
	#print()
	#print(EntitiesTop5)
	
	writer.write(str(score)+'\n')