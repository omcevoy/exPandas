import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd

url = "https://fbref.com/en/comps/22/2798/2019-Major-League-Soccer-Stats"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

tables = soup.find_all('tbody')
ecf = tables[0]
wcf = tables[2]

ecfRows = ecf.find_all('tr')
wcfRows = wcf.find_all('tr')

leagueStats = {}

def dataRetriever(data):
	startIndex = data.index('>')
	endIndex = data.index('</td')
	finalCut = data[startIndex + 1 : endIndex].replace(",", "")
	return int(finalCut)

def getClub(data):
	startIndex = data.index("<a")
	endIndex = data.index("</a")
	cutString = data[startIndex:endIndex]
	finalCut = cutString.index(">")
	return cutString[finalCut + 1:]


for row in ecfRows:
	data = row.find_all('td')
	club = str(data[0])
	clubData = data[1:]
	teamStats = {"Wins" : dataRetriever(str(clubData[1])),
				"Draws" : dataRetriever(str(clubData[2])),
				"Losses" : dataRetriever(str(clubData[3])),
				"GF" : dataRetriever(str(clubData[4])),
				"GA" : dataRetriever(str(clubData[5])),
				"Attendance" : dataRetriever(str(clubData[12]))}
	leagueStats[getClub(club)] = teamStats

for row in wcfRows:
	data = row.find_all('td')
	club = str(data[0])
	clubData = data[1:]
	teamStats = {"Wins" : dataRetriever(str(clubData[1])),
				"Draws" : dataRetriever(str(clubData[2])),
				"Losses" : dataRetriever(str(clubData[3])),
				"GF" : dataRetriever(str(clubData[4])),
				"GA" : dataRetriever(str(clubData[5])),
				"Attendance" : dataRetriever(str(clubData[12]))}
	leagueStats[getClub(club)] = teamStats

stats = pd.DataFrame(leagueStats).swapaxes('index', 'columns')
stats.reset_index(level = 0, inplace = True)
stats.rename(columns = {'index' : 'club'}, inplace = True)
stats['club'] = stats['club'].replace(["Los Angeles FC", "Philadelphia", "Seattle", "Colorado", "Columbus", "D.C. United", "FC Dallas", "Orlando City", "Atlanta", "FC Cincinnati", "Vancouver", "San Jose", "New England", "Toronto FC", "LA Galaxy", "Real Salt Lake", "Minnesota", "NYCFC", "Portland", "Chicago", "Sporting KC", "NY Red Bulls", "Montreal", "Houston"],
											  ["LAFC", "PHI", "SEA", "COL", "CLB", "DC", "DAL", "ORL", "ATL", "CIN", "VAN", "SJ", "NE", "TFC", "LA", "RSL", "MIN", "NYFC", "POR", "CHI", "KC", "NY", "MON", "HOU"])