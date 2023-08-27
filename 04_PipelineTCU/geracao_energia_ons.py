from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
import pytest
import pathlib

from selenium.webdriver.common.keys import Keys
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
    time.sleep(5)
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
    time.sleep(15)

    #Mudando o escopo para "(All)"
    caixa_escopo.click()
    lista_escopo = findElementsByClass('FIItem', driver)
    time.sleep(5)
    escopo_all = searchElementList(lista_escopo, '(All)')
    escopo_all.click()
    time.sleep(10)
    #Mudando periodo de tempo de 1998 até 2030
    XpathPeriodo1998 = '//*[@id="typein_[Parameters].[Início Primeiro Período GE Comp 3 (cópia)]"]/span[1]/input'
    inputPeriodo1998=findElementByXpath(XpathPeriodo1998,driver)
    inputPeriodo1998.click()
    inputPeriodo1998.send_keys('01/01/1999')
    inputPeriodo1998.send_keys(Keys.RETURN)
    time.sleep(10)
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
        caixa_tipo_usina.click()
        time.sleep(5)
        lista_tipo_usina = findElementsByClass('FIItem', driver)
        time.sleep(5)
        elFonte = searchElementList(lista_tipo_usina, fonte)
        elFonte.click()
        time.sleep(10)
        downloadCSV()
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
    fontes = ['Biomassa','Carvão','Gás','Gás Natural','Óleo Combustível','Oléo Diesel','Outras Multi-Combustível','Resíduos Industriais']
    caixa_tipo_usina.click()
    time.sleep(5)
    lista_tipo_usina = findElementsByClass('FIItem', driver)
    time.sleep(5)
    elFonte = searchElementList(lista_tipo_usina, 'Térmica')
    elFonte.click()
    time.sleep(5)
    fonte_anterior = 'All'
    for fonte in fontes:
        caixa_combustivel.click()
        time.sleep(5)
        listaCheck = findElementsByClass('facetOverflow', driver)
        checkAll = searchElementList(listaCheck, fonte_anterior)
        checkAll = findElementByCss('input[class="FICheckRadio"]', checkAll)       
        checkAll.click()
        fonte_anterior=fonte
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
        fonte_anterior=fonte
        downloadCSV()
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