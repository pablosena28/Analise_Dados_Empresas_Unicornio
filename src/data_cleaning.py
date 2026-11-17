"""Funções de limpeza para o dataset de empresas unicórnio."""

from __future__ import annotations

import pandas as pd


def clean_unicorn_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpa e tipa as principais colunas do dataset."""
    data = df.copy()
    data = data.drop(columns=["Unnamed: 0"], errors="ignore")

    data["Valuation_B"] = (
        data["Valuation ($B)"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace("B", "", regex=False)
        .str.strip()
    )
    data["Valuation_B"] = pd.to_numeric(data["Valuation_B"], errors="coerce")

    data["Date_Joined"] = pd.to_datetime(data["Date Joined"], errors="coerce")
    data["Join_Year"] = data["Date_Joined"].dt.year.astype("Int64")

    data["City"] = data["City"].fillna("Não informado")
    data["Select Investors"] = data["Select Investors"].fillna("Não informado")

    return data


def explode_investors(df: pd.DataFrame) -> pd.Series:
    """Transforma a coluna de investidores em uma série com um investidor por linha."""
    return (
        df["Select Investors"]
        .replace("Não informado", pd.NA)
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
    )
