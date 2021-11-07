"""Módulo para coleta de arquivos do merge."""
from datetime import datetime
from typing import List

import geopandas as gpd
import pandas as pd
import requests
import xarray as xr

from hidromet import config


def obter(data: datetime) -> xr.Dataset:
    """
    Baixa arquivo horário do Merge.

    Parameters
    ----------
    data: Datetime
        Data do arquivo a ser baixado

    Returns
    ----------
    arquivo_grib
        Diretório do arquivo merge baixado.
    """
    mes = str(data.month).zfill(2)
    ano = str(data.year)
    data_fmt = data.strftime("%Y%m%d")
    nome_arquivo = f"MERGE_CPTEC_{data_fmt}.grib2"
    arquivo_grib = config.dir_merge.joinpath(nome_arquivo)

    url = f"http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY/{ano}/{mes}/{nome_arquivo}"
    req = requests.get(url=url)

    if req.status_code == 200:
        with open(arquivo_grib, "wb") as f:
            f.write(req.content)

    return arquivo_grib
