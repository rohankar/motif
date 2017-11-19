import json
from pprint import pprint
from operator import itemgetter

data = json.load(open('Sentiment\\1.json'))

#Entities = []

#pprint(len(data["entities"]))
#for i in range(len(data["entities"])):
#	print(i)
#	ent = data["entities"][i]["name"]
#	sal = data["entities"][i]["salience"]
#	Entities.append([ent,sal])

print(data["documentSentiment"]["magnitude"])
print(data["documentSentiment"]["score"])

#Entities = sorted(Entities, key=itemgetter(1))

#print(Entities)

#EntLen = len(Entities)
#EntitiesTop5 = [Entities[EntLen-1],Entities[EntLen-2],Entities[EntLen-3],Entities[EntLen-4],Entities[EntLen-5]]

#print()
#print(EntitiesTop5)