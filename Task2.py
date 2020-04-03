import json

def serializer_json(obj):
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        if obj is True:
            return "true"
        else:
            return "false"
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return '"' + obj + '"'
    elif isinstance(obj, (tuple, set, list, frozenset)):
        result = ', '.join(serializer_json(el) for el in obj)
        return "[" + result + "]"
    elif isinstance(obj, dict):
        temp = []
        for key, value in obj.items():
                temp.append("" + serializer_json(key) + ": " + serializer_json(value))
        result = ", ".join(pair for pair in temp)
        return "{" + result + "}"
    else:
        raise TypeError("Error" + str(type(obj)) + " is not JSON serializable")

if __name__ == "__main__":
    my_dict = {
        True: False,
        1: 1,
        "List": ["i", 2, "singing"],
        "Wath": 35,
    }
    print(serializer_json(my_dict))
    print(json.dumps(my_dict))
