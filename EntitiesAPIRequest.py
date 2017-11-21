import requests
import csv

def Entities(lyrics):
	url = "https://language.googleapis.com/v1/documents:analyzeEntities"

	querystring = {"key":"AIzaSyCth5e5_lpqluLdYI0YEiQAfqwPDjsiST0"}

	content = lyrics

	#payload = "{\r\n  \"encodingType\": \"UTF8\",\r\n  \"document\": {\r\n    \"type\": \"PLAIN_TEXT\",\r\n    \"content\": \"Please allow me to introduce myself\r\nI'm a man of wealth and taste\r\nBeen around for a long, long year\r\nStole many a man's soul to waste\r\nI was 'round when Jesus Christ\r\nHad his moment of doubt and pain\r\nMade damn sure that Pilate\r\nWashed his hands and sealed his fate\r\nPleased to meet you\r\nHope you guess my name\r\n'Cause what's confusing you is just the\r\nNature of my game\r\nI stuck around St. Petersburg\r\nWhen I saw it was a time for a change\r\nI killed the Tsar and his ministers\r\nAnastasia screamed in vain\r\nI rode a tank, held a general's rank\r\nWhen the blitzkrieg raged and the bodies stank\r\nPleased to meet you\r\nHope you guess my name\r\n'Cause what's puzzling you is just the\r\nNature of my game\r\nCome on, come on, come on!\r\nPleased to meet you\r\nHope you guessed my name, ah yeah\r\n'Cause what's confusing you is just the\r\nNature of my game\r\nI watched with glee while your kings and queens\r\nFought for ten decades, for the gods they made\r\nI shouted out 'who killed the Kennedys?'\r\nWhen after all\r\nIt was you and me\r\nLet me please introduce myself\r\nI'm a man of wealth and taste\r\nI laid traps for troubadours\r\nWho get killed before they reached Bombay\r\nPleased to meet you\r\nHope you guessed my name, oh yeah\r\nBut what's confusing you is just the\r\nNature of my game\r\nJust as every cop is a criminal\r\nAnd all the sinners saints\r\nAs heads is tails, just call me Lucifer\r\n'Cause I'm in need of some restraint\r\nSo if you meet me\r\nHave some courtesy\r\nHave some sympathy, and some taste\r\nUse all your well-learned politesse\r\nOr I'll lay your soul to waste, oh yeah\r\nPleased to meet you\r\nHope you guessed my name, ah yeah\r\nBut what's puzzling you is just the\r\nNature of my game, ah yeah, get down!\r\nWhat's my name?\r\nWhat's my name?\r\nLucifer\r\nThat's my name baby\r\nAah, yeah!\r\nAah, yeah!\r\nAah, come on\"\r\n  }\r\n}"
	payload = "{\r\n  \"encodingType\": \"UTF8\",\r\n  \"document\": {\r\n    \"type\": \"PLAIN_TEXT\",\r\n    \"content\": \""+content+"\"\r\n  }\r\n}"

	headers = {
    	'cache-control': "no-cache",
    	'postman-token': "e897b429-16ce-7d86-dbf1-cf9c73bba5c3"
    	}

	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

	return response.text


def Sentiment(lyrics):
	url = "https://language.googleapis.com/v1/documents:analyzeSentiment"

	querystring = {"key":"AIzaSyCth5e5_lpqluLdYI0YEiQAfqwPDjsiST0"}

	content = lyrics

	payload = "{\r\n  \"encodingType\": \"UTF8\",\r\n  \"document\": {\r\n    \"type\": \"PLAIN_TEXT\",\r\n    \"content\": \""+content+"\"\r\n  }\r\n}"

	headers = {
    	'cache-control': "no-cache",
    	'postman-token': "e897b429-16ce-7d86-dbf1-cf9c73bba5c3"
    	}

	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

	return response.text


#print(Sentiment("BAZINGA"))

# Go through the CSV and get the Entities of each song through the Google Natural Language API

with open('songlyrics_old.csv', newline='') as lyricsfile:
    reader = csv.reader(lyricsfile)
    reader
    for row in reader:
       	print(row[0])
        with open("Entities\\"+row[0]+".json",'w') as lyricstxt:
        	lyricstxt.write(Entities(row[4]))
        		

# Go through the CSV and get the Sentiment of each song through the Google Natural Language API

with open('songlyrics_old.csv', newline='') as lyricsfile:
    reader = csv.reader(lyricsfile)
    reader
    for row in reader:
       	print(row[0])
        with open("Sentiment\\"+row[0]+".json",'w') as lyricstxt:
        	lyricstxt.write(Sentiment(row[4]))