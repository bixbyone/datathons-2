"""Arquivo de configurações do projeto"""
from pathlib import Path


dir_abs = Path(__file__).parent.parent
dir_contorno = dir_abs.joinpath("contornos", "iguacu.shp")
dir_prec_ana = dir_abs.joinpath("arquivos", "series-chuva-ana")
dir_prec_inmet = dir_abs.joinpath("arquivos", "series-chuva-inmet")

dir_prec_ana.mkdir(parents=True, exist_ok=True)
