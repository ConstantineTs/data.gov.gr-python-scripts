"""
import libraries
"""

import pandas as pd
import numpy as np
import os

"""
input/output paths and
file naming
"""

path = r'C:\Users\a'
path = input("Give the path for the output csv file if you leave it blank it will go to: C:\\Users")

name = input("Give the name of the output csv file:")
file_loc = input("Give the location of the input csv file:")


#reading csv into a data frame
df = pd.read_csv(file_loc)

#field manipulation
df['speed(km/h)'] = df['speed(m/s)'] * 3.6
conditions = [(df['bearing(deg)'] >= 0) & (df['bearing(deg)'] <= 45),
              (df['bearing(deg)'] > 45) & (df['bearing(deg)'] <= 90),
              (df['bearing(deg)'] > 90) & (df['bearing(deg)'] <= 135),
              (df['bearing(deg)'] > 135) & (df['bearing(deg)'] <= 180),
              (df['bearing(deg)'] > 180) & (df['bearing(deg)'] <= 225),
              (df['bearing(deg)'] > 225) & (df['bearing(deg)'] <= 270),
              (df['bearing(deg)'] > 270) & (df['bearing(deg)'] <= 315),
              (df['bearing(deg)'] > 315) & (df['bearing(deg)'] <= 360)
             ]
choices = ["NNE","ENE","ESE","SSE","SSW","WSW","WNW","NNW"]
df['direction'] = np.select(conditions, choices, default='black')

df['Hypsometric diff'] = df['altitude(m)'].diff(periods=1)
df['Speed diff'] = df['speed(km/h)'].diff(periods=1)

#data frame export to csv
df.to_csv(os.path.join(path,name+'.csv'), encoding='utf-8')

df.head()
