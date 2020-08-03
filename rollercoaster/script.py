import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
pd.set_option('max_columns', None)
plt.style.use("dark_background")

wood  = pd.read_csv("data/Golden_Ticket_Award_Winners_Wood.csv")
steel = pd.read_csv("data/Golden_Ticket_Award_Winners_Steel.csv")

# How many roller coasters are included in each ranking dataset?
# print(wood.shape) --> 180 x 8
# print(steel.shape) --> 180 x 8

# How many different roller coaster suppliers are included in the rankings?
# print(wood["Supplier"].nunique()) --> 32
# print(steel["Supplier"].nunique()) --> 15


''' 
rankRoller(rc, df, park) 
Parameters:
	rc : String
	df : dataFrame
	park : String
Purpose: To plot the ranking of a roller coaster over time

Use Case: rankRoller("El Toro", wood, "Six Flags Great Adventure")
'''
def rankRoller(rc, df, park):
	rankings = df[df["Name"].str.match(rc) & df["Park"].str.match(park)]["Rank"]
	years = df[df["Name"].str.match(rc) & df["Park"].str.match(park)]["Year of Rank"]
	plt.plot(years, rankings, marker = 'o')
	plt.xlabel("Year")
	plt.ylabel("Rank")
	#invert the y-axis because we want the greater rank to appear at the top
	plt.title(rc + "`s Ranking Over Time")
	plt.subplot().invert_yaxis()
	plt.show()

plt.clf()

'''
rank2Rollers(rc1, rc2, df, park1, park2)
Parameters: rc1   : String
			rc2   : String
			df    : dataFrame
			park1 : String
			park2 : String
Purpose: To plot the rankings of 2 roller coasters over time
Use Case: rank2Rollers('El Toro', 'Boulder Dash', wood, 'Six Flags Great Adventure', 'Lake Compounce')
'''
def rank2Rollers(rc1, rc2, df, park1, park2):
	rc1info = df[df['Name'].str.match(rc1) & df['Park'].str.match(park1)]
	rc2info = df[df['Name'].str.match(rc2) & df['Park'].str.match(park2)]
	
	plt.plot(rc1info["Year of Rank"], rc1info["Rank"], color = 'red', marker = 'o', label = rc1)
	plt.plot(rc2info["Year of Rank"], rc2info["Rank"], color = 'blue', marker = '*', label = rc2)
	plt.legend()
	plt.xlabel("Year")
	plt.ylabel("Rank")
	plt.title("Ranking " + rc1 + " & " + rc2 + " Over Time")
	plt.subplot().invert_yaxis()
	plt.show()

plt.clf()
'''
ranknRollers(n, df)
Parameters: n  : Integer
			df : dataFrame
Purpose: To plot each coaster's rankings in a dataframe that has a ranking less than or equal to n
Use Case: ranknRollers(5, steel)
'''
def ranknRollers(n, df):
	chosen = df[df['Rank'] <= n]
	ax = plt.subplot()
	for coaster in set(chosen['Name']):
		rankings = chosen[chosen['Name'].str.match(coaster)]
		ax.plot(rankings['Year of Rank'], rankings['Rank'], label = coaster)
	plt.legend()
	plt.xlabel("Year")
	plt.ylabel("Rank")
	ax.invert_yaxis()
	plt.show()

plt.clf()

# load roller coaster data here:

rcData = pd.read_csv("data/roller_coasters.csv")

'''
histMaker(df, col)
Parameters: df  : dataFrame
			col : String
Purpose: To plot a histogram of df[col]
Use Case: histMaker(rcData, "speed")
'''

def histMaker(df, col):
	# This checks that col exists within df, however it does not ensure that df[col] is numerical
	if col in df.columns:
		plt.hist(df[col].dropna())
		plt.axvline(df[col].mean(), linestyle = "dashed", color = 'red')
		plt.xlabel("Height of Roller Coasters")
		plt.ylabel("Number of Roller Coasters")
		plt.show()
	

plt.clf()

'''
inversionBar(df, park)
Parameters: df   : dataFrame
			park : String
Purpose: To plot the number of inversions of all rides at a specified park
Use Case:  inversionBar(rcData, 'Six Flags Great Adventure')
'''

def inversionBar(df, park):
	rc = df[df['park'].str.match(park) & df['num_inversions'] > 0].sort_values('num_inversions', ascending=False)
	rc_names = rc['name']
	inversions = rc['num_inversions']
	plt.figure(figsize = (15, 5))
	ax = plt.subplot()
	plt.bar(range(len(rc_names)), inversions)
	ax.set_xticks(range(len(rc_names)))
	ax.set_xticklabels(rc_names, fontsize = 6)
	plt.xlabel("Ride")
	plt.ylabel("Number of Inversions")
	plt.show()

plt.clf()

'''
statusPie(df)
Parameters: df : dataFrame
Purpose : To plot a pie chart showing which percentage of the rides are operational/closed
Use Case: statusPie(rcData)
'''

def statusPie(df):
	operating = df[df['status'].str.match("status.operating")]
	closed = df[df['status'].str.match("status.closed.definitely")]
	status = [len(operating), len(closed)]
	plt.pie(status, autopct='%0.1f%%', labels = ["Operating", "Closed"])
	plt.legend()
	plt.show()

