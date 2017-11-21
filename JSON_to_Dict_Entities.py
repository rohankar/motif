import json
from pprint import pprint
from operator import itemgetter
import csv

writer = open('Entities\\All_Entities.txt','w')
#writer = csv.writer(EntityFile)
#i=1
for i in range(123):
	print(i+1)
	data = json.load(open('Entities\\'+str(i+1)+'.json'))

	Entities = []
	#EntitiesOnly = []
	EntitiesOnly = ''

	pprint(len(data["entities"]))
	for j in range(len(data["entities"])):
		print(j)
		ent = data["entities"][j]["name"]
		sal = data["entities"][j]["salience"]
		Entities.append([ent,sal])
		EntitiesOnly = EntitiesOnly+','+ent
		#EntitiesOnly.append(ent)
		
	#print(Entities)

	#Entities = sorted(Entities, key=itemgetter(1))

	#print(Entities)

	#EntLen = len(Entities)
	#EntitiesTop5 = [Entities[EntLen-1],Entities[EntLen-2],Entities[EntLen-3],Entities[EntLen-4],Entities[EntLen-5]]
	print("+++++++")
	print(EntitiesOnly)
	#print(EntitiesTop5)
	writer.write(EntitiesOnly+'\n')