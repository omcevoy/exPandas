import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scrape import stats

pd.set_option('max_columns', None)

df2009 = pd.read_csv("salary2009.csv")
df2019 = pd.read_csv("salary2019.csv",  encoding='latin-1')

df2019.rename(columns = {"Last Name" : "last_name",
						'Club' : 'club',
						"First Name" : "first_name",
						"Playing Position" : "position",
						"CY Salary (Annual)" : "cy-annual", 
						"CY Guaranteed Comp (Annual)" : "guaranteed"},
			  inplace = True)
removeChars = ["$", ",", " ", ")"]
for char in removeChars:
	df2019["cy-annual"]  = df2019["cy-annual"].str.replace(char, '')
	df2019["guaranteed"] = df2019["guaranteed"].str.replace(char, '')
df2019["cy-annual"] = pd.to_numeric(df2019['cy-annual'], errors = 'coerce')
df2019["guaranteed"] = pd.to_numeric(df2019['guaranteed'], errors = 'coerce')

df2009.rename(columns = {"Last Name" : "last_name",
						 "Club" : "club",
						 "First Name" : "first_name",
						 "Pos" : "position",
						 "Base Salary" : "cy-annual",
						 "Compensation" : "guaranteed"},
			inplace	= True)


# <---------- Extract data for clubs from 2009 ------------>
clubsFrom2009 = pd.DataFrame({'club' : df2009.club.unique()})

netspend = df2009.groupby(['club']).sum()['cy-annual']
clubs2009 = clubsFrom2009.join(netspend, on = 'club', how = 'left')
positions = ['D', 'M', 'F', 'GK', 'D-M', 'F-M']
positionSpend = {}

df2019 = df2019[~df2019['club'].isin(["Inter Miami", "Major League Soccer", "Nashville SC"])]
for club in clubs2009['club']: 
    clubData = df2009[df2009['club'] == club]
    goodToAdd = False
    clubPositions = {}
    for pos in positions:
        positionData = clubData[clubData['position'] == pos]
        positionalSpend = positionData.groupby(['club', 'position']).sum()['cy-annual']
        try:
        	clubPositions[pos] = positionalSpend[0]
        	goodToAdd = True
        except:
        	continue 
    if (goodToAdd):
    	positionSpend[club] = clubPositions


pos = pd.DataFrame(positionSpend).swapaxes('index', 'columns')
pos.reset_index(level = 0, inplace = True)
pos.rename(columns = {'index' : 'club',
					  'M': 'mf-budget',
					  'GK': 'gk-budget'},
		   inplace = True)
pos['def-budget'] = pos['D'] + pos['D-M'].fillna(0)
pos['fwd-budget'] = pos['F'] + pos['F-M'].fillna(0)

pos.drop(columns = ['D', 'F', 'D-M', 'F-M'], inplace = True)
clubs2009 = clubs2009.merge(pos, on = 'club', how = 'left')
clubs2009 = clubs2009[clubs2009['mf-budget'].notna()] #get rid of Pool goalkeepers
clubs2009 = clubs2009[clubs2009['club'] != 'CHV'] #Get rid of Chivas
clubs2009 = clubs2009.sort_values('club')

#<------- Extract data for clubs from 2019 -------->
clubs2019 = pd.DataFrame({'club' : df2019.club.unique()})
netspend2019 = df2019.groupby('club').sum()['cy-annual']
clubs2019 = clubs2019.join(netspend2019, on = 'club', how = 'left')
positions = ['D', 'M', 'F', 'GK', 'D-M', 'M-F']
positionSpend = {}
for club in clubs2019['club']:
	clubData = df2019[df2019['club'] == club]
	goodToAdd = False
	clubPositions = {}
	for pos in positions:
		# print(clubData)
		positionData = clubData[clubData['position'] == pos]
		positionalSpend = positionData.groupby(['club', 'position']).sum()['cy-annual'] #do you need to group by club and position here????
		try:
			clubPositions[pos] = positionalSpend[0]
			goodToAdd = True
		except:
			continue
	if goodToAdd:
		positionSpend[club] = clubPositions
pos = pd.DataFrame(positionSpend).swapaxes('index', 'columns')
pos.reset_index(level = 0, inplace = True)
pos.rename(columns = {'index' : 'club',
					  'M': 'mf-budget',
					  'GK': 'gk-budget'},
		   inplace = True)
pos['def-budget'] = pos['D'] + pos['D-M'].fillna(0) 
pos['fwd-budget'] = pos['F'] + pos['M-F'].fillna(0) #includes any player with 'M' in midfield budget

pos.drop(columns = ['D-M', 'M-F', 'D', 'F'], inplace = True)
clubs2019 = clubs2019.merge(pos, on = 'club', how = 'left')

#notna() to drop Miami and Nashville as they have incomplete data at this time
clubs2019 = clubs2019[clubs2019['mf-budget'].notna()] 

#Replace club names with appropriate acronyms
clubs2019['club'] = clubs2019['club'].replace(["Philadelphia Union", "Seattle Sounders FC", "Colorado Rapids", "Columbus Crew", "DC United", "FC Dallas", "Orlando City SC", "Atlanta United", "FC Cincinnati", "Vancouver Whitecaps", "San Jose Earthquakes", "New England Revolution", "Toronto FC", "LA Galaxy", "Real Salt Lake", "Minnesota United", "New York City FC", "Portland Timbers", "Chicago Fire", "Sporting Kansas City", "New York Red Bulls", "Montreal Impact", "Houston Dynamo", "Major League Soccer"],
											  ["PHI", "SEA", "COL", "CLB", "DC", "DAL", "ORL", "ATL", "CIN", "VAN", "SJ", "NE", "TFC", "LA", "RSL", "MIN", "NYFC", "POR", "CHI", "KC", "NY", "MON", "HOU", "MLS"])

originalTeams = clubs2009.club.unique()
clubs2019['expansion'] = clubs2019['club'].apply(lambda x : False if x in originalTeams else True)
clubs2019 = clubs2019.sort_values('club')

ogTeams = clubs2019[clubs2019['expansion'] == False]

clubs2019['champ'] = clubs2019['club'].apply(lambda x : True if x == 'SEA' else False)
clubs2019 = clubs2019[clubs2019['club'] != 'MLS'] #Get rid of players that don't belong to a particular club

clubs2019 = clubs2019.merge(stats, on = 'club', how = 'left')

# <------- Swarm Plot For each team to show how they pay players -------->

def plotSwarm():
	plt.style.use("dark_background")
	fig, ax = plt.subplots(figsize = (16, 8))
	sns.swarmplot(x = 'club', y = 'cy-annual', data = df2019, hue = 'position')
	plt.axhline(df2019['cy-annual'].median(), color = 'red', linestyle = 'dashed', label = 'League Average')
	plt.xticks(rotation = 90)
	ax.ticklabel_format(style = 'plain', axis = 'y')
	ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
	plt.title('How Different MLS Franchises Pay their Players')
	plt.ylabel('Annual Wage')
	plt.legend()


# <-------- 2019 MLS Player Salary Distribution (Histogram) --------->

def plotHist():
	fig, ax = plt.subplots(figsize = (12,8))
	bins = np.arange(0, 1200000, 100000)
	binLabels = ["0", "$100,000", "$200,000", "$300,000", "$400,000", "$500,000", "$600,000", "$700,000", "$800,000", "$900,000", "$1,000,000", "> $1,000,000"]
	plt.style.use("fivethirtyeight")

	plt.title("MLS Salary Distribution 2009 vs 2019")
	plt.xlabel("Salary Range")
	plt.ylabel("Number of Players")
	plt.hist([np.clip(df2009['cy-annual'], bins[0], bins[-1]),
			  np.clip(df2019['cy-annual'], bins[0], bins[-1])], bins = bins, rwidth = 0.85, label = ['2009', '2019'])
	plt.legend(loc = 'upper right')
	n_labels = len(binLabels)
	plt.xlim([0, 1000000])
	plt.xticks(bins)
	ax.set_xticklabels(binLabels, rotation = 25)
	xticks = ax.xaxis.get_major_ticks()
	xticks[0].label1.set_visible(False)
	fig.tight_layout()


def comparePayroll():
	plt.style.use("fivethirtyeight")
	teams2009 = clubs2009.sort_values('club')
	theOgs = ogTeams.sort_values('club')
	xlabels = ogTeams['club']
	width = 0.35
	fig, ax = plt.subplots(figsize = (12, 8))
	plt.title("Franchise Payrolls 2009 vs 2019")
	x_pos = np.arange(0, len(originalTeams), 1)
	y_ticks = np.arange(0, 23000000, 1000000)
	y_labels = ["$" + str(x / 1000000) for x in y_ticks]
	ax.bar(x_pos, teams2009['cy-annual'], width, color = 'lightcoral', label = '2009')
	ax.bar(x_pos + width, theOgs['cy-annual'], width, color = 'maroon', label = '2019')
	plt.xticks(x_pos, xlabels)
	plt.yticks(y_ticks, y_labels)
	plt.ylabel("Payroll (in Millions)")
	plt.legend()
	plt.xlabel("MLS Franchise")

def payrollByPosition():
	plt.style.use('fivethirtyeight')
	fig, ax = plt.subplots(figsize = (18, 6))
	plt.title("Positional Payroll by Franchise")
	x_pos = np.arange(0, len(clubs2019['club']), 1)
	width = 0.65
	y_ticks = np.arange(0, 23000000, 1000000)
	y_labels = ["$" + str(x / 1000000) for x in y_ticks]
	ax.bar(x_pos, clubs2019['gk-budget'], width, color = 'darkslategray', label = 'Goalkeepers')
	ax.bar(x_pos, clubs2019['def-budget'], width,  bottom = clubs2019['gk-budget'], color = 'lightcoral', label = 'Defenders')
	ax.bar(x_pos, clubs2019['mf-budget'], width,  bottom = clubs2019['def-budget'] + clubs2019['gk-budget'], color = 'seagreen', label = 'Midfielders')
	ax.bar(x_pos, clubs2019['fwd-budget'], width, bottom = clubs2019['def-budget'] + clubs2019['gk-budget'] + clubs2019['mf-budget'], color = 'goldenrod', label = 'Forwards')
	ax.grid(axis = 'x')
	plt.legend()
	plt.xticks(x_pos, clubs2019['club'])
	plt.yticks(y_ticks, y_labels)
	plt.xlabel('MLS Franchise')
	plt.ylabel('Budget (in Millions)')

def makeScatter():
	plt.style.use("fivethirtyeight")
	fig,ax = plt.subplots(figsize = (12, 6))
	sns.scatterplot(data = clubs2019, x = 'fwd-budget', y = 'Wins', size = 'GF')
	plt.xlabel("Money Spent on Attacking Players")
	plt.ylabel("Number of Regular Season Wins")
	plt.ticklabel_format(style = 'plain')
	ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

makeScatter()
plt.show()
