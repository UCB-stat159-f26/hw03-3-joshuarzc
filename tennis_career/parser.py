import json


def parse_career_js(js_text):
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
