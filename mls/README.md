# A Look at How MLS Grew in the Past 10 Years

**TLDR**
MLS was founded in the early 90s so that the US would be able to host the 1994 FIFA World Cup. Since then, it has received a lot of criticism from soccer fans for its poor business model and poor product. I took a statistical approach to how the league has grown between the years 2009 and 2019.

This repo includes the work for an exploratory data analysis project I did on data about Major League Soccer. Source data can be found on the MLS Player Unions [website](https://mlsplayers.org/resources/salary-guide "website"). It originally included data about players, their position, their salary, and their club. Using Pandas magic, I created a dataframe on MLS teams with information about each teams total payroll and payrolls for respective positions. I later wrote a script to scrape data to collect information on teams such as the amount of goals they scored in the season. (See [scrape.py](https://github.com/omcevoy/exPandas/blob/master/mls/scrape.py))

![playerSal](https://github.com/omcevoy/exPandas/blob/master/mls/img/playerSal.png)

This graphic reveals that in the past 10 years, MLS has significantly signed more players as one would expect due to the addition of multiple expansion teams. Additionally, more players in the league are earning higher wages. In 2019 roughly 54% of MLS players earned less than $200,000 annually (base salary), whereas in 2009 nearly 91% of the players were earning below $200,000.

![compare](https://github.com/omcevoy/exPandas/blob/master/mls/img/comparedPayroll.png)
This graphic compares the payrolls of the original 14 MLS teams after the ten years. The general trend here is that most teams have significantly increased their payroll during this period. Some teams such as Toronto FC, Sporting KC, and Seattle have invested heavily into their players and have had championship seasons to show for it.  

![position](https://github.com/omcevoy/exPandas/blob/master/mls/img/payrollByPos.png)
This graphic looks at each teams payroll broken down by position. The graphic reveals that most teams spend the most money on their attacking players. This fact translates on the field, as MLS is notorious for bad defending and lack of solid team play.  

It is worth noting that for players listed as a 'D-M' or 'M-F', meaning they may occasionally play in the midfield, I included them in the Defenders/Forwards budget as they were likely signed to contribute on the defensive/attacking ends. 

![swarmplot](https://github.com/omcevoy/exPandas/blob/master/mls/img/swarmplot.png)

The swarmplot provides extra insight to how teams pay their players. The different ideologies throughout the league are prevalent here. LA Galaxy takes the traditional MLS approach by offering a single player a large salary and hope he carries the weight, while a team like Toronto FC has 3 players earning good salaries. It is also visibly apparent, that the majority of players are earning below the league average. 

![scatter](https://github.com/omcevoy/exPandas/blob/master/mls/img/scatter.png)
This scatter plot looks at the relationship between an attacking budget and the number of wins a team gets in a season. The points on the graph are also sized based off of the number of goals the team scored throughout the season. 
