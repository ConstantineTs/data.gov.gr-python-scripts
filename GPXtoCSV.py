""""
import libraries
""""

import gpxpy
import gpxpy.gpx
import pandas as pd
import os

"""""
input/output paths and file naming
""""

path = r'C:\Users\a'
path = input("Give the path for the output csv file if you leave it blank it will go to: C:\\Users")
name = input("Give the name of the output csv file:")
file_loc = input("Give the location of the input gpx file:")

""""
gpx file opening, parsing,
dataframe creation
""""

gpx_file = open(file_loc,mode='r')
gpx = gpxpy.parse(gpx_file)
data = gpx.tracks[0].segments[0].points
df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time', 'speed(m/s)'])
for point in data:
    df = df.append({'lon': point.longitude,
                    'lat' : point.latitude,
                    'alt' : point.elevation,
                    'time' : point.time,
                   'speed': point.speed}, ignore_index=True)

#creating three new fields on the data frame, derivatives of existing fields

df['speed(km/h)'] = df['speed'] * 3.6
df['Hypsometric diff'] = df['alt'].diff(periods=1)
df['Speed diff'] = df['speed(km/h)'].diff(periods=1)

#output to csv

df.to_csv(os.path.join(path,name+'.csv'), encoding='utf-8')
