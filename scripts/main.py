from anuarioHandler import AnuarioHandler
from benHandler import BenHandler
from comunicacaoHandler import ComunicacaoHandler
from datetime import datetime
from excelScrapper import ExcelScrapper
from excelScrapperByHref import ExcelScrapperByHref
import pathlib
from pcbioHandler import PCBIOHandler
from pneHandler import PNEHandler
from zipScrapper import ZipScrapper
from ieaHandler import IeaHandler
from Scrappers.excelScrapperIEA import ExcelScrapperIEA

if __name__ == '__main__':
    year_atual = datetime.now().year
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_consts = path_dir + '/constants/'
    path_raiz = path_dir[0:-8]
    name_left = 'Anuário'
    year = year_atual
    name_right = 'Workbook'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica'
    url_final = 'https://www.epe.gov.br'
    file = 'Anuario.xlsx'
    cont = 0
    while(cont < 10):
        scrapper = ExcelScrapper(name_left, str(year), name_right, url_site, url_final, file, path_raiz, path_consts)
        if scrapper.link != None:
            if scrapper.getFile():
                anuario = AnuarioHandler(file, path_consts)
                anuario.generateTables()
                break
        year -= 1
        cont += 1
    name_left = 'Matrizes Consolidadas'
    year = year_atual
    name_right = ''
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/BEN-Series-Historicas-Completas'
    file = 'BEN.xlsx'
    cont = 0
    while(cont < 10):
        scrapper = ExcelScrapper(name_left, str(year), name_right, url_site, url_final, file, path_raiz, path_consts)
        if scrapper.link != None:
            if scrapper.getFile():
                ben = BenHandler(file, path_consts)
                ben.generateTable()
                break
        year -= 1
        cont += 1
    name_left = 'Relatórios de saída'
    name_right = ''
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/Plano-Nacional-de-Energia-2050'
    scrapper = ZipScrapper(name_left, name_right, url_site, url_final, path_consts + 'Dados_saida_eletricidade/')
    if scrapper.link != None:
        if scrapper.getFile():
            pne = PNEHandler(path_consts + 'Dados_saida_eletricidade/', path_consts + 'Cenarios_PNE/')
            pne.generaterTables()
    name_left = 'EmissoesGEE'
    url_site = 'https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/indicadores/paginas/dados-abertos/dados-abertos-mctic/sirene-sistema-de-registro-nacional-de-emissoes'
    file = 'ComunicacaoNacional.xlsx'
    scrapper = ExcelScrapperByHref(name_left, url_site, file, path_raiz, path_consts)
    if scrapper.link != None:
        if scrapper.getFile():
            comunicacao = ComunicacaoHandler(file, path_consts, path_consts)
            comunicacao.generateTable()
    name_left = 'PCBIO'
    year = year_atual
    url_site = 'https://www.ccee.org.br/web/guest/pre%C3%A7o-m%C3%A9dio-de-descarboniza%C3%A7%C3%A3o-informa%C3%A7%C3%B5es'
    url_final = 'https://www.ccee.org.br'
    file = 'PCBIO.xlsx'
    cont = 0
    while(cont < 10):
        scrapper = ExcelScrapperByHref(name_left, url_site, file, path_raiz, path_consts, str(year), url_final)
        if scrapper.link != None:
            if scrapper.getFile():
                pcbio = PCBIOHandler(file, path_consts, path_consts)
                pcbio.generateTable()
                break
        year -= 1
        cont += 1

    '''
    Extração arquivo IEA
    '''
    url_site = "https://www.iea.org/data-and-statistics/data-product/world-energy-statistics-and-balances"
    scrapperIea = ExcelScrapperIEA(url_site, path_raiz)
    nome_arquivo = scrapperIea.baixa_arquivo()
    ieaHandler = IeaHandler(file=nome_arquivo)
    ieaHandler.formatar_xlsx_IEA()