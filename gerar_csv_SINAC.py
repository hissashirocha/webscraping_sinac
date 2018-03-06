import pandas as pd
import psycopg2

# Conexão com o banco de dados
conn = psycopg2.connect("dbname=SINAC user=postgres password=1520")
cursor = conn.cursor()
query = "SELECT data, uf, mun, porte, cnae, qtde FROM estatisticas_sinac"
query += " WHERE data IN (SELECT DISTINCT data FROM estatisticas_sinac ORDER BY data DESC LIMIT 1);"
cursor.execute(query)

dados = pd.DataFrame(cursor.fetchall())

#Cria o arquivo sinac.csv
dados.to_csv('sinac.csv')

cursor.close()
conn.close()
