"""Executa a análise exploratória e imprime os principais resultados."""

from pathlib import Path
import pandas as pd

from src.data_cleaning import clean_unicorn_data, explode_investors

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "startups_2021_end.csv"


def main() -> None:
    raw = pd.read_csv(DATA_PATH)
    df = clean_unicorn_data(raw)

    print("=== VISÃO GERAL ===")
    print(f"Empresas: {len(df):,}")
    print(f"Países: {df['Country'].nunique()}")
    print(f"Setores: {df['Industry'].nunique()}")
    print(f"Valuation total: US$ {df['Valuation_B'].sum():,.2f} bi")
    print(f"Valuation mediano: US$ {df['Valuation_B'].median():,.2f} bi")

    print("\n=== TOP 10 PAÍSES ===")
    print(df["Country"].value_counts().head(10))

    print("\n=== TOP 10 SETORES ===")
    print(df["Industry"].value_counts().head(10))

    print("\n=== TOP 10 VALUATIONS ===")
    cols = ["Company", "Valuation_B", "Country", "Industry"]
    print(df.nlargest(10, "Valuation_B")[cols].to_string(index=False))

    print("\n=== TOP 15 INVESTIDORES ===")
    print(explode_investors(df).value_counts().head(15))

    print("\n=== BRASIL ===")
    br = df[df["Country"] == "Brazil"].sort_values("Valuation_B", ascending=False)
    print(br[["Company", "Valuation_B", "City", "Industry"]].to_string(index=False))


if __name__ == "__main__":
    main()
