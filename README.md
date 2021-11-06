# dados-hidrometeorologicos

![texto](https://img.shields.io/static/v1?label=linguagem&message=python&color=green&style=flat-square "linguagem")

1. [Descrição do projeto](#descrição-do-projeto)  
2. [Funcionalidades](#funcionalidades)  
3. [Pré-requisitos](#pré-requisitos)  
4. [Como rodar a aplicação](#como-rodar-a-aplicação)

## :scroll: Descrição do projeto

Módulo de obtenção e processamento de dados hidrometeorológicos.

## :sparkles: Funcionalidades

:heavy_check_mark: Obtenção de séries de precipitação da ANA e INMET

:wrench: Módulo de utilidades para recorte de séries dentro de uma bacia.

## :warning: Pré-requisitos

- [Python](https://www.python.org/) (obrigatório)
- [Poetry](https://python-poetry.org/) (para desenvolvimento)


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

### Exemplos de uso

#### Lista de todas as estações telemétricas do INMET.
```python
from hidromet.INMET import INMET

inmet = INMET()
inmet.listar_estacoes()
```

#### Inventário pluviométrico das estações da Agência Nacional das Águas.
```python
from hidromet.ANA import ANA

ana = ANA()
ana.inventario(tipoest=2)
```

Mais exemplos de uso disponíveis nos notebooks `dadosANA.ipynb` e `dadosINMET.ipynb`!

**OBS** Nos notebooks estão disponíveis exemplos de recorte dos dados pluviométricos extraídos da ANA e do INMET a partir dos contornos para os SMAPS mensais do laboratório. Os contornos são aqueles disponíveis na pasta de modelagem e gerados manualmente no QGis. 

## :construction: Desenvolvimento

### :snake: Preparação do ambiente Python

```bash
# 1. entre no diretório do projeto
cd datathons-2

# 2. crie o ambiente virtual do projeto
poetry install

# 3. ative o ambiente (opcional)
source .venv/bin/activate
```

