"""Utilitários gerais."""
from pathlib import Path


def dir_projeto() -> Path:
    """
    Define a raíz do diretório do projeto.

    Returns
    -------
    Path
        Caminho para o projeto.
    """
    return Path(__file__).parent.parent
