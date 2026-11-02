import pandas as pd


OUTPUT_COLUMNS = [
    "match_date",
    "tournament",
    "surface",
    "result",
    "opponent",
    "player_age",
    "opponent_age",
    "age_difference",
]


def _select_match_fields(records):
    """Select the fields needed for cleaning from raw match records."""
    matches = pd.DataFrame(records).iloc[:, [0, 1, 2, 4, 11, 16]]
    matches.columns = ["match_date", "tournament", "surface", "result", "opponent", "opponent_data"]
    return matches


def _add_opponent_age(matches):
    """Add opponent ages from birth dates or existing age values."""
    values = matches.pop("opponent_data").replace("", pd.NA)
    if values.str.fullmatch(r"\d{8}").any():
        birthdays = pd.to_datetime(values, format="%Y%m%d", errors="coerce")
        matches["opponent_age"] = (matches["match_date"] - birthdays).dt.days / 365.25
    else:
        matches["opponent_age"] = pd.to_numeric(values, errors="coerce")


def _clean_career_records(records, player_birth_date):
    """
    Convert career records into a clean match-level data frame.

    Parameters:
    records : Match records returned by _parse_career_js().
    player_birth_date : The player's date of birth.

    Returns:
    A data frame with match information, player age, opponent age, and age difference.

    Raises:
    ValueError: If match dates or the player birth date cannot be parsed.
    """
    matches = _select_match_fields(records)
    matches["match_date"] = pd.to_datetime(matches["match_date"], format="%Y%m%d")
    matches["result"] = matches["result"].map({"W": "won", "L": "lost"})
    matches["player_age"] = (matches["match_date"] - pd.Timestamp(player_birth_date)).dt.days / 365.25
    _add_opponent_age(matches)
    matches = matches.dropna(subset=["player_age", "opponent_age"])
    matches["age_difference"] = matches["player_age"] - matches["opponent_age"]
    return matches[OUTPUT_COLUMNS]
