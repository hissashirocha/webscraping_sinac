import psycopg2
import os
import sys

try:
    conn = psycopg2.connect("dbname=SINAC user=postgres password=1520")
    cursor = conn.cursor()

    query = "CREATE TEMP TABLE temp AS SELECT a.data, a.cnae, a.uf, a.mun, a.qtde2 as qtde"
    query += " FROM (SELECT s.data, s.uf, s.mun, s.cnae, CASE WHEN m.qtde IS NULL THEN s.qtde ELSE (s.qtde - m.qtde) END AS qtde2"
    query += " FROM (SELECT * FROM estatisticas_sinac WHERE porte = 'MPE') s"
    query += " LEFT JOIN (SELECT * FROM estatisticas_sinac WHERE porte = 'MEI') m"
    query += " ON s.cnae = m.cnae AND s.mun = m.mun AND s.uf = m.uf AND s.data = m.data) a"
    query += " WHERE a.qtde2 != 0;"
    query += "DELETE FROM estatisticas_sinac WHERE porte = 'MPE';"
    query += "INSERT INTO estatisticas_sinac (data, uf, mun, cnae, porte, qtde) SELECT data, uf, mun, cnae, 'ME-EPP', qtde FROM temp;"

    cursor.execute(query)
    conn.commit()

    fo = open("/home/hissashi/Desktop/Python3/WS_SINAC/data_ref.txt", "r")
    data = fo.read()

    cursor.execute("SELECT porte, sum(qtde) FROM estatisticas_sinac WHERE data ='"+ data +"' GROUP BY porte;")
    print("Total de empresas importadas: ")
    print(cursor.fetchall())

except Excetion(e):
    print(e)
finally:
    fo.close()
    cursor.close()
    conn.close()