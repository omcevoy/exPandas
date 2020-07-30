import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

pd.set_option('max_columns', None)

plt.style.use("dark_background")

df = pd.read_csv("Pokemon.csv")
# Capitalize columns and replace spcaces
df.columns = df.columns.str.upper().str.replace(' ', '_')

# I don't like or understand mega pokemon so I am removing them from the dataset
df["IS_MEGA"] = df["NAME"].apply(lambda x : True if "Mega" in x else False)
df = df[df["IS_MEGA"] == False]
# Remove the two columns that I don't need
df.drop(["IS_MEGA", "#"],  axis = 1, inplace = True)

df.set_index('NAME', inplace = True)

# print('The columns of the dataset are: ',df.columns) 
# print('The shape of the dataframe is: ',df.shape)

# Fill NaN values in Type2 with corresponding values of Type1 IF the pokemon does not have a second type
df['TYPE_2'].fillna(df['TYPE_1'], inplace=True) 

# These lines below help find the strongest pokemon for each type
# strongPoke = df.sort_values(by = "TOTAL", ascending = False)
# strongPoke.drop_duplicates(subset = ["TYPE_1"], keep = "first")

# print(strongPoke)


# Prints the amount of types of each pokemon 
# print(df['TYPE_1'].value_counts())


# A histogram that plots each pokemons Attack stats. The output can be found at /img/img1.png
# bins = range(0, 200, 20)
# plt.hist(df["ATTACK"], bins, histtype = "bar", rwidth = 1.2, color = "#c2c2d6")
# plt.xlabel('Attack Rating')
# plt.ylabel('# of Pokemon')
# plt.plot()
# plt.axvline(df['ATTACK'].mean(), linestyle = "dashed", color = "#ff80bf")
# plt.show()

# A scatterplot that plots the attack/defense stats for legendary & nonlegendary pokemon. The output can be found at /img/img2.png
# lgnds = df[df["LEGENDARY"] == True]
# nonlgnds = df[df["LEGENDARY"] == False]

# plt.scatter(lgnds["ATTACK"], lgnds["DEFENSE"], color = "#ffb3b3", label = "Legendary Pokemon", marker = '*', s = 50)
# plt.scatter(nonlgnds["ATTACK"], nonlgnds["DEFENSE"], color = "#b3d9ff", label = "Regular Pokemon", s = 15)
# plt.xlabel("Attack")
# plt.ylabel("Defense")
# plt.legend()
# plt.plot()

# fig = plt.gcf()  #get the current figure using .gcf()
# fig.set_size_inches(12,6) #set the size for the figure
# plt.show()

gen1 = df[df["GENERATION"] == 1]

plt.figure(figsize = (12, 6))
best_types = gen1["TYPE_1"].value_counts()[:10] #takes the ten best types 
gen1plt = gen1[gen1["TYPE_1"].isin(best_types.index)]

sns.swarmplot(x = "TYPE_1", y = "TOTAL", data = gen1plt, hue = "LEGENDARY")
plt.axhline(gen1plt["TOTAL"].mean(), color = "red", linestyle = "dashed")
plt.show()
