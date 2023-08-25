import pandas as pd
import sys
import os
from pathlib import Path


file_path = './constants/Capacidade_Instalada_Matriz_Eletrica_BR_ONS.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Preencher valores ausentes na coluna de 2022 com 0
df['MW'] = df['MW'].fillna(0)

# Arredondar todos os valores para inteiros
df['MW'] = df['MW'].round(0).astype(int)

# Criar uma tabela dinâmica usando pivot_table
pivot_df = df.pivot_table(index='Ano_referencia', columns='Fonte', values='MW', aggfunc='sum')

# Reorganizar as colunas para ter o cabeçalho desejado
desired_order = ['Eólica', 'Térmica', 'Hidráulica', 'Nuclear', 'Solar', 'MMGD']
pivot_df = pivot_df[desired_order]

# Resetar o índice para trazer a coluna 'Ano_referencia' de volta para os dados
pivot_df = pivot_df.reset_index()

# Salvar a tabela dinâmica em um novo arquivo CSV com formatação UTF-8
path = str(Path(__file__).parent.resolve()) 
path += "/constants/"
output_file_path = 'caminho_para_o_novo_arquivo.csv'
pivot_df.to_csv(path + "Capacidade_Instalada_Matriz_Eletrica_BR_ONS_formatado.csv", index=None)

print("Tabela dinâmica salva como CSV:")
print(output_file_path)