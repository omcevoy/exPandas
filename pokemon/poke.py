import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt 
# import seaborn as sns

pd.set_option('max_columns', None)

# plt.style.use("fivethirtyeight")

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

# This line below is sorted based off of TOTAL to retrieve the 10 "strongest" pokemon
# sortedDF = df.sort_values("TOTAL", ascending = False).head(10)


# Prints the amount of types of each pokemon 
print(df['TYPE_1'].value_counts())