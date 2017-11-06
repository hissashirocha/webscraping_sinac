Web scraping and data manipulation with Python, Shell Scripting, Selenium and Pandas

O projeto tem por objetivo extrair dados de numeros de empresas por UF, CNAE (atividade economica) e cidade, do site Estatisticas SINAC, realizar tratamento nos dados e inseri-los em banco de dados.

O arquivo que deve ser executado tem por nome robo_SINAC.sh (LINUX). Esse arquivo aciona o arquivo download_SINAC.py, responsavel pelo web scraping (utilizando Python e a biblioteca Selenium), em seguida realiza tratamento nos arquivos CSV baixados, para entao chamar outro arquivo (readSINAC_insertDB.py) que, com a utilizacao de Pandas, faz a leitura do arquivo consolidado e inseri os dados em um banco de dados PostgreSQL.

Este projeto ainda nao esta finalizado ate a data de 03/11/2017.
