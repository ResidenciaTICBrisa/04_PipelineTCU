import os
import pathlib
import requests
from requests_html import HTMLSession


class ExcelScrapperAnuarioANP:
    """
    Uma classe para baixar os arquivos csv disponibilizados pelo Anuário Estatístico da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis.

    Atributos:
        links (set): links com os quais vamos baixar os arquivos
        path_raiz (str): Caminho até o diretório raiz da aplicação
        path_dest (str): Caminho até onde os arquivos serão salvos

    Métodos:
        def getLinks(self):
            Método que retorna o conjunto de links da página
        def getFiles(self, tab_nomes):
            Baixa os arquivo especificados e salva na pasta escolhida
    """
    def __init__(self, url_site, path_raiz, path_dest):
        """
        Construtor da classe ExcelScrapperAnuarioANP

        Args:
            url_site (str): URL do site que possui o link para baixar o arquivo desejado.
            path_raiz (str): Caminho até o diretório raiz da aplicação
            path_dest (str): Caminho até onde os arquivos serão salvos
        """
        self.path_raiz = path_raiz
        self.path_dest = path_dest
        os.makedirs(self.path_dest, exist_ok=True)
        session = HTMLSession()
        r = session.get(url_site)
        self.links = r.html.links

    def getLinks(self):
        """
        Método que retorna o conjunto de links da página

        Retorna: set
        """

        return self.links

    def getFiles(self, tab_nomes):
        """
        Baixa os arquivos especificados e salva na pasta escolhida

        Args:
            tab_nomes (list[str]): lista com os nomes das tabelas que devem ser baixadas.
        Retorna: bool: Verdadeiro se todos os arquivos desejados foram baixados, Falso caso contrário.
        """

        n_tabelas = 0
        for link in self.links:
            for nome in tab_nomes:
                if str(link).find(nome) != -1:
                    r = requests.get(link, allow_redirects=True)
                    with open(nome, 'wb') as output:
                        output.write(r.content)
                    pathlib.Path(self.path_raiz + nome).rename(self.path_dest + nome)
                    n_tabelas += 1
                    break
        return n_tabelas == len(tab_nomes)
