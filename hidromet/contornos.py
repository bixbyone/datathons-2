"""Módulo de funções referentes aos contornos."""
from typing import Any
from typing import List
from typing import Optional

import geopandas as gpd
import pandas as pd
import shapely


def recortar_postos(
    postos: gpd.geoseries.GeoSeries, contorno: shapely.geometry.polygon.Polygon
) -> gpd.geodataframe.GeoDataFrame:
    """
    Recorta os postos dentro de um contorno.

    Parameters
    ----------
    postos : gpd.geoseries.GeoSeries
        Série de geometrias dos postos indexados pelo código.

    contorno : shapely.geometry.polygon.Polygon
        Geometria do polígono de entrada.

    Returns
    -------
    gpd.geodataframe.GeoDataFrame
        Lista de postos dentro do contorno.
    """
    recorte = postos.geometry.within(contorno)
    return postos.loc[recorte].to_frame()


def zipar_coordenadas(
    latitude: gpd.geoseries.GeoSeries, longitude: gpd.geoseries.GeoSeries
) -> List[shapely.geometry.Point]:
    """
    Concatena uma série de latitude e outra de longitude.

    A lista de saída contém objetos do tipo shapely.geometry.Point.

    Parameters
    -------
    latitude : gpd.geoseries.GeoSeries
        Série de latitudes.

    longitude : gpd.geoseries.Geoseries
        Série de longitudes

    Returns
    -------
    List[shapely.geometry.Point]
        Lista de coordenadas.
    """
    return [shapely.geometry.Point(x) for x in zip(longitude, latitude)]


def criar_geodataframe(
    coordenadas: List[Any], df: Optional[pd.DataFrame] = None
) -> gpd.geodataframe.GeoDataFrame:
    """
    Cria um geodataframe a partir de uma lista de coordenadas.

    Parameters
    -------
    coordenadas : List[Any]
        Lista de coordenadas.

    Returns
    -------
    gpd.geodataframe.GeoDataFrame
        Dataframe de coordenadas.
    """
    return gpd.GeoDataFrame(df, geometry=coordenadas)
