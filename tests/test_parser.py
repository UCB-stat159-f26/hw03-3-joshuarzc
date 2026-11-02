import pytest

from tennis_career.parser import _parse_career_js


def test_parse_female_career_js():
    with open("tests/mock_data/female_player_career.js") as file:
        records = _parse_career_js(file.read())

    assert len(records) == 3
    assert records[0][0] == "19951030"


def test_parse_male_career_js():
    with open("tests/mock_data/male_player_career.js") as file:
        records = _parse_career_js(file.read())

    assert len(records) == 3
    assert records[0][0] == "20010910"


def test_parse_career_js_rejects_missing_match_data():
    with pytest.raises(ValueError, match="morematchmx"):
        _parse_career_js("var matchmx = [];")
