import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import geopandas as gpd
from hidromet import contornos


def plot_postos(pontos:pd.DataFrame, shp:gpd.GeoDataFrame) -> go.Figure:
    """
    Plota um mapa com os postos e a bacia hidrográfica.
    ----------------------------------------------------
    pontos: pd.DataFrame
        DataFrame com os dados dos postos: latitude, longitude e nome.
    shp: gpd.GeoDataFrame
        Geodataframe bacia hidrográfica.
    ----------------------------------------------------
    Retorna um objeto do tipo go.Figure

    """
    postos = pontos.index
    xs = pontos['x']
    ys = pontos['y']

    df = contornos.coordenadas_shapefile(shp)
    bacia_lon = df['longitude']
    bacia_lat = df['latitude']

    fig = go.Figure()

    fig.add_trace(go.Scattermapbox(
        lon=bacia_lon,
        lat=bacia_lat,
        mode='lines',
        fill='toself',
        fillcolor='rgba(191, 191, 191, 0.6)',
        opacity=0,
        line=dict(
            width=5,
            color='rgba(46, 49, 49, 1)',
        )
    ))

    fig.add_trace(go.Scattermapbox(
        lon=xs,
        lat=ys,
        text=postos,
        mode='markers',
        marker=dict(
            size=8,
            color='black',
            opacity=1
        )
    ))


    fig.update_layout(
        height=500,
        margin={"r":0,"t":0,"l":0,"b":0},
        mapbox_style="open-street-map",
        showlegend=False
    )

    fig.update_layout(
        mapbox_center={"lat": -25.5, "lon": -49.25},
        mapbox_zoom=5.5,
    )

    return fig.show()


def plot_series(series:pd.DataFrame) -> go.Figure:

    """
    Plota um gráfico de barras com os dados de uma série temporal.
    ----------------------------------------------------

    series: pd.DataFrame
        DataFrame com os dados da série temporal.
    ----------------------------------------------------
    Retorna um objeto do tipo go.Figure
    """


    figline = px.line(
                series, 
                x=series.index, 
                y=series.columns,
                title="Precipitação por posto da bacia do Iguaçu"
                )



    figline.update_layout(annotations=[], overwrite=True,
        xaxis_title="Tempo",
        yaxis_title="Precipitação (mm)",
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        plot_bgcolor="white",
    )


   
    return figline.show(config=dict(displayModeBar=False))


def plot_bubble(series:pd.DataFrame) -> go.Figure:

    """
    Plota um gráfico de bolhas com as falhas dos postos.
    ----------------------------------------------------
    series: pd.DataFrame
        DataFrame com os falhas da série temporal.
    ----------------------------------------------------
    Retorna um objeto do tipo go.Figure
    """

    posto = series.index
    xs = series['x']
    ys = series['y']
    falhas = series['falhas']

    figbub = go.Figure()


    figbub.add_trace(go.Scattergeo(
        lon=xs,
        lat=ys,
        text=[posto, falhas],
        mode='markers',
        marker=dict(
            color='black',
            opacity=0.7,
            size=falhas
        )
    ))


    figbub.update_layout(
        height=500,
        margin={"r":0,"t":0,"l":0,"b":0},
        mapbox_style="open-street-map"
    )

    figbub.update_layout(
        mapbox_center={"lat": -25.5, "lon": -49.25},
        mapbox_zoom=5.5,
    )

    return figbub.show()   