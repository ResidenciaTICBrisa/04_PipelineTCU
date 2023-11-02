import os
import pathlib
from bs4 import BeautifulSoup
import requests


class ExcelScrapper:
    """
    Uma classe para baixar os arquivos xlsx/csv disponibilizados pelas fontes de dados.

    Atributos:
        file (str): Nome com o qual salvaremos o arquivo
        link (str): Link com o qual vamos baixar o arquivo
        path_raiz (str): Caminho até o diretório da raiz da aplicação onde será baixado o arquivo direto da internet
        path_dest (str): Caminho para onde se desejar enviar o arquivo

    Métodos:
        def getLink(self):
            Método que retorna o atributo link do objeto
        def setLink(self, link):
            Método que define um valor para o atributo link
        def getFile(self, sub_path):
            Baixa o arquivo especificado e salva na pasta escolhida
    """

    def __init__(self, name_left, year, name_right, url_site, url_final, file, path_raiz, path_dest):
        """
        Construtor da classe excelScrapper.

        Args:
            name_left (str): Parte esquerda do nome do arquivo declarado na página que vem antes do ano.
            year (str): Ano do novo arquivo.
            name_right (str): Parte direita do nome do arquivo declarado na página que vem depois do ano.
            url_site (str): URL do site que possui o link para baixar o arquivo desejado.
            url_final (str): Metade esquerda do link que iremos usar para baixar o arquivo desejado.
            file (str): Nome com o qual salvaremos o arquivo.
            path_raiz (str): Caminho até o diretório da raiz da aplicação onde será baixado o arquivo direto da internet
            path_dest (str): Caminho para onde se desejar enviar o arquivo
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
                html = str(tag.encode_contents(), encoding='utf-8').replace('\n', '')
                if html.find(year) != -1:
                    if html.find(name_left) != -1:
                        if html.find(name_right) != -1:
                            a = tag
                            break
            self.link = url_final + a['href']
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

        Retorna: bool: Verdadeiro se a operação foi bem-sucedida, Falso caso contrário.
        """
        try:
            r = requests.get(self.link, allow_redirects=True)
            with open(self.file, 'wb') as output:
                output.write(r.content)
            pathlib.Path(self.path_raiz + self.file).rename(self.path_dest + self.file)
            return True
        except Exception:
            return False
