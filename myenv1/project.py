#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 19:38:39 2025

@author: srikardesikan
"""

'''Data Exploration and Loading'''
import pandas as pd
import pymysql
from sqlalchemy import create_engine

df = pd.read_csv('/Users/srikardesikan/Desktop/Trainings/Walmart_Project/myenv1/Walmart.csv', encoding_errors='ignore')
df.shape
df.head
df.describe()
df.info()

df.duplicated().sum()
df.drop_duplicates(inplace=True)

df.isnull().sum()

#dropping missing values
df.dropna(inplace=True)
df.isnull().sum()
df.shape

#Type Conversion
df['unit_price'] = df['unit_price'].str.replace('$', '').astype(float)
df.head()
df.info()
df.columns

df['Total'] = df['unit_price'] * df['quantity']
df.head()

df.to_csv('walmart_clean_data1.csv', index=False)

#MySQL connection
engine_mysql = create_engine("mysql+pymysql://root:Suk$ik9497@localhost:3306/Walmart_db")

try:
    engine_mysql
    print("Connection Successful to MySQL")
except:
    print("Unable to connect")    

df.to_sql(name='walmart', con=engine_mysql, if_exists='append', index=False)

#df.to_sql
#host = localhost
#port = 3306
#user = root
#password = 'Suk$ik9497'