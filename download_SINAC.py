# This Python file uses the following encoding: utf-8
import os
import sys
import re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Define parâmetros de download do Firefox
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2) # Não irá para a pasta Downloads
profile.set_preference("browser.download.manager.showWhenStarting", False) # Não exibe status do download
profile.set_preference("browser.download.dir", '/home/hissashi/Desktop/Python3/WS_SINAC/') # Local do download
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv") # Não pede permissão para download de txt ou csv

# Faz com que o Firefox rode no mode headless (sem ser exibido)
os.environ['MOZ_HEADLESS'] = '1'

# Aponta para o arquivo binário do Firefox e carrega os parâmetros para a criação do driver
binary = FirefoxBinary('/usr/bin/firefox', log_file=sys.stdout)
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=profile)

# Abre a página
driver.get('http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATBHE/estatisticasSinac.app/Default.aspx')

# Identifica se o processamento será de MPE ou de MEI e clica no respectivo link
# Os demais passos são identicos para ambos
if sys.argv[1]=='MPE':
    driver.find_element_by_id('ctl00_ctl00_Conteudo_AntesTabela_lnkOptantesPorCNAE').click()
elif sys.argv[1]=='MEI':
    driver.find_element_by_id('ctl00_ctl00_Conteudo_AntesTabela_lnkEstatisticasOptantesPorCNAEMeiTotal').click()

# Identifica menu dropdown e escolhe a opção "Município"
Select(driver.find_element_by_id("ctl00_ctl00_Conteudo_AntesTabela_ddlColuna")).select_by_visible_text("Município")

try:
    for i in range (1, 28):
        driver.find_element_by_id('ctl00_ctl00_Conteudo_AntesTabela_btnFiltros').click()

        # Carrega o menu dropdown contendo os nomes dos UF
        uf = Select(driver.find_element_by_id("ctl00_ctl00_Conteudo_AposTabela_ddlUf"))
        print("pegando: "+uf.options[i].get_attribute('value'))

        # Escolhe 1 UF por vez
        uf.options[i].click()
        time.sleep(20)

        # Clica na opção "Todos os municípios"
        driver.find_element_by_id('chkTodosMunicipios').click()
        time.sleep(10)

        # Clica no botão OK. Este botão não tem ID no html, portanto, a busca foi feita por texto
        driver.find_element_by_xpath("//*[contains(text(),'Ok')]").click()
        time.sleep(5)

        # Clica com ENTER ao invés do clique.
        # Isso foi feito pois, ao clicar no botão Exibir, a página permanecia em um load eterno,
        # impedindo o código de continuar a execução. Apesar da página continuar no load, ao clicar com
        # ENTER, o código continua executando.
        driver.find_element_by_id("ctl00_ctl00_Conteudo_AntesTabela_btnExibir").send_keys(u'\ue007')
        print("exibindo tabela")
        time.sleep(30)

        # Clica no botão que gera o CSV
        driver.find_element_by_id("ctl00_ctl00_Conteudo_AreaInterna_btnCsv").send_keys(u'\ue007')
        time.sleep(5)
        print("fazendo download")

    # Recupera a data de referência dos dados
    texto = driver.find_element_by_id("ctl00_ctl00_Conteudo_AntesTabela_lblDataEstatistica")
    print(texto.text)
    match = re.search(r'\d{2}\/\d{2}\/\d{4}', texto.text)
    data = match.group()
    print(data)

    # Salva a data em um arquivo para ser usado posteriormente
    fo = open("/home/hissashi/Desktop/Python3/WS_SINAC/data_ref.txt", "w")
    fo.write(data)
    print("escreveu a data no arquivo")
    # fo.close()

except Exception as e:
    print(e)
finally:
    fo.close()
    driver.quit()
