import pandas as pd

df = pd.read_csv('data.csv')
df.to_excel('data.xlsx', sheet_name='Sheet1')

import sqlite3
