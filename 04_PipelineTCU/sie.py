from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pathlib
from pathlib import Path
import os

driver = webdriver.Chrome()

def baixar(btn_form, btn_excel):
    driver.execute_script("arguments[0].click();", btn_form)
    driver.execute_script("arguments[0].click();", btn_excel)

if __name__ == '__main__' :    
    driver.get('https://www.mme.gov.br/SIEBRASIL/consultas/reporte-dinamico.aspx?or=30225&ss=2&v=1')
    tabela = driver.find_element(By.ID, value = 'glTiempo_DDD_gv_DXMainTable')
    seletor_ano = driver.find_element(By.ID, value='glTiempo_B-1')
    itens = tabela.find_elements(By.CLASS_NAME, value='dxgvDataRow')
    btn_rel = driver.find_element(By.ID, value = 'btnVerReporte')
    cont = 1
    seletor_ano.click()
    itens.pop(0)
    for item in itens:
        if cont == 4:
            break
        id = 'glTiempo_DDD_gv_DXSelBtn' + str(cont) + '_D'
        checkbox = item.find_element(By.ID, id)
        driver.execute_script("arguments[0].click();", checkbox)
        cont += 1
    btn_rel.click()
    time.sleep(5)
    btn_form = driver.find_element(By.ID, value='ctl00_cphPrincipal_sptReporte_tpcReporte_rvReporte_ctl06_ctl04_ctl00_Button')
    btn_excel = driver.find_element(By.XPATH, value='//*[@id="ctl00_cphPrincipal_sptReporte_tpcReporte_rvReporte_ctl06_ctl04_ctl00_Menu"]/div[1]/a')
    time.sleep(5)
    baixar(btn_form, btn_excel)
    time.sleep(5)
    driver.close()
    arquivo = "reporte_dinamico_emisiones.xlsx" 
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads/", arquivo)
    path = str(pathlib.Path(__file__).parent.resolve()) 
    path += "/constants/" + arquivo
    Path(download_folder).rename(path)