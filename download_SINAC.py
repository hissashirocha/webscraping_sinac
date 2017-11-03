# This Python file uses the following encoding: utf-8
import os
import sys
import re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/home/hissashi/Desktop/Python3/WS_SINAC/')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

os.environ['MOZ_HEADLESS'] = '1'
binary = FirefoxBinary('/usr/bin/firefox', log_file=sys.stdout)
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=profile)

driver.get('http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATBHE/estatisticasSinac.app/Default.aspx')
driver.find_element_by_id('ctl00_ctl00_Conteudo_AntesTabela_lnkOptantesPorCNAE').click()
Select(driver.find_element_by_id("ctl00_ctl00_Conteudo_AntesTabela_ddlColuna")).select_by_visible_text("Município")

try:
    for i in range (1, 28):
        driver.find_element_by_id('ctl00_ctl00_Conteudo_AntesTabela_btnFiltros').click()
        uf = Select(driver.find_element_by_id("ctl00_ctl00_Conteudo_AposTabela_ddlUf"))
        print("pegando: "+uf.options[i].get_attribute('value'))
        uf.options[i].click()
        time.sleep(20)
        driver.find_element_by_id('chkTodosMunicipios').click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[contains(text(),'Ok')]").click()
        time.sleep(5)
        driver.find_element_by_id("ctl00_ctl00_Conteudo_AntesTabela_btnExibir").send_keys(u'\ue007')
        print("exibindo tabela")
        time.sleep(30)
        driver.find_element_by_id("ctl00_ctl00_Conteudo_AreaInterna_btnCsv").send_keys(u'\ue007')
        time.sleep(5)
        print("fazendo download")

    texto = driver.find_element_by_id("ctl00_ctl00_Conteudo_AntesTabela_lblDataEstatistica")
    print(texto.text)
    match = re.search(r'\d{2}\/\d{2}\/\d{4}', texto.text)
    data = match.group()
    print(data)

    fo = open("/home/hissashi/Desktop/Python3/WS_SINAC/data_ref.txt", "w")
    fo.write(data)
    print("escreveu no arquivo")
    fo.close()

except Exception as e:
    print(e)
finally:
    driver.quit()
