import dash
from dash import dcc
from dash import html
import geopandas as gpd
import pandas as pd

from hidromet import config
from hidromet import visualizacao
from hidromet import utils

# encontrando diretorios
contornos = config.dir_contorno
dir_series_concatenadas = config.dir_prec_concat
info_bacias = list(dir_series_concatenadas.glob("*.json"))
series = list(dir_series_concatenadas.glob("*_sout.csv"))

#abrindo arquivos com postos
bacias = list()
for bacia in info_bacias:
    var = utils.carregar_json(bacia)
    aux = pd.DataFrame(var)
    bacias.append(aux)

df_postos = pd.concat(bacias)
df_postos.set_index('codigo', inplace=True)
    
# abrindo contornos
gdf_contornos = gpd.read_file(contornos)
crs = gdf_contornos.crs

#abrindo arquivos de series
df_series = list()
for serie in series:
    df = pd.read_csv(serie)
    df_series.append(df)

series_concatenadas = pd.concat(df_series, axis=1)
series_concatenadas.rename(columns={"Unnamed: 0": "time"}, inplace=True)
series_concatenadas.set_index("time", inplace=True)
falhas = round(series_concatenadas.isna().sum()/len(series_concatenadas),2)*100

df_postos = df_postos.assign(falhas=falhas)  


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dados de precipitação'),

    html.Div(children='''
        Dados iniciais de precipitação
    '''),

    dcc.Graph(
        id='postos-geograficos',
        figure=visualizacao.plot_postos(df_postos, gdf_contornos)
    ),
    dcc.Graph(
        id="falhas",
        figure=visualizacao.plot_bubble(df_postos)
    ),
    dcc.Graph(
        id='series-concatenadas',
        figure=visualizacao.plot_series(series_concatenadas)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)