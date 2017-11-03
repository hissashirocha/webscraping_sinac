import pandas as pd
import psycopg2

dados = pd.read_csv('EstatisticasSinacFinal.txt', header=None)

conn = psycopg2.connect("dbname=SINAC user=postgres password=1520")
cursor = conn.cursor()

for i in range(1,len(dados)):
    data = dados.iloc[i][0]
    uf = dados.iloc[i][1]
    mun = dados.iloc[i][2]
    cnae = dados.iloc[i][3]
    qtde = dados.iloc[i][4]
    print("data: " + data)
    print("uf: " + uf)
    print("mun: " + mun)
    print("cnae: " + str(cnae))
    print("qtde: " + str(qtde))
    query =  "INSERT INTO estatisticas (data, uf, mun, cnae, qtde) VALUES (%s, %s, %s, %s, %s);"
    tupla = (data, uf, mun, cnae, int(qtde))
    cursor.execute(query, tupla)
    conn.commit()
cursor.close()
conn.close()