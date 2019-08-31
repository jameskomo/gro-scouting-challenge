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

##  Gathering the irregular information about the start and end dates in one list containing of lists of dates via compile_data function.
def compile_data(data):
    start_date = [[[str(int(data['Year'][i])-1) + '-' + data.columns[1][0]+data.columns[1][1]] for i in range(len(data))]]
    end_date = [[[data['Year'][i] + '-' + data.columns[1][3]+data.columns[1][4]] for i in range(len(data))]]
    for j in range(1,12):
        start_date.append([[data['Year'][i] + '-' + data.columns[j+1][0]+data.columns[j+1][1]] for i in range(len(data))])
        end_date.append([[data['Year'][i] + '-' + data.columns[j+1][3]+data.columns[j+1][4]] for i in range(len(data))])
        for i in range(len(data)):
            if (dfob.iloc[i][j+1] == '-999.00'):
                dfob.iloc[i][j+1] = "NULL"
    start_matrix = pd.DataFrame(start_date)
    end_matrix = pd.DataFrame(end_date)
    return start_matrix, end_matrix
# print(dfob.columns)