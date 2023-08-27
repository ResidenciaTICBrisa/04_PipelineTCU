from selenium import webdriver
import pandas as pd
import os
import pytest
import pathlib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome()
def findElementByXpath(xpath, d):
    try:
        element = WebDriverWait(d, 15).until(EC.element_to_be_clickable\
                                             ((By.XPATH, xpath)))

    finally:
        return element

def findElementByClass(cl, d):
    try:
        element = WebDriverWait(d, 15).until(EC.element_to_be_clickable\
                                             ((By.CLASS_NAME, cl)))

    finally:
        return element

def findElementsByClass(cl, d):
    try:
        element = WebDriverWait(d, 15).until(
                lambda x: x.find_elements(By.CLASS_NAME,cl)
                )
        time.sleep(1)
    finally:
        return element


def findElementByCss(css, d):
    try:
        element = WebDriverWait(d, 15).until(
            lambda x: x.find_element(By.CSS_SELECTOR,css))
    finally:
            return element

def getHTML(elem):
    return elem.get_attribute('innerHTML')

def compHTMLStr(elem, str):
    return getHTML(elem).find(str)

def searchElementList(list, str):
    for item in list:
        if compHTMLStr(item,str) != -1:
            return item
    return None


def downloadCSV(driver):
    botao_baixar = findElementByCss('div[aria-label="Download"]', driver)
    time.sleep(3)
    botao_baixar.click()
    botao_crosstab = findElementByCss('button[data-tb-test-id="DownloadCrosstab-Button"]', driver)
    driver.execute_script("arguments[0].click();", botao_crosstab)
    imgs = findElementsByClass('f1hykqr2', driver)
    for img in imgs:
        if compHTMLStr(img,'Simples Geração de Energia Dia') != -1:
            break
    time.sleep(3)
    img.click()
    opcoes = findElementsByClass('f1u2kjnq', driver)
    opcao_csv = searchElementList(opcoes, 'CSV')
    time.sleep(3)
    opcao_csv.click()
    botao_tab = findElementByCss('button[data-tb-test-id="export-crosstab-export-Button"]', driver)
    driver.execute_script("arguments[0].click();", botao_tab)
    time.sleep(3)

if __name__ == '__main__' :  
    #Acessando URL
    driver.get('https://tableau.ons.org.br/t/ONS_Publico/views/GeraodeEnergia/HistricoGeraodeEnergia?%3Aembed=y&%3AshowAppBanner=false&%3AshowShareOptions=true&%3Adisplay_count=no&%3AshowVizHome=no')
    #Encontrando dropdown responsável pela escolha da escala de tempo da tabela e mudando para ano 
    pathEscala = '//*[@id="tableau_base_widget_ParameterControl_1"]/div/div[2]/span/div[1]'
    caixa_selecao_escala = findElementByXpath(pathEscala, driver)
    time.sleep(3)
    caixa_selecao_escala.click()
    lista_escala = findElementsByClass('tabMenuItem', driver)
    escala_ano = searchElementList(lista_escala, 'Ano')
    time.sleep(3)
    escala_ano.click()
    #Encontrando dropdowns responsáveis pelo escopo, tipo de fonte/tecnologia e combustível 
    caixas_selecao = findElementsByClass('CategoricalFilterBox',driver)
    count=0
    for caixa in caixas_selecao:
        if compHTMLStr(caixa,'title="Escopo') != -1:
            caixa_escopo = findElementByClass('tabComboBoxNameContainer', caixa)
            count += 1
        elif compHTMLStr(caixa, 'title="Tipo de Usina') != -1:
            caixa_tipo_usina = findElementByClass('tabComboBoxNameContainer', caixa)
            count += 1
        elif compHTMLStr(caixa,'title="Combustível') != -1:
            caixa_combustivel = findElementByClass('tabComboBoxNameContainer', caixa)
            count+=1
        if count >= 3:
            break
    #Mudando o escopo para "(All)"
    time.sleep(1)
    caixa_escopo.click()
    lista_escopo = findElementsByClass('FIItem', driver)
    escopo_all = searchElementList(lista_escopo, '(All)')
    escopo_all.click()
    #Mudando periodo de tempo de 1998 até 2030
    XpathPeriodo1998 = '//*[@id="typein_[Parameters].[Início Primeiro Período GE Comp 3 (cópia)]"]/span[1]/input'
    inputPeriodo1998=findElementByXpath(XpathPeriodo1998,driver)
    time.sleep(3)
    inputPeriodo1998.click()
    inputPeriodo1998.send_keys('01/01/1999')
    inputPeriodo1998.send_keys(Keys.RETURN)
    XpathPeriodo2030 = '//*[@id="typein_[Parameters].[Fim Primeiro Período GE Comp 3 (cópia)]"]/span[1]/input'
    inputPeriodo2030=findElementByXpath(XpathPeriodo2030,driver)
    inputPeriodo2030.click()
    inputPeriodo2030.send_keys('12/12/2030')
    inputPeriodo2030.send_keys(Keys.RETURN)
    #Selecionando o arquivo onde iremos colocar as fonte
    separeted_line=pd.DataFrame()
    #Pegando Eólica, Hidrelétrica, Nuclear, Solar
    fontes = ['Eólica', 'Hidrelétrica', 'Nuclear', 'Solar']
    for fonte in fontes:
        time.sleep(8)
        caixa_tipo_usina.click()
        lista_tipo_usina = findElementsByClass('FIItem', driver)
        time.sleep(5)
        elFonte = searchElementList(lista_tipo_usina, fonte)
        elFonte.click()
        time.sleep(3)
        downloadCSV(driver)
        arquivo = 'Simples Geração de Energia Barra Semana.csv'
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads/", arquivo)        
        df_planilha = pd.read_csv(download_folder,encoding='utf-16', delimiter='\t', header=None)
        df_planilha = df_planilha.drop(index=[0,1,2]).reset_index(drop=True) 
        df_planilha.drop(df_planilha.iloc[:, 0:5], axis=1, inplace=True)
        df_planilha.drop(df_planilha.iloc[:, 1:3], axis=1, inplace=True)
        df_planilha.drop(df_planilha.iloc[:, 2:5], axis=1, inplace=True)
        for index, row in df_planilha.iterrows():
            coluna = 3
            while coluna<len(df_planilha.iloc[index]):
                if not pd.isna(df_planilha.iloc[index,coluna]):
                    if ',' in df_planilha.iloc[index,coluna]: 
                        value=int(df_planilha.iloc[index,coluna].split(',')[0] + df_planilha.iloc[index,coluna].split(',')[1])
                    elif '.' in df_planilha.iloc[index,coluna]:
                        value=int(float(df_planilha.iloc[index,coluna]))
                    else:
                        value=int(df_planilha.iloc[index,coluna])
                    print(value)
                coluna=coluna+1
            data=[[df_planilha.iloc[index,0],df_planilha.iloc[index,1],value]]
            data = pd.DataFrame(data, columns=['Ano', 'Tecnologia', 'Geração'])
            separeted_line=pd.concat([separeted_line,data])
        path = pathlib.Path(__name__).parent.resolve()
        path = str(path)
        path += "/constants/geracao_energia_ons.csv"
        with open(path, 'w') as f:
            separeted_line.to_csv(f, index=False)
        os.remove(download_folder)
    fontes = ['Biomassa','Carvão','Gás','Gás Natural','Óleo Combustível']
    caixa_tipo_usina.click()
    lista_tipo_usina = findElementsByClass('FIItem', driver)
    elFonte = searchElementList(lista_tipo_usina, 'Térmica')
    elFonte.click()
    fonte_anterior = 'All'
    for fonte in fontes:
        time.sleep(3)
        caixa_combustivel.click()
        listaCheck = findElementsByClass('facetOverflow', driver)
        checkAll = searchElementList(listaCheck, fonte_anterior)
        checkAll = findElementByCss('input[class="FICheckRadio"]', checkAll)       
        checkAll.click()
        fonte_anterior=fonte
        checkFonte = searchElementList(listaCheck, fonte)
        checkFonte = findElementByCss('input[class="FICheckRadio"]',checkFonte)
        checkFonte.click()
        botaoApply = findElementByCss('button[title="Apply"]', driver)
        botaoApply.click()
        tela = findElementByClass('tab-glass', driver)
        time.sleep(3)
        tela.click()
        fonte_anterior=fonte
        downloadCSV(driver)
        arquivo = 'Simples Geração de Energia Barra Semana.csv'
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads/", arquivo)        
        df_planilha = pd.read_csv(download_folder,encoding='utf-16', delimiter='\t', header=None)
        df_planilha = df_planilha.drop(index=[0,1,2]).reset_index(drop=True) 
        df_planilha.drop(df_planilha.iloc[:, 0:5], axis=1, inplace=True)
        df_planilha.drop(df_planilha.iloc[:, 1:3], axis=1, inplace=True)
        df_planilha.drop(df_planilha.iloc[:, 2:5], axis=1, inplace=True)
        for index, row in df_planilha.iterrows():
            coluna = 3
            while coluna<len(df_planilha.iloc[index]):
                if not pd.isna(df_planilha.iloc[index,coluna]):
                    if ',' in df_planilha.iloc[index,coluna]: 
                        value=int(df_planilha.iloc[index,coluna].split(',')[0] + df_planilha.iloc[index,coluna].split(',')[1])
                    elif '.' in df_planilha.iloc[index,coluna]:
                        value=int(float(df_planilha.iloc[index,coluna]))
                    else:
                        value=int(df_planilha.iloc[index,coluna])
                    print(value)
                coluna=coluna+1
            data=[[df_planilha.iloc[index,0],fonte,value]]
            data = pd.DataFrame(data, columns=['Ano', 'Tecnologia', 'Geração'])
            separeted_line=pd.concat([separeted_line,data])
        path = pathlib.Path(__name__).parent.resolve()
        path = str(path)
        path += "/constants/geracao_energia_ons.csv"
        with open(path, 'w') as f:
            separeted_line.to_csv(f, index=False)
        os.remove(download_folder)
    driver.close()