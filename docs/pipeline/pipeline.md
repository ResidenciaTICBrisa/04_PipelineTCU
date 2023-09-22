# Pipeline

## Arquitetura
Na engenharia de software e na automação de processos, um pipeline refere-se a um conjunto de tarefas automatizadas que são executadas sequencialmente para processar, transformar ou mover dados de uma etapa para outra. Cada etapa desse pipeline pode ser responsável por uma parte específica do processo.

<p align="center">
    <img src="https://github.com/ResidenciaTICBrisa/04_PipelineTCU/assets/51385738/cb17934a-e8f9-4a98-a4a3-7fe0921b780c" width="1000">
</p>
</p>
<center> <figcaption>Figura 1: Arquitetura geral</figcaption> </center>
<br>

## Pipeline

<p align="center">
    <img src="https://github.com/ResidenciaTICBrisa/04_PipelineTCU/assets/51385738/7ce6dd6e-9173-4e62-bff9-328794ddfa6c" width="1000">
</p>
<center> <figcaption>Figura 2: Pipeline de processamento</figcaption> </center>


## Extração
Dados brutos são frequentemente encontrados em arquivos no formato XLSX. Esses arquivos, também conhecidos como planilhas do Microsoft Excel, são uma das formas mais comuns de armazenar informações em formato tabular.

Nesta etapa, os dados brutos relacionados ao setor energético brasileiro são coletados de fontes de dados no formato XLSX. Esses arquivos podem conter informações como produção de energia, consumo, fontes de energia, emissões de carbono, entre outros. A extração é realizada a partir desses arquivos e os dados são obtidos para análise.

## Transformação
Após a extração, os dados brutos precisam ser limpos e preparados para análise. Isso envolve várias tarefas, como:

#### Formatação dos dados: 
Garantir que os dados estejam em um formato  consistente e coerente, como datas no mesmo padrão, valores numéricos com a mesma precisão, etc.
#### Seleção de tabelas relevantes: 
Identificar quais partes dos dados são pertinentes para a análise da transição energética até 2050 e descartar informações irrelevantes.
#### Transformação de tipos de dados: 
Converter os tipos de dados, se necessário, para que sejam compatíveis com o banco de dados do SQL Server. Por exemplo, converter datas para o formato apropriado.

## Carregamento
Com os dados limpos e transformados, eles são carregados no banco de dados do SQL Server. Isso envolve a inserção dos dados nas tabelas apropriadas do banco de dados, garantindo que a estrutura das tabelas corresponda aos dados transformados.

## Visualização
Após o carregamento dos dados no banco de dados, eles estão prontos para serem visualizados e analisados. Para isso, os dados são conectados a um painel de visualização, como o Power BI. Nesse painel, é possível criar gráficos, tabelas e outros elementos visuais que permitem aos usuários entender e explorar os dados relacionados à transição energética do Brasil até 2050.