from anuarioHandler import AnuarioHandler
from benHandler import BenHandler
from datetime import datetime
from excelScrapper import ExcelScrapper
import pathlib
from pneHandler import PNEHandler
from zipScrapper import ZipScrapper

if __name__ == '__main__':
    # year_atual = datetime.now().year
    path_dir = str(pathlib.Path(__file__).parent.resolve()) 
    path_consts = path_dir + '/constants/'
    path_raiz = path_dir[0:-14] 
    # name_left = 'Anuário'
    # year = year_atual
    # name_right = 'Workbook'
    # url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica'
    url_final = 'https://www.epe.gov.br'
    # file = 'Anuario.xlsx'
    # cont = 0
    # while(cont < 10):
    #     scrapper = ExcelScrapper(name_left, str(year), name_right, url_site, url_final, file, path_raiz, path_consts)
    #     if scrapper.link != None:
    #         if scrapper.getFile():
    #             anuario = AnuarioHandler(file, path_consts)
    #             anuario.generateTables()
    #             break
    #     year -= 1
    #     cont += 1

    # name_left = 'Matrizes Consolidadas'
    # year = year_atual
    # name_right = ''
    # url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/BEN-Series-Historicas-Completas'
    # file = 'BEN.xlsx'
    # cont = 0
    # while(cont < 10):
    #     scrapper = ExcelScrapper(name_left, str(year), name_right, url_site, url_final, file, path_raiz, path_consts)
    #     if scrapper.link != None:
    #         if scrapper.getFile(): 
    #             ben = BenHandler(file, path_consts)
    #             ben.generateTable()
    #             break
    #     year -= 1
    #     cont += 1
    name_left = 'Relatórios de saída'
    name_right = ''
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/Plano-Nacional-de-Energia-2050'
    scrapper = ZipScrapper(name_left, name_right, url_site, url_final, path_consts + 'Dados_saida_eletricidade/')
    if scrapper.link != None:
        if scrapper.getFile(): 
            pne = PNEHandler(path_consts + 'Dados_saida_eletricidade/', path_consts + 'Cenarios_PNE/')
            pne.generaterTables()
