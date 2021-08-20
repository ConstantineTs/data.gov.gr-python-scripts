"""""
import libraries
"""""

import requests
import pandas as pd
#from pandas import DataFrame
import json
import os

"""""
user inputs
date time inputs
output csv file name
"""""

st_year = str(input("Give the start year:"))
st_month = str(input("Give the start month:"))
st_date = str(input("Give the start date:"))
en_year = str(input("Give the end year:"))
en_month = str(input("Give the end month:"))
en_date = str(input("Give the end date:"))
name = input("Give the name of the output csv file:")

#input path
path = r'C:\Users\<user_name>'
path = input("Give the path for the output csv file if you leave it blank it will go to: C:\\Users")

web_location = input("Give the url:")
url = web_location
#token authorization
headers = {'Authorization':'Token <my token>'}
response = requests.get(url, headers=headers)
dt = pd.DataFrame(data=response)
print (response.json())
#json return validity check
if response.text == "[]":
    print("If the return json is empty [] please check your input dates through the official web portal https://www.data.gov.gr/")

data= json.dumps(response.json())
#json to data frame
df = pd.DataFrame(eval(data))

#export to csv
df.to_csv(os.path.join(path,name+'.csv'), encoding='utf-8')

df
