import pandas as pd
import psycopg2

# Conexão com o banco de dados
conn = psycopg2.connect("dbname=SINAC user=postgres password=1520")
cursor = conn.cursor()
cursor.execute("SELECT data, uf, mun, porte, cnae, qtde FROM estatisticas_sinac;")

dados = pd.DataFrame(cursor.fetchall())
dados.to_csv('sinac.csv')

cursor.close()
conn.close()
