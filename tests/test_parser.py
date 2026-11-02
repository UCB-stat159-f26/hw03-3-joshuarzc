import pytest

from tennis_career.parser import _parse_career_js, _parse_player_birth_date


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


def test_parse_player_birth_date():
    with open("tests/mock_data/player_metadata.js") as file:
        birth_date = _parse_player_birth_date(file.read())

    assert birth_date == "1981-09-26"


def test_parse_player_birth_date_rejects_missing_date():
    with pytest.raises(ValueError, match="date of birth"):
        _parse_player_birth_date("var fullname = 'Unknown Player';")
