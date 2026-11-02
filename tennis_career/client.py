import requests


CAREER_URL = "https://www.tennisabstract.com/jsmatches/{player_id}Career.js"
PLAYER_METADATA_URL = "https://www.tennisabstract.com/jsmatches/{player_id}.js"


def _normalize_player_name(player_name):
    """Convert a player name to the Tennis Abstract identifier format."""
    if not isinstance(player_name, str) or not player_name.strip():
        raise ValueError("Player name must be a non-empty string.")

    parts = player_name.split()
    if len(parts) == 1:
        return parts[0][0].upper() + parts[0][1:]
    return "".join(part.capitalize() for part in parts)


def _build_career_url(player_name):
    """Build the Tennis Abstract career JavaScript URL for a player."""
    return CAREER_URL.format(player_id=_normalize_player_name(player_name))


def _build_player_metadata_url(player_name):
    """Build the Tennis Abstract player metadata JavaScript URL."""
    return PLAYER_METADATA_URL.format(player_id=_normalize_player_name(player_name))


def _fetch_career_js(player_name):
    """
    Retrieve career JavaScript text from Tennis Abstract.

    Parameters:
    player_name : A player name accepted by _normalize_player_name().

    Returns:
    Career JavaScript text containing the `morematchmx` array.

    Raises:
    ValueError: If the player cannot be found or career data cannot be retrieved.
    """
    try:
        response = requests.get(_build_career_url(player_name), timeout=10)
    # Handle network-related errors
    except requests.RequestException:
        raise ValueError(f"Could not retrieve career data for {player_name}.")

    # Handle HTTP errors
    if response.status_code == 404:
        raise ValueError(f"Could not find career data for {player_name}.")
    
    # Handle unexpected content
    if response.status_code != 200 or "var morematchmx =" not in response.text:
        raise ValueError(f"Could not retrieve career data for {player_name}.")
    
    return response.text


def _fetch_player_metadata(player_name):
    """
    Retrieve player metadata JavaScript text from Tennis Abstract.

    Parameters:
    player_name : A player name accepted by _normalize_player_name().

    Returns:
    Player metadata JavaScript text.

    Raises:
    ValueError: If the player cannot be found or metadata cannot be retrieved.
    """
    try:
        response = requests.get(_build_player_metadata_url(player_name), timeout=10)
    except requests.RequestException:
        raise ValueError(f"Could not retrieve player metadata for {player_name}.")

    if response.status_code == 404:
        raise ValueError(f"Could not find player metadata for {player_name}.")
    if response.status_code != 200:
        raise ValueError(f"Could not retrieve player metadata for {player_name}.")
    return response.text
