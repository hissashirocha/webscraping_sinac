# Web scraping and data manipulation with Python, Shell Scripting, Selenium and Pandas

O projeto tem por objetivo extrair dados de números de empresas por UF, CNAE (atividade econômica) e cidade, do site Estatísticas SINAC, realizar tratamento nos dados e inserí-los em banco de dados.

ETAPAS:

1 - Rodar o script SINAC.sh, que é o executor do web scraping e responsável por acionar os códigos Python

2 - O código download_SINAC.py é acionado para navegar no site Estatísticas SINAC utilizando a biblioteca Selenium. Ao final, vários arquivos csv são baixados automaticamente.

3 - Ao retornar para o script, os arquivos são tratados utilizando awk e sed e remontados em dois únicos arquivos.

4 - O código insert_SINAC.py é acionado para fazer a leitura dos arquivos, utilizando a biblioteca Pandas, e insere os dados em banco de dados PostegreSQL local.

5 - Para finalizar, o código subtrai_MEI.py é acionado para subtrair do número de MPE as empresas que são MEI, de forma que MPE represente apenas ME e EPP.
