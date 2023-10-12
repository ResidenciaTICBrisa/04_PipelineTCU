# Dicionário de Dados

## Introdução 
Um Dicionário de Dados é uma ferramenta essencial para organizar, descrever e padronizar informações relacionadas a sistemas de dados e software. Ele fornece uma visão detalhada das estruturas de dados, incluindo definições, formatos e relacionamentos, facilitando a colaboração e garantindo a qualidade e integridade dos dados em projetos de TI e gerenciamento de informações.
Nesse documento, adicionamos o dicionário relacionado as tabelas presentes no banco de dados com separação por página do dashboard.

## **Página de Capacidade Instalada**

#### **Tabela: PotAcumPNE**

|       DADO       |    NOME DO CAMPO    |  TIPO DO DADO |            DESCRIÇÃO           | RESTRIÇÃO |
|:----------------:|:-------------------:|:-------------:|:------------------------------:|:---------:|
| Fonte_Tecnologia | Fonte ou Tecnologia | NVARCHAR(50)  | Fonte ou Tecnologia da análise | NÃO NULO  |
| Ano_2015         | Ano de 2015         | FLOAT         | Quantidade no ano de 2015      | NÃO NULO  |
| Ano_2030         | Ano de 2030         | INT           | Quantidade no ano de 2030      | NÃO NULO  |
| Ano_2040         | Ano de 2040         | INT           | Quantidade no ano de 2040      | NÃO NULO  |
| Ano_2050         | Ano de 2050         | INT           | Quantidade no ano de 2050      | NÃO NULO  |
| Cenário          | Cenário do PNE      | NVARCHAR(150) | Cenário do PNE de análise      | NÃO NULO  |

## **Página de Geração Período Médio**

#### **Tabela: GerPerMedPNE**

|       DADO       |    NOME DO CAMPO    |  TIPO DO DADO |            DESCRIÇÃO           | RESTRIÇÃO |
|:----------------:|:-------------------:|:-------------:|:------------------------------:|:---------:|
| Fonte_Tecnologia | Fonte ou Tecnologia | NVARCHAR(50)  | Fonte ou Tecnologia da análise | NÃO NULO  |
| Ano_2015         | Ano de 2015         | FLOAT         | Quantidade no ano de 2015      | NÃO NULO  |
| Ano_2030         | Ano de 2030         | INT           | Quantidade no ano de 2030      | NÃO NULO  |
| Ano_2040         | Ano de 2040         | INT           | Quantidade no ano de 2040      | NÃO NULO  |
| Ano_2050         | Ano de 2050         | INT           | Quantidade no ano de 2050      | NÃO NULO  |
| Cenário          | Cenário do PNE      | NVARCHAR(150) | Cenário do PNE de análise      | NÃO NULO  |

## **Página de Balanço de Potência**

#### **Tabela: AtendPontaPNE**
|       DADO       |    NOME DO CAMPO    |  TIPO DO DADO |            DESCRIÇÃO           | RESTRIÇÃO |
|:----------------:|:-------------------:|:-------------:|:------------------------------:|:---------:|
| Fonte_Tecnologia | Fonte ou Tecnologia | NVARCHAR(50)  | Fonte ou Tecnologia da análise | NÃO NULO  |
| Ano_2015         | Ano de 2015         | FLOAT         | Quantidade no ano de 2015      | NÃO NULO  |
| Ano_2030         | Ano de 2030         | INT           | Quantidade no ano de 2030      | NÃO NULO  |
| Ano_2040         | Ano de 2040         | INT           | Quantidade no ano de 2040      | NÃO NULO  |
| Ano_2050         | Ano de 2050         | INT           | Quantidade no ano de 2050      | NÃO NULO  |
| Cenário          | Cenário do PNE      | NVARCHAR(150) | Cenário do PNE de análise      | NÃO NULO  |

#### **Tabela: DemMax(MW)**
|      DADO      |  NOME DO CAMPO | TIPO DO DADO |           DESCRIÇÃO          | RESTRIÇÃO |
|:--------------:|:--------------:|:------------:|:----------------------------:|:---------:|
| Demanda_Máxima | Demanda Máxima | INT          | Quantidade em MW de Demanda  | NÃO NULO  |
| Região         | Região         | NVARCHAR(50) | Região de análise            | NÃO NULO  |
| Ano            | Ano de análise | SMALLINT     | Ano de análise               | NÃO NULO  |

## **Página de Matriz Energética**

#### **Tabela: Matriz energética - Brasil**
|            DADO            |        NOME DO CAMPO       | TIPO DO DADO |                    DESCRIÇÃO                   | RESTRIÇÃO |
|:--------------------------:|:--------------------------:|:------------:|:----------------------------------------------:|:---------:|
| Ano                        | Ano                        | SMALLINT     | Ano de análise                                 | NÃO NULO  |
| Carvão                     | Carvão                     | INT          | Quantidade vinda do carvão                     | NÃO NULO  |
| Gás Natural                | Gás Natural                | INT          | Quantidade vinda do Gás Natural                | NÃO NULO  |
| Nuclear                    | Nuclear                    | INT          | Quantidade vinda de energia Nuclear            | NÃO NULO  |
| Hidro                      | Hidro                      | INT          | Quantidade vinda de Hidro                      | NÃO NULO  |
| Biocombustíveis e resíduos | Biocombustíveis e resíduos | INT          | Quantidade vinda de Biocombustíveis e resíduos | NÃO NULO  |
| Óleo                       | Óleo                       | INT          | Quantidade vinda de óleo                       | NÃO NULO  |
| Eólica, solar, etc.        | Eólica, solar, etc.        | INT          | Quantidade vinda de Eólica, solar, etc.        | NÃO NULO  |
| Unidades                   | Unidades                   | NVARCHAR(50) | Unidade de medida                              | NÃO NULO  |

#### **Tabela: Matriz energética - Mundo**
|            DADO            |        NOME DO CAMPO       | TIPO DO DADO |                    DESCRIÇÃO                   | RESTRIÇÃO |
|:--------------------------:|:--------------------------:|:------------:|:----------------------------------------------:|:---------:|
| Ano                        | Ano                        | SMALLINT     | Ano de análise                                 | NÃO NULO  |
| Carvão                     | Carvão                     | INT          | Quantidade vinda do carvão                     | NÃO NULO  |
| Gás Natural                | Gás Natural                | INT          | Quantidade vinda do Gás Natural                | NÃO NULO  |
| Nuclear                    | Nuclear                    | INT          | Quantidade vinda de energia Nuclear            | NÃO NULO  |
| Hidro                      | Hidro                      | INT          | Quantidade vinda de Hidro                      | NÃO NULO  |
| Biocombustíveis e resíduos | Biocombustíveis e resíduos | INT          | Quantidade vinda de Biocombustíveis e resíduos | NÃO NULO  |
| Óleo                       | Óleo                       | INT          | Quantidade vinda de óleo                       | NÃO NULO  |
| Eólica, solar, etc.        | Eólica, solar, etc.        | INT          | Quantidade vinda de Eólica, solar, etc.        | NÃO NULO  |
| Unidades                   | Unidades                   | NVARCHAR(50) | Unidade de medida                              | NÃO NULO  |

## **Página de Empregabilidade**

#### **Tabela: Empregabilidade no Brasil**
|       DADO      |  NOME DO CAMPO  | TIPO DO DADO |            DESCRIÇÃO            | RESTRIÇÃO |
|:---------------:|:---------------:|:------------:|:-------------------------------:|:---------:|
| Pais            | Pais            | NVARCHAR(50) | País de análise                 | NÃO NULO  |
| Ano             | Ano             | SMALLINT     | Ano de análise                  | NÃO NULO  |
| Tecnologia      | Tecnologia      | NVARCHAR(50) | Tecnologia de análise           | NÃO NULO  |
| Empregabilidade | Empregabilidade | SMALLINT     | Numero de empregabilidade (MIL) |           |

## **Página de Consumo Total EPE**

#### **Tabela: CT_Consumo_GWh**

|    DADO   | NOME DO CAMPO | TIPO DO DADO |         DESCRIÇÃO         | RESTRIÇÃO |
|:---------:|:-------------:|:------------:|:-------------------------:|:---------:|
| nomMes    | Nome do mês   | NVARCHAR(50) | Mês de análise            |           |
| Ano_2016  | Ano de 2016   | FLOAT        | Quantidade no ano de 2016 |           |
| Ano_2017  | Ano de 2017   | NVARCHAR(50) | Quantidade no ano de 2017 |           |
| Ano_2018  | Ano de 2018   | NVARCHAR(50) | Quantidade no ano de 2018 |           |
| Ano_2019  | Ano de 2019   | FLOAT        | Quantidade no ano de 2019 |           |
| Ano_2020  | Ano de 2020   | FLOAT        | Quantidade no ano de 2020 |           |
| Ano_2021  | Ano de 2021   | FLOAT        | Quantidade no ano de 2021 |           |
| Ano_2022  | Ano de 2022   | FLOAT        | Quantidade no ano de 2022 |           |
| Ano_2023  | Ano de 2023   | FLOAT        | Quantidade no ano de 2023 |           |

#### **Tabela: CT_Consumo_Médio_por_classe**

|    DADO   | NOME DO CAMPO | TIPO DO DADO |         DESCRIÇÃO         | RESTRIÇÃO |
|:---------:|:-------------:|:------------:|:-------------------------:|:---------:|
| nomMes    | Nome do mês   | NVARCHAR(50) | Mês de análise            |           |
| Ano_2016  | Ano de 2016   | FLOAT        | Quantidade no ano de 2016 |           |
| Ano_2017  | Ano de 2017   | NVARCHAR(50) | Quantidade no ano de 2017 |           |
| Ano_2018  | Ano de 2018   | NVARCHAR(50) | Quantidade no ano de 2018 |           |
| Ano_2019  | Ano de 2019   | FLOAT        | Quantidade no ano de 2019 |           |
| Ano_2020  | Ano de 2020   | FLOAT        | Quantidade no ano de 2020 |           |
| Ano_2021  | Ano de 2021   | FLOAT        | Quantidade no ano de 2021 |           |
| Ano_2022  | Ano de 2022   | FLOAT        | Quantidade no ano de 2022 |           |
| Ano_2023  | Ano de 2023   | FLOAT        | Quantidade no ano de 2023 |           |

#### **Tabela: CT_Consumo_acumulado_região_GWh**

|    DADO    | NOME DO CAMPO | TIPO DO DADO |       DESCRIÇÃO       | RESTRIÇÃO |
|:----------:|:-------------:|:------------:|:---------------------:|:---------:|
| nomRegiao  | Nome Região   | NVARCHAR(50) | Região de análise     |           |
| ValorTotal | Valor Total   | FLOAT        | Quantidade de consumo |           |

## **Página BEN**

#### **Tabela: BEN_total**
|             DADO             |         NOME DO CAMPO        | TIPO DO DADO |                  DESCRIÇÃO                 | RESTRIÇÃO |
|:----------------------------:|:----------------------------:|:------------:|:------------------------------------------:|:---------:|
| CONTA                        | Conta                        | NVARCHAR(50) | Ramo analisado                             | NÃO NULO  |
| PRODUÇÃO                     | Produção                     | INT          | Quantidade de produção                     | NÃO NULO  |
| IMPORTAÇÃO                   | Importação                   | INT          | Quantidade de importação                   | NÃO NULO  |
| VARIAÇÃO_DE_ESTOQUES         | Variação de Estoques         | SMALLINT     | Quantidade da variação de estoques         | NÃO NULO  |
| EXPORTAÇÃO                   | Exportação                   | INT          | Quantidade de exportação                   | NÃO NULO  |
| NÃO_APROVEITADA              | Não Aproveitada              | SMALLINT     | Quantidade não aproveitada                 | NÃO NULO  |
| REINJEÇÃO                    | Reinjeção                    | SMALLINT     | Quantidade reinjetada                      | NÃO NULO  |
| CONSUMO_FINAL_NÃO_ENERGÉTICO | Consumo Final Não Energético | SMALLINT     | Quantidade do consumo final não energético | NÃO NULO  |
| SETOR_ENERGÉTICO             | Setor Energético             | SMALLINT     | Quantidade no setor energético             | NÃO NULO  |
| RESIDENCIAL                  | Residencial                  | SMALLINT     | Quantidade residencial                     | NÃO NULO  |
| COMERCIAL                    | Comercial                    | SMALLINT     | Quantidade comercial                       | NÃO NULO  |
| PÚBLICO                      | Público                      | SMALLINT     | Quantidade no setor público                | NÃO NULO  |
| AGROPECUÁRIO                 | Agropecuário                 | SMALLINT     | Quantidade no setor agropecuário           | NÃO NULO  |
| RODOVIÁRIO                   | Rodoviário                   | INT          | Quantidade no setor rodoviário             | NÃO NULO  |
| FERROVIÁRIO                  | Ferroviário                  | SMALLINT     | Quantidade no setor ferroviário            | NÃO NULO  |
| AÉREO                        | Aéro                         | SMALLINT     | Quantidade no setor aéro                   | NÃO NULO  |
| HIDROVIÁRIO                  | Hidroviário                  | SMALLINT     | Quantidade no setor hidroviário            | NÃO NULO  |
| INDUSTRIAL_TOTAL             | Industrial Total             | SMALLINT     | Quantidade industrial total                | NÃO NULO  |
| Ano                          | Ano                          | SMALLINT     | Ano de análise                             | NÃO NULO  |

## **Página Extras - PNE**

#### **Tabela: EmTotPNE**
|   DADO   | NOME DO CAMPO | TIPO DO DADO |               DESCRIÇÃO               | RESTRIÇÃO |
|:--------:|:-------------:|:------------:|:-------------------------------------:|:---------:|
| Período  | Período       | NVARCHAR(50) | Período de análise                    | NÃO NULO  |
| Ano_2015 | Ano de 2015   | FLOAT        | Quantidade de emissões no ano de 2015 | NÃO NULO  |
| Ano_2030 | Ano de 2030   | TINYINT      | Quantidade de emissões no ano de 2030 | NÃO NULO  |
| Ano_2040 | Ano de 2040   | TINYINT      | Quantidade de emissões no ano de 2040 | NÃO NULO  |
| Ano_2050 | Ano de 2050   | TINYINT      | Quantidade de emissões no ano de 2050 | NÃO NULO  |
| Cenário  | Cenário       | NVARCHAR(50) | Cenário PNE                           | NÃO NULO  |

#### **Tabela: CustoTotPNE**

|      DADO     |   NOME DO CAMPO  |  TIPO DO DADO |          DESCRIÇÃO         | RESTRIÇÃO |
|:-------------:|:----------------:|:-------------:|:--------------------------:|:---------:|
| Tipo_Expansão | Tipo de expansão | NVARCHAR(50)  | Tipo de expansão analisada | NÃO NULO  |
| Ano_2012      | Ano de 2012      | FLOAT         | Custo total no ano de 2012 | NÃO NULO  |
| Ano_2015      | Ano de 2015      | SMALLINT      | Custo total no ano de 2015 | NÃO NULO  |
| Cenário       | Cenário          | NVARCHAR(150) | Cenário do PNE             | NÃO NULO  |

#### **Tabela:ConsGasNatPNE**

|    DADO   | NOME DO CAMPO |  TIPO DO DADO |                     DESCRIÇÃO                    | RESTRIÇÃO |
|:---------:|:-------------:|:-------------:|:------------------------------------------------:|:---------:|
| Período   | Período       | NVARCHAR(50)  | Período médio                                    | NÃO NULO  |
| Ano_2015  | Ano de 2015   | FLOAT         | Consumo de Gás Natural no ano de 2015 (Mm^3/dia) | NÃO NULO  |
| Ano_2030  | Ano de 2030   | TINYINT       | Consumo de Gás Natural no ano de 2030 (Mm^3/dia) | NÃO NULO  |
| Ano_2040  | Ano de 2040   | TINYINT       | Consumo de Gás Natural no ano de 2040 (Mm^3/dia) | NÃO NULO  |
| Ano_2050  | Ano de 2050   | SMALLINT      | Consumo de Gás Natural no ano de 2050 (Mm^3/dia) | NÃO NULO  |
| Cenário   | Cenário       | NVARCHAR(150) | Cenário do PNE                                   | NÃO NULO  |

## **Página Mundo**

#### **Tabela: Capacidade_Instalada_Matriz_Eletrica_BR_ONS**
|    DADO    | NOME DO CAMPO | TIPO DO DADO |                  DESCRIÇÃO                 | RESTRIÇÃO |
|:----------:|:-------------:|:------------:|:------------------------------------------:|:---------:|
| Ano        | Ano           | SMALLINT     | Ano de análise                             |           |
| Eólica     | Eólica        | FLOAT        | Capacidade instalada na geração Eólica     |           |
| Térmica    | Térmica       | FLOAT        | Capacidade instalada na geração Térmica    |           |
| Hidráulica | Hidráulica    | FLOAT        | Capacidade instalada na geração Hidráulica |           |
| Nuclear    | Nuclear       | FLOAT        | Capacidade instalada na geração Nuclear    |           |
| Solar      | Solar         | FLOAT        | Capacidade instalada na geração Solar      |           |
| MMGD       | MMGD          | FLOAT        | Capacidade instalada na geração MMGD       |       

#### **Tabela: CapInstBioPaises(GW)**
|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                DESCRIÇÃO                | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:---------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                          | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                         | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada (GW) | NÃO NULO  |


#### **Tabela: CapInstBioPaises(GW)**
|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                          DESCRIÇÃO                          | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:-----------------------------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                                              | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                                             | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada de geração biomassa (GW) | NÃO NULO  |

#### **Tabela: CapInstEolPaises(GW)**

|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                          DESCRIÇÃO                          | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:-----------------------------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                                              | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                                             | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada de geração eólica (GW) | NÃO NULO  |

#### **Tabela:CapInstFonte(MW)**

|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                DESCRIÇÃO                | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:---------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                          | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                         | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada (MW) | NÃO NULO  |

#### **Tabela: CapInstNucPaises (GW)**
|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                          DESCRIÇÃO                          | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:-----------------------------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                                              | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                                             | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada de geração nuclear(GW) | NÃO NULO  |

#### **Tabela: CapInstRenPaises(GW)**
|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                          DESCRIÇÃO                          | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:-----------------------------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                                              | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                                             | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada (GW) | NÃO NULO  |

#### **Tabela: CapInstSolPaises(GW)**
|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                          DESCRIÇÃO                          | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:-----------------------------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                                              | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                                             | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada de geração solar (GW) | NÃO NULO  |

#### **Tabela: CapInstTermFosPaises(GW)**
|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                          DESCRIÇÃO                          | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:-----------------------------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                                              | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                                             | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada de térmica fóssil (GW) | NÃO NULO  |

#### **Tabela: CapInstTermFosPaises(GW)**
|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                          DESCRIÇÃO                          | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:-----------------------------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                                              | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                                             | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada de térmica fóssil (GW) | NÃO NULO  |

#### **Tabela: CapInstHidPaises(GW)**
|         DADO         |     NOME DO CAMPO    | TIPO DO DADO |                          DESCRIÇÃO                          | RESTRIÇÃO |
|:--------------------:|:--------------------:|:------------:|:-----------------------------------------------------------:|:---------:|
| Ano                  | Ano                  | NVARCHAR(50) | Ano de análise                                              | NÃO NULO  |
| País                 | País                 | TINYINT      | País de análise                                             | NÃO NULO  |
| Capacidade_Instalada | Capacidade Instalada | SMALLINT     | Quantidade de Capacidade instalada de hidrelétrica  (GW) | NÃO NULO  |

#### **Tabela:GerBioPaises(TWh)**
|   DADO  | NOME DO CAMPO | TIPO DO DADO |                DESCRIÇÃO               | RESTRIÇÃO |
|:-------:|:-------------:|:------------:|:--------------------------------------:|:---------:|
| País    | País          | NVARCHAR(50) | País de análise                        | NÃO NULO  |
| Geração | Geração       | TINYINT      | Quantidade de geração - biomassa (TWh) | NÃO NULO  |
| Ano     | Ano           | SMALLINT     | Ano de análise                         | NÃO NULO  |

#### **Tabela:GerEolPaises(TWh)**
|   DADO  | NOME DO CAMPO | TIPO DO DADO |                DESCRIÇÃO               | RESTRIÇÃO |
|:-------:|:-------------:|:------------:|:--------------------------------------:|:---------:|
| País    | País          | NVARCHAR(50) | País de análise                        | NÃO NULO  |
| Geração | Geração       | TINYINT      | Quantidade de geração - eólica(TWh) | NÃO NULO  |
| Ano     | Ano           | SMALLINT     | Ano de análise                         | NÃO NULO  |

#### **Tabela:GerHidPaises(TWh)**
|   DADO  | NOME DO CAMPO | TIPO DO DADO |                DESCRIÇÃO               | RESTRIÇÃO |
|:-------:|:-------------:|:------------:|:--------------------------------------:|:---------:|
| País    | País          | NVARCHAR(50) | País de análise                        | NÃO NULO  |
| Geração | Geração       | TINYINT      | Quantidade de geração - hidrelétrica (TWh) | NÃO NULO  |
| Ano     | Ano           | SMALLINT     | Ano de análise                         | NÃO NULO  |

#### **Tabela:GerRenPaises(TWh)**
|   DADO  | NOME DO CAMPO | TIPO DO DADO |                DESCRIÇÃO               | RESTRIÇÃO |
|:-------:|:-------------:|:------------:|:--------------------------------------:|:---------:|
| País    | País          | NVARCHAR(50) | País de análise                        | NÃO NULO  |
| Geração | Geração       | TINYINT      | Quantidade de geração - fontes renováveis (TWh) | NÃO NULO  |
| Ano     | Ano           | SMALLINT     | Ano de análise                         | NÃO NULO  |

#### **Tabela:GerSolPaises(TWh)**
|   DADO  | NOME DO CAMPO | TIPO DO DADO |                DESCRIÇÃO               | RESTRIÇÃO |
|:-------:|:-------------:|:------------:|:--------------------------------------:|:---------:|
| País    | País          | NVARCHAR(50) | País de análise                        | NÃO NULO  |
| Geração | Geração       | TINYINT      | Quantidade de geração - solar (TWh) | NÃO NULO  |
| Ano     | Ano           | SMALLINT     | Ano de análise                         | NÃO NULO  |

#### **Tabela:GerTermFosPaises(TWh)**
|   DADO  | NOME DO CAMPO | TIPO DO DADO |                DESCRIÇÃO               | RESTRIÇÃO |
|:-------:|:-------------:|:------------:|:--------------------------------------:|:---------:|
| País    | País          | NVARCHAR(50) | País de análise                        | NÃO NULO  |
| Geração | Geração       | TINYINT      | Quantidade de geração - térmica fossilr (TWh) | NÃO NULO  |
| Ano     | Ano           | SMALLINT     | Ano de análise                         | NÃO NULO  |

## **Página Brasil**

#### **Tabela:GelElFonte(GWh)**
|   DADO  | NOME DO CAMPO | TIPO DO DADO |               DESCRIÇÃO              | RESTRIÇÃO |
|:-------:|:-------------:|:------------:|:------------------------------------:|:---------:|
| Fonte   | Fonte         | NVARCHAR(50) | Fonte de análise                     | NÃO NULO  |
| Geração | Geração       | INT          | Quantidade de geração elétrica (TWh) | NÃO NULO  |
| Ano     | Ano           | SMALLINT     | Ano de análise                       | NÃO NULO  |

#### **Tabela:EmGEESistIso(MtCO2)**
|     DADO     |  NOME DO CAMPO | TIPO DO DADO |               DESCRIÇÃO              | RESTRIÇÃO |
|:------------:|:--------------:|:------------:|:------------------------------------:|:---------:|
| Fonte        | Fonte          | NVARCHAR(50) | Fonte de análise                     | NÃO NULO  |
| Emissões_GEE | Emissão de GEE | INT          | Quantidade de emissão de GEE (MtCO2) | NÃO NULO  |
| Ano          | Ano            | SMALLINT     | Ano de análise                       | NÃO NULO  |

#### **Tabela:EmGEEGerEl(MtCO2)**
|     DADO     |  NOME DO CAMPO | TIPO DO DADO |               DESCRIÇÃO              | RESTRIÇÃO |
|:------------:|:--------------:|:------------:|:------------------------------------:|:---------:|
| Fonte        | Fonte          | NVARCHAR(50) | Fonte de análise                     | NÃO NULO  |
| Emissões_GEE | Emissão de GEE | INT          | Quantidade de emissão de GEE (MtCO2) | NÃO NULO  |
| Ano          | Ano            | SMALLINT     | Ano de análise                       | NÃO NULO  |

#### **Tabela:EmGEESIN(MtCO2)**
|     DADO     |  NOME DO CAMPO | TIPO DO DADO |               DESCRIÇÃO              | RESTRIÇÃO |
|:------------:|:--------------:|:------------:|:------------------------------------:|:---------:|
| Fonte        | Fonte          | NVARCHAR(50) | Fonte de análise                     | NÃO NULO  |
| Emissões_GEE | Emissão de GEE | INT          | Quantidade de emissão de GEE (MtCO2) | NÃO NULO  |
| Ano          | Ano            | SMALLINT     | Ano de análise                       | NÃO NULO  |

#### **Tabela: ConsMedResReg(kWh_mes)**

|            DADO           |       NOME DO CAMPO       | TIPO DO DADO |                     DESCRIÇÃO                     | RESTRIÇÃO |
|:-------------------------:|:-------------------------:|:------------:|:-------------------------------------------------:|:---------:|
| Região                    | Região                    | NVARCHAR(50) | Fonte de análise                                  | NÃO NULO  |
| Consumo_médio_residencial | Consumo Médio Residencial | FLOAT        | Quantidade de consumo médio residencial (kWH/mês) | NÃO NULO  |
| Ano                       | Ano                       | SMALLINT     | Ano de análise                                    | NÃO NULO  |

#### **Tabela: ConsMedResSubsis(kWh_mes)**
|            DADO           |       NOME DO CAMPO       | TIPO DO DADO |                     DESCRIÇÃO                     | RESTRIÇÃO |
|:-------------------------:|:-------------------------:|:------------:|:-------------------------------------------------:|:---------:|
| Região                    | Região                    | NVARCHAR(50) | Fonte de análise                                  | NÃO NULO  |
| Consumo_médio_residencial | Consumo Médio Residencial | FLOAT        | Quantidade de consumo médio residencial no subsistema  (kWH/mês) | NÃO NULO  |
| Ano                       | Ano                       | SMALLINT     | Ano de análise                                    | NÃO NULO  |

#### **Tabela:ConsMedTotReg(kWh_mes)**
|            DADO           |       NOME DO CAMPO       | TIPO DO DADO |                     DESCRIÇÃO                     | RESTRIÇÃO |
|:-------------------------:|:-------------------------:|:------------:|:-------------------------------------------------:|:---------:|
| Região                    | Região                    | NVARCHAR(50) | Fonte de análise                                  | NÃO NULO  |
| Consumo_médio_residencial | Consumo Médio Residencial | FLOAT        | Quantidade de consumo médio residencial na região (kWH/mês) | NÃO NULO  |
| Ano                       | Ano                       | SMALLINT     | Ano de análise                                    | NÃO NULO  |

#### **Tabela: ConsMedTotSubsis(kWh_mes)**
|            DADO           |       NOME DO CAMPO       | TIPO DO DADO |                     DESCRIÇÃO                     | RESTRIÇÃO |
|:-------------------------:|:-------------------------:|:------------:|:-------------------------------------------------:|:---------:|
| Região                    | Região                    | NVARCHAR(50) | Fonte de análise                                  | NÃO NULO  |
| Consumo_médio_residencial | Consumo Médio Residencial | FLOAT        | Quantidade de consumo médio residencial na região (kWH/mês) | NÃO NULO  |
| Ano                       | Ano                       | SMALLINT     | Ano de análise                                    | NÃO NULO  |

#### **Tabela: ConsMedAnPerCapReg(kWh_hab)**
|              DADO              |          NOME DO CAMPO         | TIPO DO DADO |                       DESCRIÇÃO                      | RESTRIÇÃO |
|:------------------------------:|:------------------------------:|:------------:|:----------------------------------------------------:|:---------:|
| Região                         | Região                         | NVARCHAR(50) | Região de análise                                    | NÃO NULO  |
| Consumo_médio_anual_per_capita | Consumo Médio Anual Per Capita | FLOAT        | Consumo Médio Anual Per Capita l na região (kWh_hab) | NÃO NULO  |
| Ano                            | Ano                            | SMALLINT     | Ano de análise                                       | NÃO NULO  |

#### **Tabela: emissoes_co2_Br**
|      DADO      |    NOME DO CAMPO    | TIPO DO DADO |            DESCRIÇÃO           | RESTRIÇÃO |
|:--------------:|:-------------------:|:------------:|:------------------------------:|:---------:|
| CO2_GWP_SAR_Gg | GWP - SAR Gg (CO2e) | NVARCHAR(50) | Setor de análise               |           |
| Ano_1991       | Ano 1991            | INT          | Quantidade de emissões em 1991 |           |
| Ano_1992       | Ano 1992            | INT          | Quantidade de emissões em 1992 |           |
| Ano_1993       | Ano 1993            | INT          | Quantidade de emissões em 1993 |           |
| Ano_1994       | Ano 1994            | INT          | Quantidade de emissões em 1994 |           |
| Ano_1995       | Ano 1995            | INT          | Quantidade de emissões em 1995 |           |
| Ano_1996       | Ano 1996            | INT          | Quantidade de emissões em 1996 |           |
| Ano_1997       | Ano 1997            | INT          | Quantidade de emissões em 1997 |           |
| Ano_1998       | Ano 1998            | INT          | Quantidade de emissões em 1998 |           |
| Ano_1999       | Ano 1999            | INT          | Quantidade de emissões em 1999 |           |
| Ano_2000       | Ano 2000            | INT          | Quantidade de emissões em 2000 |           |
| Ano_2001       | Ano 2001            | INT          | Quantidade de emissões em 2001 |           |
| Ano_2002       | Ano 2002            | INT          | Quantidade de emissões em 2002 |           |
| Ano_2003       | Ano 2003            | INT          | Quantidade de emissões em 2003 |           |
| Ano_2004       | Ano 2004            | INT          | Quantidade de emissões em 2004 |           |
| Ano_2005       | Ano 2005            | INT          | Quantidade de emissões em 2005 |           |
| Ano_2006       | Ano 2006            | INT          | Quantidade de emissões em 2006 |           |
| Ano_2007       | Ano 2007            | INT          | Quantidade de emissões em 2007 |           |
| Ano_2008       | Ano 2008            | INT          | Quantidade de emissões em 2008 |           |
| Ano_2009       | Ano 2009            | INT          | Quantidade de emissões em 2009 |           |
| Ano_2010       | Ano 2010            | INT          | Quantidade de emissões em 2010 |           |
| Ano_2011       | Ano 2011            | INT          | Quantidade de emissões em 2011 |           |
| Ano_2012       | Ano 2012            | INT          | Quantidade de emissões em 2012 |           |
| Ano_2013       | Ano 2013            | INT          | Quantidade de emissões em 2013 |           |
| Ano_2014       | Ano 2014            | INT          | Quantidade de emissões em 2014 |           |
| Ano_2015       | Ano 2015            | INT          | Quantidade de emissões em 2015 |           |
| Ano_2016       | Ano 2016            | INT          | Quantidade de emissões em 2016 |           |
| Ano_2017       | Ano 2017            | INT          | Quantidade de emissões em 2017 |           |
| Ano_2018       | Ano 2018            | INT          | Quantidade de emissões em 2018 |           |
| Ano_2019       | Ano 2019            | INT          | Quantidade de emissões em 2019 |           |
| Ano_2020       | Ano 2020            | INT          | Quantidade de emissões em 2020 |           |

#### **Tabela: Evolucao_Energia_1970_2022**
|        DADO        |     NOME DO CAMPO    | TIPO DO DADO |                      DESCRIÇÃO                     | RESTRIÇÃO |
|:------------------:|:--------------------:|:------------:|:--------------------------------------------------:|:---------:|
| ANO                | Ano                  | VARCHAR(150) | Ano de análise                                     |           |
| NÃO_RENOVÁVEL      | Não Renovável        | VARCHAR(150) | Produção de enregia - Não renováveis ( 103tep)     |           |
| PETRÓLEO           | Petróleo             | VARCHAR(150) | Produção de enregia - Petróleo ( 103tep)           |           |
| GÁS_NATURAL        | Gás Natural          | VARCHAR(150) | Produção de enregia - Gás Natural ( 103tep)        |           |
| CARVÃO_VAPOR       | Carvão -  Vapor      | VARCHAR(150) | Produção de enregia -Carvão vapor  ( 103tep)       |           |
| CARVÃO_METALÚRGICO | Carvão - Metaluigico | VARCHAR(150) | Produção de enregia - Carvão metalúrgico ( 103tep) |           |
| UR NIO_U3O8        | Urânio U3O8          | VARCHAR(150) | Produção de enregia - Urânio ( 103tep)             |           |
| RENOVÁVEL          | Renovável            | VARCHAR(150) | Produção de enregia - Renovaveis ( 103tep)         |           |
| ENERGIA_HIDRÁULICA | Energia Hidráulica   | VARCHAR(150) | Produção de enregia - Energia Hidráulica( 103tep)  |           |
| LENHA              | Lenha                | VARCHAR(150) | Produção de enregia - Lenha ( 103tep)              |           |
| PRODUTOS_DA_CANA   | Produtos da Cana     | VARCHAR(150) | Produção de enregia - Produtos da Cana  ( 103tep)  |           |
| EÓLICA             | Eólica               | VARCHAR(150) | Produção de enregia - Eólica  ( 103tep)            |           |
| SOLAR              | Solar                | VARCHAR(150) | Produção de enregia - Solar ( 103tep)              |           |
| OUTRAS_RENOVÁVEIS  | Outras Renováveis    | VARCHAR(150) | Produção de enregia - Outras Renováveis ( 103tep)  |           |
| TOTAL              | Total                | VARCHAR(150) | Produção de enregia - Total ( 103tep)              |           |

## Histórico de versão

| Versão |    Data    |                       Descrição                       |      Autor       |
| :----: | :--------: | :---------------------------------------------------: | :--------------: |
|  1.0   | 04/07/2023 |           Criação do documento e adição de conteúdo           |Ugor Brandão|

























