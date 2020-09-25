# A Look at How MLS Grew in the Past 10 Years

**TLDR**
MLS was founded in the early 90s so that the US would be able to host the 1994 FIFA World Cup. Since then, it has received a lot of criticism from soccer fans for its poor business model and poor product. I took a statistical approach to how the league has grown between the years 2009 and 2019.

This repo includes the work for an exploratory data analysis project I did on data about Major League Soccer. Source data can be found on the MLS Player Unions [website](https://mlsplayers.org/resources/salary-guide "website"). It originally included data about players, their position, their salary, and their club. Using Pandas magic, I created a dataframe on MLS teams with information about each teams total payroll and payrolls for respective positions. I later wrote a script to scrape data to collect information on teams such as the amount of goals they scored in the season. (See [scrape.py](https://github.com/omcevoy/exPandas/blob/master/mls/scrape.py))

![playerSal](https://github.com/omcevoy/exPandas/blob/master/mls/img/playerSal.png)

![compare](https://github.com/omcevoy/exPandas/blob/master/mls/img/comparedPayroll.png)

![position](https://github.com/omcevoy/exPandas/blob/master/mls/img/payrollByPos.png)

![swarmplot](https://github.com/omcevoy/exPandas/blob/master/mls/img/swarmplot.png)

![scatter](https://github.com/omcevoy/exPandas/blob/master/mls/img/scatter.png)
