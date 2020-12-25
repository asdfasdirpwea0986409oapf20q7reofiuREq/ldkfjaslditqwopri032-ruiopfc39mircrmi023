def decodeSchema(schemaJSON, columns):
    length = len(columns)
    output = []
    for indice in range(length):
        key = columns[indice]
        value = schemaJSON[key]
        if key == "id":
            line = key + " " + value + " UNIQUE"
        else:
            line = key + " " + value
        if indice < length - 1:
            line = line + ","
        output.append(line)
    return " ".join(output)

def rowToJSONMapping(schemaJSON, columns):
    length = len(columns)
    output = ["entry = {}"]
    for indice in range(length):
        json = f'entry["{columns[indice]}"]'
        row = f"row[{str(indice)}]"
        line = json + " = " + row
        output.append(line)
    output.append("output.append(entry)")
    return "\n".join(output)