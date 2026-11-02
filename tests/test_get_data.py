import pytest

from tennis_career import get_career_matches


def test_get_career_matches(monkeypatch):
    with open("tests/mock_data/female_player_career.js") as file:
        career_text = file.read()
    with open("tests/mock_data/player_metadata.js") as file:
        metadata_text = file.read()

    def mock_fetch_career_js(player_name):
        return career_text

    def mock_fetch_player_metadata(player_name):
        return metadata_text

    monkeypatch.setattr("tennis_career.get_data._fetch_career_js", mock_fetch_career_js)
    monkeypatch.setattr("tennis_career.get_data._fetch_player_metadata", mock_fetch_player_metadata)

    matches = get_career_matches("Serena Williams")

    assert len(matches) == 3
    assert matches.iloc[0]["result"] == "lost"
    assert matches.iloc[0]["age_difference"] == pytest.approx(-4.684463, abs=0.001)
