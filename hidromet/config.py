"""Arquivo de configurações do projeto"""
from pathlib import Path


dir_abs = Path(__file__).parent.parent
dir_arquivos = dir_abs.joinpath("arquivos")
dir_shapefile = dir_abs.joinpath("contornos")

dir_contorno = dir_shapefile.joinpath("iguacu.shp")
dir_prec_ana = dir_arquivos.joinpath("series-chuva-ana")
dir_prec_inmet = dir_arquivos.joinpath("series-chuva-inmet")
dir_prec_concat = dir_arquivos.joinpath("series-concatenadas")


dir_arquivos.mkdir(parents=True, exist_ok=True)
dir_shapefile.mkdir(parents=True, exist_ok=True)
dir_prec_ana.mkdir(parents=True, exist_ok=True)
dir_prec_inmet.mkdir(parents=True, exist_ok=True)
dir_prec_concat.mkdir(parents=True, exist_ok=True)
