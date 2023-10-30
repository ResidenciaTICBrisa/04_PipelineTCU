import pathlib
from ..handlers.anuarioHandler import AnuarioHandler
from ..scrappers.excelScrapper import ExcelScrapper

file = 'Anuario.xlsx'


def test_getAnuario2023():
    """
    Testa o código para verificar se o Anuário correspondente ao ano de 2023 é baixado

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_raiz = path_dir[0:-7]
    path_const_input = path_consts + 'Teste Anuario Estatistico Energia Eletrica Input/'
    name_left = 'Anuário'
    name_right = 'Workbook'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica'
    url_final = 'https://www.epe.gov.br'
    scrapper = ExcelScrapper(name_left, "2023", name_right, url_site, url_final, file, path_raiz, path_const_input)
    assert scrapper.getFile()


def test_getTablesAnuario2023():
    """
    Testa o código para verificar se o o código consegue retirar todas as tabelas desejadas desse ano

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Anuario Estatistico Energia Eletrica Input/'
    path_const_output = path_consts + 'Teste Anuario Estatistico Energia Eletrica Output/'
    anuario = AnuarioHandler(file, path_const_input, path_const_output)
    assert anuario.generateTables()


def test_Links2023Iguais():
    """
    Testa se o link obtido é igual ao do ano de 2023

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_raiz = path_dir[0:-7]
    path_const_input = path_consts + 'Teste Anuario Estatistico Energia Eletrica Input/'
    name_left = 'Anuário'
    name_right = 'Workbook'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica'
    url_final = 'https://www.epe.gov.br'
    scrapper = ExcelScrapper(name_left, "2023", name_right, url_site, url_final, file, path_raiz, path_const_input)
    assert scrapper.getLink() == "https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-160/topico-168/anuario-workbook.xlsx"


def test_getAnuarioAnoNaoExiste():
    """
    Testa o código para verificar o que acontece caso seja fornecido um ano que não possui Anuário

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """

    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_raiz = path_dir[0:-7]
    path_const_input = path_consts + 'Teste Anuario Estatistico Energia Eletrica Input/'
    name_left = 'Anuário'
    name_right = 'Workbook'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/anuario-estatistico-de-energia-eletrica'
    url_final = 'https://www.epe.gov.br'
    scrapper = ExcelScrapper(name_left, "2000", name_right, url_site, url_final, file, path_raiz, path_const_input)
    assert not scrapper.getFile()
