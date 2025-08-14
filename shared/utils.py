import json
import re
def read_json_file(file_path: str) -> dict:
    """
    Reads a JSON file and returns its content as a dictionary.
    
    :param file_path: Path to the JSON file.
    :return: Dictionary containing the JSON data.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def get_cell_value(wb, typ, sheet, cells = ""):
    try:
        if typ == "cell":
            return wb[sheet][cells].value
        elif typ == "range":
            ws = wb[sheet]
            cells = ws[cells]
            return [[c.value for c in row] for row in cells]
        elif typ == "chart":
            return f"Chart at {cells}"  # Placeholder
    except Exception as e:
        return f"❌ {e.__class__.__name__}: {str(e)}"
    return "N/A"

def resolve_placeholders(text: str, placeholder_values: dict, wb) -> str:
    """
    Replaces {{variable}} placeholders in text with actual values from placeholder_values / Excel.
    - type "cell" → highlighted in yellow
    - type "range" → HTML table
    """
    pattern = r"\{\{(\w+)\}\}"

    def replacer(match):
        var = match.group(1)
        if var in placeholder_values:
            info = placeholder_values[var]
            if info["type"] == "cell":
                value = str(get_cell_value(wb, info["type"], info["sheet"], info["cells"]))
                return f'<span style="background-color: yellow">{value}</span>'
            elif info["type"] == "range":
                range_values = get_cell_value(wb, "range", info["sheet"], info["cells"])
                # convert 2D list to HTML table
                table_html = "<table style='border-collapse: collapse'>"
                for row in range_values:
                    table_html += "<tr>"
                    for cell in row:
                        table_html += f"<td style='border:1px solid black;padding:2px'>{cell}</td>"
                    table_html += "</tr>"
                table_html += "</table>"
                return table_html
            elif info["type"] == "chart":
                return f"<Chart placeholder: {info['cells']}>"
        return f"{{{{{var}}}}}"  # fallback keeps original placeholder

    # replace placeholders in text
    return re.sub(pattern, replacer, text)
