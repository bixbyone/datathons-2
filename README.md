# Datathons 2

![texto](https://img.shields.io/static/v1?label=linguagem&message=python&color=green&style=flat-square "linguagem")

1. [Descrição do projeto](#descrição-do-projeto)  
2. [Funcionalidades](#funcionalidades)  
3. [Pré-requisitos](#pré-requisitos)  
4. [Execução](#execucao)

## :scroll: Descrição do projeto

Consolidação de dados de precipitação da bacia do Iguaçu.

## :sparkles: Funcionalidades

:heavy_check_mark: Obtenção de séries de precipitação da ANA e INMET

:heavy_check_mark: Obtenção de séries de precipitação do MERGE

:heavy_check_mark: Limpeza e remoção de dados espúrios nas séries de precipitação

:heavy_check_mark: Preenchimento de falhas com dados de satélite

:heavy_check_mark: EXTRA: Melhoria de cobertura da bacia utilizando postos pluviométricos artificiais


## :warning: Pré-requisitos

- [Python](https://www.python.org/) (obrigatório)
- [Conda](https://docs.conda.io/en/latest/) (para desenvolvimento)


## :arrow_forward: Execução

### Como executar

Para utilizar as funções do módulo `hidromet`, serão necessários os seguintes passos:

1. Clone este repositório.

```bash
git clone git@github.com:andradelis/datathons-2.git
```

2. Acesse o diretório do projeto.
```
cd datathons-2
```

3. Instale as dependências.

```bash
pip install -r requirements.txt
```

### :computer: Ordem de execução dos notebooks

> OBS: Todos os notebooks com o prefixo `dados` poderão ser rodados em qualquer ordem. Estes servem apenas para a coleta de dados de diversas fontes.

> OBS2: Os dados extraídos de cada etapa são exportados para o diretório `arquivos`. O download de séries de satélite **poderá demorar algumas horas**! Para a operacionalização, o dado de satélite deverá ser baixado apenas para o dia atual corrente e acrescido ao restante do histórico.


#### Execução completa

1. 00.dados-ANA.ipynb
1. 00.dados-INMET.ipynb
1. 00.dados-satelite.ipynb

2. 01.remocao-repetidos.ipynb
3. 02.EDA-viz.ipynb
4. 03.rem-out.ipynb
5. 04.representatividade.ipynb
6. 05.preenchimento.ipynb
7. 06.execucao.ipynb

**EXTRA** Preenchimento da cobertura de postos a partir de postos artificiais!
6. 05.extra.preenchimento-bacias.ipynb

#### Teste do resultado

1. 06.execucao.ipynb

## :construction: Desenvolvimento

### :snake: Preparação do ambiente Python

```bash
# 1. entre no diretório do projeto
cd datathons-2

# 2. crie o ambiente virtual do projeto
bash conda-install.bash

# 3. ative o ambiente
conda activate datathons-2
```

