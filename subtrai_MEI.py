import psycopg2

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
    query += "INSERT INTO estatisticas_sinac (data, uf, mun, cnae, porte, qtde) SELECT data, uf, mun, cnae, 'MPE', qtde FROM temp;"

    cursor.execute(query)
    conn.commit()

    cursor.execute("SELECT porte, sum(qtde) FROM estatisticas_sinac GROUP BY porte;")
    print(cursor.fetchall())


except Excetion(e):
    print(e)
finally:
    cursor.close()
    conn.close()