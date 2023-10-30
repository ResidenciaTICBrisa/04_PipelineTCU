import pathlib
from ..handlers.pneHandler import PNEHandler
from ..scrappers.zipScrapper import ZipScrapper


def teste_get_PNE_link_errado():
    """
    Testa se o código retorna o erro caso o link para o site esteja errado

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    url_final = 'https://www.epe.gov.br'
    path_const_input = path_consts + 'Teste PNE 2050 Input/'
    name_left = 'Relatórios de saída'
    url_site = 'https://www.epe.gov.b'
    scrapper = ZipScrapper(name_left, url_site, url_final, path_const_input)
    assert not scrapper.getFile()


def teste_generateTables_pathErrado():
    """
    Testa se o código detecta um erro caso seja passado o caminho de um arquivo que não existe

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste PNE Nao Existe/'
    path_const_output = path_consts + 'Teste PNE 2050 Output/'
    pne = PNEHandler(path_const_input, path_const_output)
    assert not pne.generaterTables()


def teste_getPNE():
    """
    Testa se o código pega o arquivo dos dados de saída do PNE 2050

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    url_final = 'https://www.epe.gov.br'
    path_const_input = path_consts + 'Teste PNE 2050 Input/'
    name_left = 'Relatórios de saída'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/Plano-Nacional-de-Energia-2050'
    scrapper = ZipScrapper(name_left, url_site, url_final, path_const_input)
    assert scrapper.getFile()


def teste_getLink():
    """
    Testa se o código pega o link do arquivo dos dados de saída do PNE 2050

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    url_final = 'https://www.epe.gov.br'
    path_const_input = path_consts + 'Teste PNE 2050 Input/'
    name_left = 'Relatórios de saída'
    url_site = 'https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/Plano-Nacional-de-Energia-2050'
    scrapper = ZipScrapper(name_left, url_site, url_final, path_const_input)
    assert scrapper.getLink() is not None


def teste_generateTables():
    """
    Testa se o código gera as tabelas desejadas

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste PNE 2050 Input/'
    path_const_output = path_consts + 'Teste PNE 2050 Output/'
    pne = PNEHandler(path_const_input, path_const_output)
    assert pne.generaterTables()
