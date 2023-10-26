from bs4 import BeautifulSoup
from io import BytesIO
import os
import requests
import zipfile

class ZipScrapper:
    
    # Uma classe para baixar os arquivos zip disponibilizados pelas fontes de dados.

    # Atributos:
    #   file (str): nome com o qual salvaremos o arquivo
    #   link (str): link com o qual vamos baixar o arquivo

    # Métodos:
    #     def getFile(self, sub_path):
    #         Baixa o arquivo especificado e salva na pasta escolhida
    
    def __init__(self, name_left, name_right, url_site, url_final, path_dest):
        # Construtor da classe ZipScrapper.

        # Args:
        #     name_left (str): Parte esquerda do nome do arquivo declarado na página que vem antes do ano.
        #     name_right (str): Parte direita do nome do arquivo declarado na página que vem depois do ano.
        #     url_site (str): URL do site que possui o link para baixar o arquivo desejado.
        #     url_final (str): Metade esquerda do link que iremos usar para baixar o arquivo desejado.
        #     path_dest (str): Caminho até onde os arquivos serão salvos
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'
        }
        try:
            self.path_dest = path_dest
            soup = BeautifulSoup(requests.get(url_site, headers=headers).content, 'html.parser')
            a = None
            for tag in soup.select('a'):
                html = str(tag.encode_contents(), encoding='utf-8').replace('\n', '')
                if html.find(name_left) != -1:
                    if html.find(name_right) != -1:
                        a = tag
            self.link = url_final + a['href']
        except Exception:
            self.link = None

    def getFile(self):
        # Baixa o arquivo especificado e salva na pasta escolhida

        # Retorna: bool: Verdadeiro se a operação foi bem-sucedida, Falso
        # caso contrário.
        try:
            os.makedirs(self.path_dest, exist_ok=True)
            # url = "https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-227/topico-563/Dados_saida_eletricidade.zip" 
            filebytes = BytesIO(
                requests.get(self.link).content
            )
            zip = zipfile.ZipFile(filebytes)
            zip.extractall(self.path_dest)
            return True
        except Exception:
            return False