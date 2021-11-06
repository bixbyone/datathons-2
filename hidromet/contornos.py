"""Módulo de funções referentes aos contornos."""
from typing import Any
from typing import List
from typing import Optional

import geopandas as gpd
import pandas as pd
import shapely


def obter_buffer(
    contorno: gpd.geodataframe.GeoDataFrame, distancia: float
) -> gpd.geodataframe.GeoDataFrame:
    """
    Calcula o buffer de um geodataframe.

    Parameters
    ----------
    contorno : gpd.geodataframe.GeoDataFrame
        Geodataframe de entrada.

    distancia : float
        Distância do buffer.

    Returns
    -------
    gpd.geodataframe.GeoDataFrame
        Geodataframe do buffer.
    """
    crs = contorno.crs
    df_buffer = contorno.buffer(distancia).to_frame()
    df_buffer.rename({0: "geometry"}, axis=1, inplace=True)
    df_buffer.set_crs(crs=crs, inplace=True)

    return df_buffer


def dissolver(contorno: gpd.geodataframe.GeoDataFrame) -> gpd.geodataframe.GeoDataFrame:
    """
    Dissolve um geodataframe.

    Parameters
    -------
    contorno : gpd.geodataframe.GeoDataFrame
        Dataframe de coordenadas.

    Returns
    -------
    gpd.geodataframe.GeoDataFrame
        Dataframe de coordenadas.
    """
    crs = contorno.crs
    return contorno.dissolve().set_crs(crs=crs)


def calcular_area(contorno: gpd.geodataframe.GeoDataFrame) -> float:
    """
    Calcula a área a partir da geometria de um único geodataframe.

    Parameters
    -------
    contorno : gpd.geodataframe.GeoDataFrame
        Geodataframe de entrada.

    Returns
    -------
    float
        Área do contorno.
    """
    return contorno.area.values[0]


def calcular_representatividade(
    contorno: gpd.geodataframe.GeoDataFrame, referencia: gpd.geodataframe.GeoDataFrame
) -> float:
    """
    Calcula a representatividade de um contorno sobre um contorno de referência.

    Parameters
    ----------
    contorno : gpd.geodataframe.GeoDataFrame
        Contorno de entrada.

    referencia : gpd.geodataframe.GeoDataFrame
        Contorno de referência.

    Returns
    -------
    float
        Porcentagem de representatividade do contorno de entrada sobre a referência.
    """
    return round(calcular_area(contorno) / calcular_area(referencia) * 100, 2)


def obter_intersecao(
    contorno: gpd.geodataframe.GeoDataFrame, mascara: gpd.geodataframe.GeoDataFrame
) -> gpd.geodataframe.GeoDataFrame:
    """
    Obtém a porção do contorno de entrada que está dentro da máscara.

    Parameters
    -------
    contorno : gpd.geodataframe.GeoDataFrame
        Geodataframe do contorno de entrada.

    mascara : gpd.geodataframe.GeoDataFrame
        Geodataframe da máscara.

    Returns
    -------
    gpd.geodataframe.GeoDataFrame
        Porção do contorno de entrada dentro da máscara.
    """
    return gpd.overlay(contorno, mascara, how="intersection")


def converter_epsg(
    contorno: gpd.geodataframe.GeoDataFrame, epsg: int
) -> gpd.geodataframe.GeoDataFrame:
    """
    Converte um geodataframe para um outro sistema de coordenadas.

    Parameters
    -------
    contorno : gpd.geodataframe.GeoDataFrame
        Dataframe de coordenadas.

    epsg : int
        Código do sistema de coordenadas.

    Returns
    -------
    gpd.geodataframe.GeoDataFrame
        Dataframe de coordenadas.
    """
    return contorno.to_crs(epsg=epsg)


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
