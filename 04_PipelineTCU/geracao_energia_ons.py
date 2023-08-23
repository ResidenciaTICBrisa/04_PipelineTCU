from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os

driver = webdriver.Chrome()

def findElementByXpath(xpath, d):
    return d.find_element(By.XPATH, value=xpath)

def findElementByClass(cl, d):
    return d.find_element(By.CLASS_NAME, value=cl)

def findElementsByClass(cl, d):
    return d.find_elements(By.CLASS_NAME, value=cl)

def findElementByCss(css, d):
    return d.find_element(By.CSS_SELECTOR, value=css)

def getHTML(elem):
    return elem.get_attribute('innerHTML')

def compHTMLStr(elem, str):
    return getHTML(elem).find(str)

def searchElementList(list, str):
    for item in list:
        if compHTMLStr(item,str) != -1:
            return item
    return None

def downloadCSV():
    botao_baixar = findElementByCss('div[aria-label="Download"]', driver)
    botao_baixar.click()
    time.sleep(5)
    botao_crosstab = findElementByCss('button[data-tb-test-id="DownloadCrosstab-Button"]', driver)
    driver.execute_script("arguments[0].click();", botao_crosstab)
    time.sleep(5)
    imgs = findElementsByClass('f1hykqr2', driver)
    for img in imgs:
        if compHTMLStr(img,'Simples Geração de Energia Dia') != -1:
            break
    img.click()
    time.sleep(5)
    opcoes = findElementsByClass('f1u2kjnq', driver)
    opcao_csv = searchElementList(opcoes, 'CSV')
    opcao_csv.click()
    time.sleep(5)
    botao_tab = findElementByCss('button[data-tb-test-id="export-crosstab-export-Button"]', driver)
    driver.execute_script("arguments[0].click();", botao_tab)
    time.sleep(8)

if __name__ == '__main__' :  
    driver.implicitly_wait(40)
    #Acessando URL
    driver.get('https://tableau.ons.org.br/t/ONS_Publico/views/GeraodeEnergia/HistricoGeraodeEnergia?%3Aembed=y&%3AshowAppBanner=false&%3AshowShareOptions=true&%3Adisplay_count=no&%3AshowVizHome=no')
    
    #Encontrando dropdown responsável pela escolha da escala de tempo da tabela e mudando para ano 
    pathEscala = '//*[@id="tableau_base_widget_ParameterControl_1"]/div/div[2]/span/div[1]'
    caixa_selecao_escala = findElementByXpath(pathEscala, driver)
    caixa_selecao_escala.click()
    lista_escala = findElementsByClass('tabMenuItem', driver)
    escala_ano = searchElementList(lista_escala, 'Ano')
    escala_ano.click()

    #Encontrando dropdowns responsáveis pelo escopo, tipo de fonte/tecnologia e combustível 
    caixas_selecao = findElementsByClass('CategoricalFilterBox',driver)
    cont=0
    for caixa in caixas_selecao:
        if compHTMLStr(caixa,'title="Escopo') != -1:
            caixa_escopo = findElementByClass('tabComboBoxNameContainer', caixa)
            cont += 1
        elif compHTMLStr(caixa, 'title="Tipo de Usina') != -1:
            caixa_tipo_usina = findElementByClass('tabComboBoxNameContainer', caixa)
            cont += 1
        elif compHTMLStr(caixa,'title="Combustível') != -1:
            caixa_combustivel = findElementByClass('tabComboBoxNameContainer', caixa)
            cont+=1
        if cont >= 3:
            break
    time.sleep(15)

    #Mudando o escopo para "(All)"
    caixa_escopo.click()
    lista_escopo = findElementsByClass('FIItem', driver)
    time.sleep(5)
    escopo_all = searchElementList(lista_escopo, '(All)')
    escopo_all.click()
    time.sleep(5)

    df_geracao_energia = pd.DataFrame()
    #Pegando Eólica, Hidrelétrica, Nuclear, Solar
    fontes = ['Eólica', 'Hidrelétrica', 'Nuclear', 'Solar']
    for fonte in fontes:
        caixa_tipo_usina.click()
        time.sleep(5)
        lista_tipo_usina = findElementsByClass('FIItem', driver)
        time.sleep(5)
        elFonte = searchElementList(lista_tipo_usina, fonte)
        elFonte.click()
        time.sleep(5)
        downloadCSV()
        arquivo = 'Simples Geração de Energia Barra Semana.csv'
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads/", arquivo)
        
        with open(download_folder, 'r', encoding='utf-16') as file:
            cont = 0
            for l in file.readlines():
                if l != '\n':
                    cont +=1
        with open(download_folder, 'r', encoding='utf-16') as file:
            c = 0
            for l in file.readlines():
                if l != '\n':
                    c += 1
                    if c == cont:
                        new_line = l.split(',')[0] + l.split(',')[1]
        with open(download_folder, 'w', encoding='utf-16') as file:
            file.writelines(new_line)
        df_planilha = pd.read_csv(download_folder,encoding='utf-16', delimiter='\t', header=None)
        df_planilha.drop(df_planilha.iloc[:, 9:-1], axis=1, inplace=True)
        df_planilha.drop(df_planilha.iloc[:, 0:5], axis=1, inplace=True)
        df_planilha.drop(df_planilha.iloc[:, 1:3], axis=1, inplace=True)
        df_geracao_energia = pd.concat([df_geracao_energia, df_planilha])
        os.remove(download_folder)
    fonte_anterior = '(All)'
    fontes = ['Biomassa']
    caixa_tipo_usina.click()
    time.sleep(5)
    lista_tipo_usina = findElementsByClass('FIItem', driver)
    time.sleep(5)
    elFonte = searchElementList(lista_tipo_usina, 'Térmica')
    elFonte.click()
    time.sleep(5)
    for fonte in fontes:
        caixa_combustivel.click()
        time.sleep(5)
        listaCheck = findElementsByClass('facetOverflow', driver)
        checkAll = searchElementList(listaCheck, fonte_anterior)
        checkAll = findElementByCss('input[class="FICheckRadio"]', checkAll)       
        checkAll.click()
        time.sleep(5)
        checkFonte = searchElementList(listaCheck, fonte)
        checkFonte = findElementByCss('input[class="FICheckRadio"]',checkFonte)
        checkFonte.click()
        time.sleep(5)
        botaoApply = findElementByCss('button[title="Apply"]', driver)
        botaoApply.click()
        time.sleep(10)
        tela = findElementByClass('tab-glass', driver)
        tela.click()
        time.sleep(5)
        downloadCSV()
        arquivo = 'Simples Geração de Energia Barra Semana.csv'
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads/", arquivo)
        
        with open(download_folder, 'r', encoding='utf-16') as file:
            cont = 0
            for l in file.readlines():
                if l != '\n':
                    cont +=1
        with open(download_folder, 'r', encoding='utf-16') as file:
            c = 0
            for l in file.readlines():
                if l != '\n':
                    c += 1
                    if c == cont:
                        new_line = l.split(',')[0] + l.split(',')[1]
        with open(download_folder, 'w', encoding='utf-16') as file:
            file.writelines(new_line)
        df_planilha = pd.read_csv(download_folder,encoding='utf-16', delimiter='\t', header=None)
        df_planilha.drop(df_planilha.iloc[:, 9:-1], axis=1, inplace=True)
        df_planilha.drop(df_planilha.iloc[:, 0:5], axis=1, inplace=True)
        df_planilha.drop(df_planilha.iloc[:, 1:3], axis=1, inplace=True)
        df_geracao_energia = pd.concat([df_geracao_energia, df_planilha])
        os.remove(download_folder)
        fonte_anterior = fonte
    print(df_geracao_energia)
    driver.close()