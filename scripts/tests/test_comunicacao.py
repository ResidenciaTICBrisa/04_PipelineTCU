import pathlib
from ..handlers.comunicacaoHandler import ComunicacaoHandler
from ..scrappers.excelScrapperByHref import ExcelScrapperByHref


def teste_getComunicacao_linkErrado():
    """
    Testa se o código detecta um erro caso o link esteja errado

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_raiz = path_dir[0:-7]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Comunicacao Nacional Input/'
    name_left = 'EmissoesGEE'
    url_site = 'https://www.go.br/mcti/pt-br/acompanhe-o-mcti/indicadores/paginas/dados-abertos/Errado'
    file = 'ComunicacaoNacional.xlsx'
    scrapper = ExcelScrapperByHref(name_left, url_site, file, path_raiz, path_const_input)
    assert not scrapper.getFile()


def teste_generateTable_caminhoErrado():
    """
    Testa se o código detecta um erro caso seja fornecido um path errado para o arquivo de origem

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Comunicacao Nacional Errado/'
    path_const_output = path_consts + 'Teste Comunicacao Nacional Output/'
    file = 'ComunicacaoNacional.xlsx'
    comunicacao = ComunicacaoHandler(file, path_const_input, path_const_output)
    assert not comunicacao.generateTable()


def teste_getComunicacao():
    """
    Testa se o código pega o arquivo da Comunicação Nacional e baixa ele

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_raiz = path_dir[0:-7]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Comunicacao Nacional Input/'
    name_left = 'EmissoesGEE'
    url_site = 'https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/indicadores/paginas/dados-abertos/dados-abertos-mctic/sirene-sistema-de-registro-nacional-de-emissoes'
    file = 'ComunicacaoNacional.xlsx'
    scrapper = ExcelScrapperByHref(name_left, url_site, file, path_raiz, path_const_input)
    assert scrapper.getFile()


def teste_linkExiste():
    """
    Testa se o link obtido não é None

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_raiz = path_dir[0:-7]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Comunicacao Nacional Input/'
    name_left = 'EmissoesGEE'
    url_site = 'https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/indicadores/paginas/dados-abertos/dados-abertos-mctic/sirene-sistema-de-registro-nacional-de-emissoes'
    file = 'ComunicacaoNacional.xlsx'
    scrapper = ExcelScrapperByHref(name_left, url_site, file, path_raiz, path_const_input)
    assert scrapper.getLink() is not None


def teste_generateTable():
    """
    Testa se o código gera a tabela tratada do arquivo original

    Retorna:
        assert (bool): O método retorna o resultado da comparação.
    """
    path_dir = str(pathlib.Path(__file__).parent.resolve())
    path_dir = path_dir[0:-6]
    path_consts = path_dir + '/constants/'
    path_const_input = path_consts + 'Teste Comunicacao Nacional Input/'
    path_const_output = path_consts + 'Teste Comunicacao Nacional Output/'
    file = 'ComunicacaoNacional.xlsx'
    comunicacao = ComunicacaoHandler(file, path_const_input, path_const_output)
    assert comunicacao.generateTable()
