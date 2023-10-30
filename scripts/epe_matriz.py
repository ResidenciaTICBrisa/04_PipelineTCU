import os
from github import Github
import requests

# Token de acesso
github_access_token = os.getenv("PASSWORD_KEY")

if github_access_token:

    g = Github(github_access_token)

    # Configurando upload no repositório
    repo_owner = "ResidenciaTICBrisa"
    repo_name = "04_PipelineTCU"
    file_url = "https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-748/topico-678/Matriz%20ab2022.xlsx"
    file_name_in_repo = "Matriz_2022.xlsx"
    response = requests.get(file_url)

    if response.status_code == 200:
        file_content = response.content
        repo = g.get_user(repo_owner).get_repo(repo_name)

        try:
            contents = repo.get_contents(file_name_in_repo)
            repo.update_file(file_name_in_repo, "Atualizando arquivo", file_content, contents.sha)
            print(f"Arquivo '{file_name_in_repo}' atualizado com sucesso no repositório '{repo_name}'.")
        except Exception:
            repo.create_file(file_name_in_repo, "Criando arquivo", file_content)
            print(f"Arquivo '{file_name_in_repo}' criado com sucesso no repositório '{repo_name}'.")
    else:
        print("Falha ao baixar o arquivo a partir do URL.")
else:
    print("Token de acesso pessoal não encontrado. Certifique-se de configurar a secret PASSWORD_KEY em seu repositório.")
