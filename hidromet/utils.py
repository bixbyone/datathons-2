"""Utilitários gerais."""
import json

from pathlib import Path
from typing import Any
from typing import Dict

import pandas as pd


def carregar_json(arquivo: Path) -> Dict[Any, Any]:
    """
    Carrega um arquivo json.

    Parameters
    ----------
    arquivo : Path
        Caminho para o arquivo json.

    Returns
    -------
    Dict[Any, Any]
        Arquivo json
    """
    with open(arquivo) as f:
        json_data = json.load(f)

    return json_data
