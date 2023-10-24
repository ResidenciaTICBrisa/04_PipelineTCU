from bs4 import BeautifulSoup
import pathlib
import requests

class ExcelScrapperByHref:
    
    # Uma classe para baixar os arquivos xlsx/csv disponibilizados pelas fontes de dados só que quando já sabemos um texto contido dentro do href da tag procurada e quando a tag fornece um link completo.

    # Atributos:
    #   file (str): nome com o qual salvaremos o arquivo
    #   link (str): link com o qual vamos baixar o arquivo

    # Métodos:
    #     def getFile(self, sub_path):
    #         Baixa o arquivo especificado e salva na pasta escolhida
    
    def __init__(self, name, url_site, file, path_raiz, path_dest, year='', url_final=''):
        # Construtor da classe excelScrapper.

        # Args:
        #     name (str): Parte do nome do arquivo que estamos procurando.
        #     year (str): Ano do arquivo, caso precise
        #     url_site (str): URL do site que possui o link para baixar o arquivo desejado.
        #     file (str): Nome com o qual salvaremos o arquivo.
        #     path_raiz (str): Caminho até o diretório raiz da aplicação
        #     path_dest (str): Caminho até onde os arquivos serão salvos
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'
        }
        try:
            self.file = file
            self.path_raiz = path_raiz 
            self.path_dest = path_dest
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

    def getFile(self):
        # Baixa o arquivo especificado e salva na pasta escolhida

        # Retorna: Verdadeiro se a operação foi bem-sucedida, Falso caso contrário.
        try:
            r = requests.get(self.link, allow_redirects=True)
            output = open(self.file, 'wb')
            output.write(r.content)
            output.close()
            pathlib.Path(self.path_raiz + self.file).rename(self.path_dest + self.file)
            return True
        except Exception:
            return False