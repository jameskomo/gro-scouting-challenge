# -*- coding: utf-8 -*-

import pandas as pd  
##  To read and work on the data
import sqlite3  ##  To work on the database
df = pd.read_csv("https://www.esrl.noaa.gov/psd/enso/mei/data/meiv2.data")  ##  Data retreival from the URL.
df = df.iloc[:41]  ##  Unncessary text removed from the data
print(df)