import json

def read_json_file(file_path: str) -> dict:
    """
    Reads a JSON file and returns its content as a dictionary.
    
    :param file_path: Path to the JSON file.
    :return: Dictionary containing the JSON data.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)