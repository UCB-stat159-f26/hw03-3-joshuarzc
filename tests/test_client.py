import pytest

from tennis_career.client import _build_career_url, _fetch_career_js, _normalize_player_name


class MockResponse:
    def __init__(self, status_code, text=""):
        self.status_code = status_code
        self.text = text


def test_normalize_player_name():
    assert _normalize_player_name("serena williams") == "SerenaWilliams"
    assert _normalize_player_name("Serena Williams") == "SerenaWilliams"
    assert _normalize_player_name("SerenaWilliams") == "SerenaWilliams"


def test_normalize_player_name_rejects_empty_name():
    with pytest.raises(ValueError, match="non-empty"):
        _normalize_player_name("")


def test_build_career_url():
    expected = "https://www.tennisabstract.com/jsmatches/SerenaWilliamsCareer.js"

    assert _build_career_url("Serena Williams") == expected


def test_fetch_career_js_returns_response_text(monkeypatch):
    text = "var morematchmx = [];"

    def mock_get(url, timeout):
        assert url == _build_career_url("Serena Williams")
        assert timeout == 10
        return MockResponse(200, text)

    monkeypatch.setattr("tennis_career.client.requests.get", mock_get)

    assert _fetch_career_js("Serena Williams") == text


def test_fetch_career_js_reports_unknown_player(monkeypatch):
    def mock_get(url, timeout):
        return MockResponse(404)

    monkeypatch.setattr("tennis_career.client.requests.get", mock_get)

    with pytest.raises(ValueError, match="Could not find career data for Gaston Sanchez"):
        _fetch_career_js("Gaston Sanchez")
