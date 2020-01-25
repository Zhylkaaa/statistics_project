import sqlite3
import pandas as pd

conn = sqlite3.connect('project_data.db')

df = pd.read_csv('emission data.csv', delimiter=',')

df.to_sql('emissions', conn, if_exists='append', index=False)

conn.close()