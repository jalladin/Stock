"creando una base de datos llamada supply_chain.db con una tabla llamada inventario."

import pandas as pd
import sqlite3

#Cargar CSV
df = pd.read_csv('data/raw/supply_chain_data.csv')

#Crear la base de datos SQLite
conn = sqlite3.connect('sql/supply_chain.db')
df.to_sql('inventario',conn, if_exists='replace',index=False)
conn.close()

