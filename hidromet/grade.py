"""Métodos utilitários para lidar com dados em grade."""
import os

from pathlib import Path

import geopandas as gpd
import rioxarray
import xarray as xr

from hidromet import config


def converter_grib_para_netcdf(
    arquivo_grib: Path, arquivo_netcdf: Path, remover_arquivo_grib: bool = True
) -> None:
    """
    Converte um arquivo GRIB em um arquivo NetCDF.

    Parameters
    ----------
    arquivo_grib : Path
        Caminho para o arquivo grib.

    arquivo_netcdf : Path
        Caminho para o arquivo netcdf.

    remover_arquivo_grib : bool
        Caso seja desejado remover o arquivo grib do diretório.
    """
    ds = xr.open_dataset(arquivo_grib, engine="cfgrib")
    ds.to_netcdf(arquivo_netcdf)

    if remover_arquivo_grib:
        arquivos_indesejados = config.dir_merge.glob("*[!nc]")
        for arquivo in list(arquivos_indesejados):
            os.remove(arquivo)


def preparar_para_recorte(
    dataset: xr.Dataset, crs="epsg:4326", xdim="longitude", ydim="latitude"
) -> xr.Dataset:
    """
    Ajusta o dataset para ter sistema de coordenadas correto para o recorte.
    ----------
    Argumentos:
        dataset: Dataset
            Dataset a ser ajustado.
        crs: str
            Sistema de coordenadas a ser utilizado.
        xdim: str
            Nome da dimensão x.
        ydim: str
            Nome da dimensão y.
    ----------
    Retorna:
        Dataset
    """
    dataset = dataset.assign_coords(
        longitude=(((dataset.longitude + 180) % 360) - 180)
    ).sortby(xdim)
    dataset = dataset.rio.set_spatial_dims(x_dim=xdim, y_dim=ydim)
    dataset = dataset.rio.write_crs(crs)
    return dataset


def recorte(dataset, shp):
    """
    Recorta o dataset de acordo com o polígono do shapefile.
    ----------
    Argumentos:
        dataset: Dataset
        shp: GeoDataFrame
    """
    shapefile = gpd.GeoDataFrame(shp).transpose()
    clip = dataset.rio.clip(shapefile["geometry"], "epsg:4326")

    return clip


def reprojetar(dataset, crs_destino):
    """
    Reprojeta o dataset para o sistema de coordenadas especificado.
    ----------
    Argumentos:
        dataset: Dataset
        crs_destino: str
    """
    dataset = dataset.rio.reproject(crs_destino)
    return dataset
