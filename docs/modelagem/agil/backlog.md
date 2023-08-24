# Backlog do Produto

## Introdução

O backlog do produto é uma lista dinâmica e priorizada de todas as funcionalidades, requisitos, melhorias e correções que precisam ser desenvolvidas em um projeto. Ele serve como um repositório central de todas as necessidades e demandas dos usuários, stakeholders e equipe de desenvolvimento.

Essa lista é organizada em ordem de prioridade, com os itens mais importantes ou de maior valor estratégico no topo. O backlog do produto evolui ao longo do tempo, à medida que novas informações são obtidas, prioridades mudam e o projeto se adapta às necessidades do mercado.

## Metodologia

A metodologia do backlog do produto é uma abordagem estruturada e colaborativa para gerenciar as demandas e requisitos de um produto ou projeto de forma ágil. Ela é parte fundamental da metodologia Scrum e outras metodologias ágeis, onde o desenvolvimento é orientado por ciclos curtos de trabalho chamados sprints.

### Etapa de Pré-rastreabilidade

- [Rich Picture](../../analise/rich_picture.md)
- [Projetos Similares](../../analise/projetos_similares.md)

### Etapa de elicitação

- [Brainstorming](../../elicitacao/brainstorming.md) [Em progresso]
- [Entrevista](../../elicitacao/entrevista.md)
- [Personas](../../elicitacao/personas.md)
- [Storytelling](../../elicitacao/storytelling.md)

### Etapa de Priorização

- [MosCow](../../elicitacao/priorizacao/MoScoW.md)


## Elicitação de Requisitos

Serão apresentados todos os requisitos funcionais elicitados durante o processo de elicitação.



| Identificador |                                                   Requisito                                                   |                               Rastreabilidade                                |
| :-----------: | :-----------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------: |
|     RF01      |                                O usúario deve poder visualizar os dados de Emissões Equivalentes de CO2 do Brasil                                 |      [ST01](../../elicitacao/storytelling.md#elicitacao-de-requisitos)       |
|     RFN01      |                                           O sistema deveria exportar a dashboard em excel                                           |      [ST02](../../elicitacao/storytelling.md#elicitacao-de-requisitos)       |
|     RFN02      |                                O usuário deveria poder Visualizar a fonte de dados de cada gráfico                                 |      [ST03](../../elicitacao/storytelling.md#elicitacao-de-requisitos)       |
|     RFN03      |                                              A dashboard deveria ser compatível com dispositivos móveis                                               |      [ST04](../../elicitacao/storytelling.md#elicitacao-de-requisitos)       |
|     RF02      |                                 O sistema deve ser simples e intuitivo                                 |      [ST06](../../elicitacao/storytelling.md#elicitacao-de-requisitos)       |
|     RF03      |                                       O usúario deve poder visualizar os dados de Consumo de Gás Natural do Brasil                                      | [ST07](../../elicitacao/storytelling.md#elicitacao-de-requisitos) |
|     RF04      |                                       Ser capaz de funcionar sem internet                                         | [ST08](../../elicitacao/storytelling.md#elicitacao-de-requisitos) |
|     RF05      |                                       Visualizar os dados de Potência Acumulada do Brasil e do Mundo                                         | [ENT01](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF06      |                                       Visualizar os dados de Geração Período Médio do Brasil                                         | [ENT02](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF7      |                                       Visualizar os dados de Custo de Operação do Brasil e do Mundo                                         | [ENT03](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF8      |                                       Visualizar a fonte de dados de cada gráfico                                         | [ENT04](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF9      |                                       Filtrar os dados atualizados de empregabilidade por fonte/tecnologia                                         | [ENT06](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF10      |                                       Filtrar os dados atualizados da matriz energética do Brasil                                         | [ENT07](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF11      |                                       Filtrar uma matriz energética e verificar seu nível de emissões                                         | [ENT08](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF12      |                                       Filtrar a fonte de dados de cada gráfico                                         | [ENT09](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF13      |                                       Simular diferentes cenários de demanda, para avaliar seu impacto nas projeções de emissão                                         | [ENT10](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF14      |                                       Comparar dados de Emissões Equivalentes de CO2 do Brasil e do mundo                                         | [ENT11](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF15      |                                       Comparar dados de Custo de Operação do Brasil e do Mundo                                         | [ENT12](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF16      |                                       Comparar dados de Consumo de Gás Natural do Brasil e do Mundo                                         | [ENT13](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |
|     RF17      |                                       Comparar dados atualizados de empregabilidade                                         | [ENT14](../../elicitacao/entrevista.md#elicitacao-de-requisitos) |

## Temas

Especifica-se dois grandes temas que reunem os épicos.

- Visualização: Está relacionado à visualização geral dos indicadores da dashboard.
- Dashboard: Trata sobre as funcionalidades da dashboard em si, envolvendo sistema e funcionalidades.
## Épicos

<center>

<table>
  <tr>
    <th>Tema</th>
    <th>Épicos</th>
    <th>ID</th>
  </tr>
  <tr>
    <td style="vertical-align:middle">Visualização</td>
    <td>Visualização de dados: Todas as funcionalidades relacionadas as Visualizações de dados.</td>
    <td>EP01</td>
  </tr>

  <tr>
    <td style="vertical-align:middle" rowspan="3">Dashboard</td>
    <td>Filtrar dados: Funcionalidades relacionadas à Filtragem de dados.</td>
    <td>EP02</td>
  </tr>
  <tr>
    <td>Simular cenário: Envolve as funcionalidades relacionadas a simulação de cenários</td>
    <td>EP03</td>
    </tr>
    <tr>
    <td>Comparar cenário: Envolve as funcionalidades relacionadas a comparação de cenários</td>
    <td>EP04</td>
  </tr>
</table>

</center>



