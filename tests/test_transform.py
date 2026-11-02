import pytest

from tennis_career.parser import _parse_career_js
from tennis_career.transform import _clean_career_records


EXPECTED_COLUMNS = [
    "match_date",
    "tournament",
    "surface",
    "result",
    "opponent",
    "player_age",
    "opponent_age",
    "age_difference",
]


def test_clean_female_career_records():
    with open("tests/mock_data/female_player_career.js") as file:
        records = _parse_career_js(file.read())

    matches = _clean_career_records(records, "1981-09-26")
    first_match = matches.iloc[0]

    assert list(matches.columns) == EXPECTED_COLUMNS
    assert len(matches) == 3
    assert first_match["result"] == "lost"
    assert first_match["player_age"] == pytest.approx(14.091718, abs=0.001)
    assert first_match["opponent_age"] == pytest.approx(18.776181, abs=0.001)
    assert first_match["age_difference"] == pytest.approx(-4.684463, abs=0.001)


def test_clean_male_career_records():
    with open("tests/mock_data/male_player_career.js") as file:
        records = _parse_career_js(file.read())

    matches = _clean_career_records(records, "1986-06-03")
    first_match = matches.iloc[0]

    assert list(matches.columns) == EXPECTED_COLUMNS
    assert len(matches) == 3
    assert first_match["result"] == "lost"
    assert first_match["player_age"] == pytest.approx(15.271732, abs=0.001)
    assert first_match["opponent_age"] == pytest.approx(22.264203, abs=0.001)
    assert first_match["age_difference"] == pytest.approx(-6.992471, abs=0.001)
