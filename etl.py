# -*- coding: utf-8 -*-

import pandas as pd  
##  To read and work on the data
import sqlite3  ##  To work on the database
df = pd.read_csv("https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data")  ##  Data retreival from the URL.
df = df.iloc[:41]  ##  Unncessary text removed from the data
list = [(df.iloc[row][0].split()) for row in range(len(df))]  ##  Creating a list with list comprehension consisting of lists(yearly data)
dfob = pd.DataFrame(list)  ##  Converting this list into a DataFrame

dfob.columns = ['Year', '12-01', '01-02', '02-03', '03-04', '04-05', '05-06', '06-07', '07-08', '08-09', '09-10', '10-11', '11-12']
##  The header names are renewed.
print(dfob.columns)