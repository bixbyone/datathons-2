"""Estruturas de informação sobre as séries de cada posto/bacia."""
from typing import List

import pandas as pd

from hidromet import config
from pydantic import BaseModel
from shapely.geometry import Point


class Posto(BaseModel):
    """Dados do posto."""

    # latitude do posto
    latitude: float
    # longitude do posto
    longitude: float
    # código do posto
    codigo: str


class Bacia(BaseModel):
    """Dados da bacia."""

    # lista de postos com a série vazia
    serie_vazia: List[Posto]
    # lista de postos com menos do mínimo de número de anos de dados.
    nao_representativos: List[Posto]
    # lista de postos com mais do limite de falhas
    com_falhas: List[Posto]
    # postos remanescentes (ok)
    postos_ok: List[Posto]
    # número total de postos, tendo ou não passado no teste
    n_postos: int
    # nome da bacia
    bacia: str


class Satelite(BaseModel):
    """Dados de satélite."""

    # coordenadas do ponto de grade
    coordenadas: Point
    # serie de precipitação
    serie: pd.Series

    class Config:
        """Configurações de tipo."""

        arbitrary_types_allowed = True


class IntersecaoSatelitePosto(BaseModel):
    """Estrutura de interseção entre satélite e postos de chuva."""

    # coordenadas do posto
    coords_posto: Point
    # nome do posto
    codigo_posto: str
    # extensão do buffer
    extensao_buffer: float = config.buffer
    # lista de pontos de grade de satélite dentro do buffer
    pontos_grade: List[Point]
    # série de precipitação média dos pontos de grade do satélite
    serie_satelite: pd.Series

    class Config:
        """Configurações de tipo."""

        arbitrary_types_allowed = True
