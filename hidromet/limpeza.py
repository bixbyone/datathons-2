"""Funções para a limpeza de séries."""

from datetime import date

import numpy as np
import pandas as pd


def remover_codigos_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove os códigos duplicados do dataset.

    Atualmente, a remoção mantém o primeiro código disponível.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe de entrada indexado por código de posto.

    Returns
    -------
    pd.DataFrame
        Dataframe com códigos de postos removidos.
    """
    return df[~df.index.duplicated(keep="first")]


def remover_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove índices de data duplicados.

    OBS: o primeiro valor disponível para a data duplicada será mantido.

    Parameters
    ----------
    df : pd.DataFrame
        Série de dados.

    Returns
    -------
    pd.DataFrame
        Série sem datas duplicadas.
    """
    return df.loc[~df.index.duplicated(), :]


def percentil(serie: pd.Series, p: float) -> float:
    """
    Retorna o percentil de uma série.

    Parameters
    ----------
    serie : pd.Series
        Série de dados.

    p : float
        Percentil da série, de 0 a 1.

    Returns
    -------
    float
        Número da série que representa o percentil solicitado.
    """
    return serie.quantile(p)


def remover_outliers(serie: pd.Series, limite: float = 400) -> pd.Series:
    """
    Remove os valores maiores que o limite máximo possível da série.

    OBS: Onde houver outliers, o valor será substituído por NaN na série.

    Parameters
    ----------
    serie : pd.Series
        Série de dados.

    limite : float
        Limite máximo da série.

    Returns
    -------
    pd.Series
        Série sem outliers.
    """
    indice_outliers = serie[serie > limite].index
    serie.loc[indice_outliers] = np.nan

    return serie


def substituir_negativos(serie: pd.Series) -> pd.Series:
    """
    Substitui valores negativos da série por NaN.

    Parameters
    ----------
    serie : pd.Series
        Série de dados.

    Returns
    -------
    pd.Series
        Série com valores negativos substituídos por NaN.
    """
    serie_sem_na = serie.dropna()
    indices_negativos = serie_sem_na[serie_sem_na < 0].index
    serie.loc[indices_negativos] = np.nan
    return serie


def contabilizar_falhas(serie: pd.Series) -> float:
    """
    Contabiliza a porcentagem de falhas de uma série de dados.

    Parameters
    ----------
    serie : pd.Series
        Série de dados.

    Returns
    -------
    float
        Porcentagem de falhas na série.
    """
    n_dados = len(serie)
    n_nan = serie.isna().sum()

    return n_nan / n_dados


def recortar_periodo(serie: pd.Series, inicio: date, fim: date) -> pd.Series:
    """
    Recorta um período da série.

    Parameters
    ----------
    serie : pd.Series
        Série de dados completa.

    inicio : datetime
        Data inicial desejada.

    fim : datetime
        Data final desejada.

    Returns
    -------
    pd.Series
        Série recortada no período solicitado.
    """
    return serie[(serie.index >= inicio) & (serie.index <= fim)]


def remover_meses_nao_representativos(
    df: pd.DataFrame, limite: int = 15
) -> pd.DataFrame:
    """
    Remove meses com menos de x dias de dados.

    Parameters
    ----------
    df : pd.DataFrame
        Série de dados.

    limite : int
        Número mínimo de dias presentes na série mensal.

    Returns
    -------
    pd.DataFrame
        Série de dados contendo apenas meses com mais de
        15 dias de representatividade.
    """
    contagem = df.groupby([(df.index.year), (df.index.month)]).count()
    for ano, mes in contagem.index:
        dias = contagem.loc[(ano, mes)].values[0]
        if dias < limite:
            condicao = (df.index.month == mes) & (df.index.year == ano)
            df.drop(df.loc[condicao].index, axis=0, inplace=True)

    return df


def anos_disponiveis(df: pd.DataFrame) -> float:
    """
    Obtém o número de anos de disponibilidade de dados em uma série.

    OBS: O número de anos não considera meses consecutivos, apenas o número
    total de meses e quantos anos o número representa.

    Parameters
    ----------
    df : pd.Series
        Série de dados a ser avaliada.

    Returns
    -------
    int
        Número de anos com dados disponíveis na série.
    """
    serie_mensal = df.resample("M").mean()
    serie_mensal.dropna(inplace=True)
    meses_disponiveis = len(serie_mensal)

    return meses_disponiveis / 12
