"""Módulo para obtenção de dados do Instituto Nacional de Meteorologia."""

from typing import Dict
from typing import List
from typing import Literal

import requests


# Código baseado no manual de uso da API de estações e dados meteorológicos do INMET: https://portal.inmet.gov.br/manual/manual-de-uso-da-api-estações


class INMET:
    """Classe de requisição da API do INMET."""

    url_base = "https://apitempo.inmet.gov.br"

    def __init__(self) -> None:
        """Inicialização da classe de consumo da API."""
        pass

    def obter_dados_estacao(
        self,
        data_inicial: str,
        data_final: str,
        cod_estacao: str,
        freq: Literal["H", "D"] = "H",
    ) -> List[Dict[str, str]]:
        """
        Obtenção de dados horários ou diários referentes a uma estação automática ou manual específica.

        Parameters
        ----------
        data_inicial : str
            Data de início do intervalo no formato AAAA-MM-DD.
        data_final : str
            Data final do intervalo no formato AAAA-MM-DD.
        cod_estacao : str
            Código da estação.
        freq : {'H', 'D'}
            Frequência dos dados, onde H se refere a dados horários e D, diários.
        Returns
        -------
            List[Dict[str, str]] : dados horários referentes a uma estação automática ou manual.
        """
        freq_ = "" if freq == "H" else "diaria/"
        url_requisicao = (
            f"{self.url_base}/estacao/{freq_}{data_inicial}/{data_final}/{cod_estacao}"
        )
        resposta = requests.get(url_requisicao)

        return resposta.json()

    def obter_dados_estacoes(self, dia: str, hora: str = None) -> List[Dict[str, str]]:
        """
        Obtenção de dados horários de todas as estações automáticas de um determinado dia.
        Caso desejado, pode ser solicitada uma hora específica para os dados.

        Parameters
        ----------
        dia : str
            Data dos dados no formato AAAA-MM-DD.

        hora : str.
            Hora dos dados, em UTC.

        Returns
        -------
            List[Dict[str, str]] : dados horários de todas as estações automáticas para a data especificada.
        """
        sufixo = f"{dia}/{hora}" if hora else dia
        url_requisicao = f"{self.url_base}/estacao/dados/{sufixo}"
        resposta = requests.get(url_requisicao)

        return resposta.json()

    def listar_estacoes(self, tipo: Literal["T", "M"] = "T") -> List[Dict[str, str]]:
        """
        Listagem de todas as estações de acordo com o tipo passado como parâmetro.

        Parameters
        ----------
        tipo : {"T", "M"}
            Tipo de estação, onde T se refere a estações automáticas e M, manuais.

        Returns
        -------
            List[Dict[str, str]] : Lista de estações.
        """
        url_requisicao = f"{self.url_base}/estacoes/{tipo}"
        resposta = requests.get(url_requisicao)

        return resposta.json()

    def obter_estacao_geocode(self, geocode: str) -> Dict[str, Dict[str, str]]:
        """
        Obtenção dos dados da estação mais próxima ao geocode passado como parâmetro.

        Parameters
        ----------
        geocode : str
            Tipo de estação, onde T se refere a estações automáticas e M, manuais.

        Returns
        -------
            Dict[str, Dict[str,str]] : dados de uma estação próxima ao geocode informado.
        """
        url_requisicao = f"https://apiprevmet3.inmet.gov.br/estacao/proxima/{geocode}"
        resposta = requests.get(url_requisicao)

        return resposta.json()
