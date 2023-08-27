from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
from pathlib import Path

driver = webdriver.Chrome()

def findElementsByClass(cl, d):
    return d.find_elements(By.CLASS_NAME, value=cl)

def findElementByCss(css, d):
    return d.find_element(By.CSS_SELECTOR, value=css)

def findElementsByCss(css, d):
    return d.find_elements(By.CSS_SELECTOR, value=css)

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
    driver.get('https://tableau.ons.org.br/t/ONS_Publico/views/MatrizdeEnergiaEltrica/PainelCapacidadeInstaladaTotal?%3Aembed_code_version=3&%3Aembed=y&%3AloadOrderID=0&%3Adisplay_spinner=no&%3AshowAppBanner=false&%3Adisplay_count=n&%3AshowVizHome=n&%3Aorigin=viz_share_link')
    arquivo = 'Total Disponível Tipo Usinas - Anual.csv'
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads/", arquivo)
    df_final = pd.DataFrame()
    downloadCSV()
    new_lines = []
    with open(download_folder, 'r', encoding='utf-16') as file:
        for l in file.readlines():
            if l != '\n':
                n = l.replace(',', '')
                new_lines.append(n)
    with open(download_folder, 'w', encoding='utf-16') as file:
        file.writelines(new_lines)
    df_planilha = pd.read_csv(download_folder,encoding='utf-16', delimiter='\t')
    df_planilha.drop(df_planilha.iloc[:, -1:], axis=1, inplace=True)
    df_planilha.drop(df_planilha.iloc[:, -2:-1], axis=1, inplace=True)
    df_final = pd.concat([df_final, df_planilha])
    os.remove(download_folder)
    dropdowns = findElementsByClass("CategoricalFilterBox", driver)
    ano_referencia = searchElementList(dropdowns, 'Ano de Referência')
    drop_ano_referencia = findElementByCss('div[class="tabComboBoxNameContainer tab-ctrl-formatted-fixedsize"]', ano_referencia)
    drop_ano_referencia.click()
    time.sleep(4)
    container_anos = findElementByCss('div[class="CFOuterContainer tabMenuComboDropdownTheme tab-ctrl-formatted-widget"]', driver)
    lista_container_anos = findElementsByCss('div[tabindex="-1"]', container_anos)
    lista_anos = []
    for container_ano in lista_container_anos:
        ano = getHTML(findElementByCss('a',container_ano))
        lista_anos.append(ano)
    for ano in lista_anos:
        container_anos = findElementByCss('div[class="CFOuterContainer tabMenuComboDropdownTheme tab-ctrl-formatted-widget"]', driver)
        lista_container_anos = findElementsByCss('div[tabindex="-1"]', container_anos)
        elAno = searchElementList(lista_container_anos, ano)
        elAno.click()
        time.sleep(8)
        downloadCSV()
        new_lines = []
        with open(download_folder, 'r', encoding='utf-16') as file:
            for l in file.readlines():
                if l != '\n':
                    n = l.replace(',', '')
                    new_lines.append(n)
        with open(download_folder, 'w', encoding='utf-16') as file:
            file.writelines(new_lines)
        df_planilha = pd.read_csv(download_folder,encoding='utf-16', delimiter='\t')
        df_planilha.drop(df_planilha.iloc[:, -1:], axis=1, inplace=True)
        df_planilha.drop(df_planilha.iloc[:, -2:-1], axis=1, inplace=True)
        df_final = pd.concat([df_final, df_planilha])
        os.remove(download_folder)
        dropdowns = findElementsByClass("CategoricalFilterBox", driver)
        ano_referencia = searchElementList(dropdowns, 'Ano de Referência')
        drop_ano_referencia = findElementByCss('div[class="tabComboBoxNameContainer tab-ctrl-formatted-fixedsize"]', ano_referencia)
        drop_ano_referencia.click()
        time.sleep(8)
    file_path = './constants/Capacidade_Instalada_Matriz_Eletrica_BR_ONS.csv'

    # Preencher valores ausentes na coluna de 2022 com 0
    df_final['MW'] = df_final['MW'].fillna(0)

    # Arredondar todos os valores para inteiros
    #df['MW'] = df['MW'].round(0).astype(int)

    # Criar uma tabela dinâmica usando pivot_table
    pivot_df = df_final.pivot_table(index='Ano_referencia', columns='Fonte', values='MW', aggfunc='sum')

    # Reorganizar as colunas para ter o cabeçalho desejado
    desired_order = ['Eólica', 'Térmica', 'Hidráulica', 'Nuclear', 'Solar', 'MMGD']
    pivot_df = pivot_df[desired_order]

    # Resetar o índice para trazer a coluna 'Ano_referencia' de volta para os dados
    pivot_df = pivot_df.reset_index()

    path = str(Path(__file__).parent.resolve()) 
    path += "/constants/" 
    pivot_df.to_csv(path + "Capacidade_Instalada_Matriz_Eletrica_BR_ONS.csv", index=None)  
    driver.close()