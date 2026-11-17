import pandas as pd

from src.data_cleaning import clean_unicorn_data, explode_investors


def test_clean_unicorn_data_converts_valuation_and_date():
    sample = pd.DataFrame(
        {
            "Company": ["Teste"],
            "Valuation ($B)": ["$2.5"],
            "Date Joined": ["4/7/2021"],
            "Country": ["Brazil"],
            "City": [None],
            "Industry": ["Fintech"],
            "Select Investors": ["Alpha, Beta"],
        }
    )

    cleaned = clean_unicorn_data(sample)

    assert cleaned.loc[0, "Valuation_B"] == 2.5
    assert cleaned.loc[0, "Join_Year"] == 2021
    assert cleaned.loc[0, "City"] == "Não informado"


def test_explode_investors_splits_values():
    sample = pd.DataFrame({"Select Investors": ["Alpha, Beta", "Alpha"]})
    investors = explode_investors(sample).tolist()

    assert investors == ["Alpha", "Beta", "Alpha"]
