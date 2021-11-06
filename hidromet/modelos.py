"""Estruturas de informação sobre as séries de cada posto/bacia."""
from typing import List
from pydantic import BaseModel


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