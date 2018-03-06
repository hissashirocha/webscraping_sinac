import sys
import pandas as pd
import psycopg2
import os.path as path

try:
    # Lendo os arquivos csv
    if sys.argv[1]=='MPE':
        dados = pd.read_csv('EstatisticasSinacFinal.txt', header=None)
        print("inserindo MPE")
    elif sys.argv[1]=='MEI':
        dados = pd.read_csv('EstatisticasSinacMEIFinal.txt', header=None)
        print("inserindo MEI")

    # Conexão com o banco de dados
    conn = psycopg2.connect("dbname=SINAC user=postgres password=1520")
    cursor = conn.cursor()



    # Loop que varia de 1 até o tamanho do DataFrame "dados"
    for i in range(1,len(dados)):

        # Acessa cada coluna do arquivo
        porte = dados.iloc[i][0]
        data = dados.iloc[i][1]
        uf = dados.iloc[i][2]
        mun = dados.iloc[i][3]
        cnae = dados.iloc[i][4]
        qtde = dados.iloc[i][5]

        # Exibe o município no console apenas para debug
        print("mun: " + mun)

        # Monta a estrutura da query que será utilizada para inserir a linha no banco de dados
        query =  "INSERT INTO estatisticas_sinac (porte, data, uf, mun, cnae, qtde) VALUES (%s, %s, %s, %s, %s, %s);"

        # Carrega os dados e insere na variável
        tupla = (porte, data, uf, mun, str(cnae), int(qtde))

        # Aplica os dados na query e envia para o banco
        cursor.execute(query, tupla)
        conn.commit()

except Exception as e:
    print(e)

finally:
    # Fecha o cursor e a conexão
    cursor.close()
    conn.close()