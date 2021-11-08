"""Arquivo de configurações do projeto"""
from pathlib import Path


dir_abs = Path(__file__).parent.parent
dir_arquivos = dir_abs.joinpath("arquivos")
dir_shapefile = dir_abs.joinpath("contornos")

dir_satelite = dir_arquivos.joinpath("satelite")
dir_contorno = dir_shapefile.joinpath("iguacu.shp")
dir_prec_ana = dir_arquivos.joinpath("series-chuva-ana")
dir_prec_inmet = dir_arquivos.joinpath("series-chuva-inmet")
dir_prec_concat = dir_arquivos.joinpath("series-concatenadas")
dir_merge = dir_arquivos.joinpath("merge")
dir_merge_concat = dir_arquivos.joinpath("merge-concatenado")
dir_merge_posto = dir_arquivos.joinpath("merge-e-posto")
dir_final = dir_arquivos.joinpath("series-preenchidas")
dir_final_extra = dir_arquivos.joinpath("series-preenchidas-extra")

dir_arquivos.mkdir(parents=True, exist_ok=True)
dir_shapefile.mkdir(parents=True, exist_ok=True)
dir_prec_ana.mkdir(parents=True, exist_ok=True)
dir_prec_inmet.mkdir(parents=True, exist_ok=True)
dir_prec_concat.mkdir(parents=True, exist_ok=True)
dir_merge.mkdir(parents=True, exist_ok=True)
dir_merge_concat.mkdir(parents=True, exist_ok=True)
dir_merge_posto.mkdir(parents=True, exist_ok=True)
dir_final.mkdir(parents=True, exist_ok=True)
dir_final_extra.mkdir(parents=True, exist_ok=True)

# epsg UTM da bacia do iguaçu
epsg = "31985"
# epgs inicial
epsg_inicial = "4326"
# buffer em metros
buffer = 15000
