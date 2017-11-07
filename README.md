Web scraping and data manipulation with Python, Shell Scripting, Selenium and Pandas

O projeto tem por objetivo extrair dados de números de empresas por UF, CNAE (atividade econômica) e cidade, do site Estatísticas SINAC, realizar tratamento nos dados e inserí-los em banco de dados.

O arquivo que deve ser executado tem por nome SINAC.sh (shell script). Esse arquivo aciona o código download_SINAC.py, responsável pelo web scraping (utilizando Python e a biblioteca Selenium), em seguida realiza tratamento nos arquivos CSV baixados, para então chamar o código insert_SINAC.py, que, com a utilizacao de Pandas, faz a leitura do arquivo consolidado e insere os dados em um banco de dados PostgreSQL.

Esta versão é a beta do projeto, com data de 07/11/2017.
