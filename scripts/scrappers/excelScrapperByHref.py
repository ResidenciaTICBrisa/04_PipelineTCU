import os
import pathlib
from bs4 import BeautifulSoup
import requests


class ExcelScrapperByHref:
    """
    Uma classe para baixar os arquivos xlsx/csv disponibilizados pelas fontes de dados só que quando já temos certeza de um texto contido dentro do href da tag procurada e quando a tag fornece um link completo.

    Atributos:
        file (str): nome com o qual salvaremos o arquivo
        link (str): link com o qual vamos baixar o arquivo
        path_raiz (str): Caminho até o diretório da raiz da aplicação onde será baixado o arquivo direto da internet
        path_dest (str): Caminho para onde se desejar enviar o arquivo

    Métodos:
        def getFile(self, sub_path):
            Baixa o arquivo especificado e salva na pasta escolhida
        def getLink(self):
            Método que retorna o atributo link do objeto
    """

    def __init__(self, name, url_site, file, path_raiz, path_dest, year='', url_final=''):
        """
        Construtor da classe ExcelScrapperByHref.

        Args:
            name (str): Parte do nome do arquivo que estamos procurando.
            url_site (str): URL do site que possui o link para baixar o arquivo desejado.
            file (str): Nome com o qual salvaremos o arquivo.
            path_raiz (str): Caminho até o diretório da raiz da aplicação onde será baixado o arquivo direto da internet
            path_dest (str): Caminho para onde se desejar enviar o arquivo
            year (str): Ano do arquivo, caso precise
            url_final (str): URL que precisa ser concatenada ao href da tag procurada caso ela não venha completa
        """

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'
        }
        try:
            self.file = file
            self.path_raiz = path_raiz
            self.path_dest = path_dest
            os.makedirs(self.path_dest, exist_ok=True)
            soup = BeautifulSoup(requests.get(url_site, headers=headers).content, 'html.parser')
            a = None
            for tag in soup.select('a'):
                if str(tag['href']).find(name) != -1:
                    if str(tag['href']).find(year) != -1:
                        a = tag
                        break
            self.link = url_final + str(a['href'])
        except Exception:
            self.link = None

    def getLink(self):
        """
        Método que retorna o atributo link do objeto

        Retorna: str|None
        """
        return self.link

    def getFile(self):
        """
        Baixa o arquivo especificado e salva na pasta escolhida

        Retorna: Verdadeiro se a operação foi bem-sucedida, Falso caso contrário.
        """
        try:
            r = requests.get(self.link, allow_redirects=True)
            with open(self.file, 'wb') as output:
                output.write(r.content)
            pathlib.Path(self.path_raiz + self.file).rename(self.path_dest + self.file)
            return True
        except Exception:
            return False
