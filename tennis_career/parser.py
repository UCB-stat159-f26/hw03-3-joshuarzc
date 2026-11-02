import json
import re


def _parse_career_js(js_text):
    """
    Parse match records from a Tennis Abstract career JavaScript file.

    Parameters:
    js_text : Text read from a player career JavaScript file.

    Returns:
    Match records stored in the `morematchmx` array.

    Raises:
    ValueError: If `morematchmx` is missing or cannot be parsed as JSON.
    """
    prefix = "var morematchmx ="
    if prefix not in js_text:
        raise ValueError("Could not find morematchmx data.")

    data = js_text.split("=", 1)[1].rstrip(";\n ")
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        raise ValueError("Could not parse morematchmx data.")


def _parse_player_birth_date(metadata_text):
    """
    Extract a player birth date from Tennis Abstract metadata JavaScript.

    Parameters:
    metadata_text : Text read from a player metadata JavaScript file.

    Returns:
    The player birth date in YYYY-MM-DD format.

    Raises:
    ValueError: If a player date of birth cannot be found.
    """
    match = re.search(r"var\s+dob\s*=\s*['\"]?(\d{8})['\"]?\s*;", metadata_text)
    if not match:
        raise ValueError("Could not find player date of birth.")

    birth_date = match.group(1)
    return f"{birth_date[:4]}-{birth_date[4:6]}-{birth_date[6:]}"
