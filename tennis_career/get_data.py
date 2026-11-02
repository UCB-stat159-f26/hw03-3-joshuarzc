from .client import _fetch_career_js, _fetch_player_metadata
from .parser import _parse_career_js, _parse_player_birth_date
from .transform import _clean_career_records


def get_career_matches(player_name):
    """
    Retrieve and clean career match data for a tennis player.

    Parameters:
    player_name : A player name accepted by Tennis Abstract.

    Returns:
    A clean data frame with one row per career match.

    Raises:
    ValueError: If player data cannot be retrieved or parsed.
    """
    career_text = _fetch_career_js(player_name)
    metadata_text = _fetch_player_metadata(player_name)
    records = _parse_career_js(career_text)
    birth_date = _parse_player_birth_date(metadata_text)
    return _clean_career_records(records, birth_date)
