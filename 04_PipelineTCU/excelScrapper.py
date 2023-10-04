from bs4 import BeautifulSoup
import pathlib
import requests

class ExcelScrapper:
    
    # Uma classe para baixar os arquivos xlsx/csv disponibilizados pelas fontes de dados.

    # Atributos:
    #   file (str): nome com o qual salvaremos o arquivo
    #   link (str): link com o qual vamos baixar o arquivo

    # Métodos:
    #     def getFile(self, sub_path):
    #         Baixa o arquivo especificado e salva na pasta escolhida
    
    def __init__(self, name_left, year, name_right, url_site, url_final, file):
        # Construtor da classe excelScrapper.

        # Args:
        #     name_left (str): Parte esquerda do nome do arquivo declarado na página que vem antes do ano.
        #     year (str): Ano do novo arquivo.
        #     name_right (str): Parte direita do nome do arquivo declarado na página que vem depois do ano.
        #     url_site (str): URL do site que possui o link para baixar o arquivo desejado.
        #     url_final (str): Metade esquerda do link que iremos usar para baixar o arquivo desejado.
        #     file (str): Nome com o qual salvaremos o arquivo.
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'
        }
        try:
            self.file = file
            soup = BeautifulSoup(requests.get(url_site, headers=headers).content, 'html.parser')
            a = None
            for tag in soup.select('a'):
                html = str(tag.encode_contents(), encoding='utf-8').replace('\n', '')
                if html.find(year) != -1:
                    if html.find(name_left) != -1:
                        if html.find(name_right) != -1:
                            a = tag
            self.link = url_final + a['href']
        except Exception:
            self.link = None

    def getFile(self, sub_path):
        # Baixa o arquivo especificado e salva na pasta escolhida

        #Args:
        #    sub_path (str): Caminho no qual o arquio será salvo dentro da pasta pai.

        # Retorna: bool: Verdadeiro se a operação foi bem-sucedida, Falso
        # caso contrário.
        try:
            r = requests.get(self.link, allow_redirects=True)
            output = open(self.file, 'wb')
            output.write(r.content)
            output.close()
            path = str(pathlib.Path(__file__).parent.resolve())
            path_dir = path[0:-14]
            pathlib.Path(path_dir + self.file).rename(path + sub_path + self.file)
            return True
        except Exception as e:
            print(e)
            return False

        
