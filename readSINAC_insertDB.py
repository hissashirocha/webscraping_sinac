import pandas as pd
import psycopg2

# Lendo o arquivo csv
dados = pd.read_csv('EstatisticasSinacFinal.txt', header=None)

# Conexão com o banco de dados
conn = psycopg2.connect("dbname=SINAC user=postgres password=1520")
cursor = conn.cursor()

try:

    # Loop que varia de 1 até o tamanho do DataFrame "dados"
    for i in range(1,len(dados)):

        # Acessa cada coluna do arquivo
        data = dados.iloc[i][0]
        uf = dados.iloc[i][1]
        mun = dados.iloc[i][2]
        cnae = dados.iloc[i][3]
        qtde = dados.iloc[i][4]

        # Exibe o município no console apenas para debug
        print("mun: " + mun)

        # Monta a estrutura da query que será utilizada para inserir a linha no banco de dados
        query =  "INSERT INTO estatisticas (data, uf, mun, cnae, qtde) VALUES (%s, %s, %s, %s, %s);"

        # Carrega os dados e insere na variável
        tupla = (data, uf, mun, str(cnae), int(qtde))

        # Aplica os dados na query e envia para o banco
        cursor.execute(query, tupla)
        conn.commit()

except Exception as e:
    print(e)

finally:
    # Fecha o cursor e a conexão
    cursor.close()
    conn.close()