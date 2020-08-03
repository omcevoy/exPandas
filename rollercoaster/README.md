# More Practice With Pandas and Matplotlib

This project was completed so I could get more practice using Pandas and Matplotlib. For this project, I was given three files containing data about roller coasters. 

I ended up writing 6 functions that visualize different components of the 3 datasets. 

![img1](https://github.com/omcevoy/exPandas/blob/master/rollercoaster/img/fig1.png)
* This visualization was obtained by calling the *rankRoller* function, which plots the ranking of a specific ride over time
  * rankRoller("El Toro", wood, "Six Flags Great Adventure")
  
![img2](https://github.com/omcevoy/exPandas/blob/master/rollercoaster/img/fig2.png)
* This visualization was obtained by calling *rank2Rollers*, which plots the ranking of two specific rides over time.
  * rank2Rollers('El Toro', 'Boulder Dash', wood, 'Six Flags Great Adventure', 'Lake Compounce')
  
![img3](https://github.com/omcevoy/exPandas/blob/master/rollercoaster/img/fig3.png)
* This visualization was obtained by calling the *ranknRollers* function, which plots the rankings of all the coasters that have a ranking less than (lower is better) or equal to n
  * ranknRollers(5, steel)
  
![img4](https://github.com/omcevoy/exPandas/blob/master/rollercoaster/img/fig4.png)
* This visualization was obtained by calling the *histMaker* function, which plots a simple histogram of the specified column
  * histMaker(rcData, "speed")
  
![img5](https://github.com/omcevoy/exPandas/blob/master/rollercoaster/img/fig5.png)
* This visualization was obtained by calling the *inversionBar* function, which creates a bar chart that plots all the coasters at a specified park with inversions
  * inversionBar(rcData, 'Six Flags Great Adventure')

![img6](https://github.com/omcevoy/exPandas/blob/master/rollercoaster/img/fig6.png)
* This visualization was obtained by calling the *statusPie* function, which simply creates a pie chart plotting the percentage of coasters at a park that are operational/closed
  * statusPie(rcData)


