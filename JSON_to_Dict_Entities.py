import json
from pprint import pprint
from operator import itemgetter
import csv

with open('Entities\\All_Entities.csv','w') as EntityFile:
	writer = csv.writer(EntityFile)
	i=1
#for i in range(123):
	print(i+1)
	data = json.load(open('Entities\\'+str(i+1)+'.json'))

	Entities = []
	EntitiesOnly = []

	pprint(len(data["entities"]))
	for i in range(len(data["entities"])):
		print(i)
		ent = data["entities"][i]["name"]
		sal = data["entities"][i]["salience"]
		Entities.append([ent,sal])
		EntitiesOnly.append(ent)
		
	print(Entities)

	Entities = sorted(Entities, key=itemgetter(1))

	print(Entities)

	EntLen = len(Entities)
	EntitiesTop5 = [Entities[EntLen-1],Entities[EntLen-2],Entities[EntLen-3],Entities[EntLen-4],Entities[EntLen-5]]

	print()
	print(EntitiesTop5)
	writer.writerow(EntitiesOnly)