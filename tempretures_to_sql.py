import sqlite3
import pandas as pd

conn = sqlite3.connect('project_data.db')

import os

base = 'climate-change-earth-surface-temperature-data/'
files = os.listdir('climate-change-earth-surface-temperature-data')

for file in files:
    print('reading file:', base+file)
    df = pd.read_csv(base + file, delimiter=',')
    print('create table', file[:-4])
    df.to_sql(file[:-4], conn, if_exists='append', index=False)
conn.close()
