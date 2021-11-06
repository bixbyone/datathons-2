"""Utilitários gerais."""
from pathlib import Path
import json
import pandas as pd

def obter_coordenadas(arquivo: Path) -> pd.DataFrame:
    """
    Obtém os postos de medição que passaram nos testes.

    Parameters
    ----------
    arquivo : Path
        Diretório para o arquivo json.

    Returns
    -------
    pd.DataFrame
        DataFrame com as coordenadas dos pontos de medição que passaram nos testes. 
    """
    with open(arquivo) as f:
        json_data = json.load(f)

    postos_ok = json_data['postos_ok']
    return pd.DataFrame.from_dict(postos_ok).round(2)