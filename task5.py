from task2 import serializer_json
import json


def test_json():
    test_1 = "12"
    test_2 = 12
    test_3 = "[1,2,3,4]"
    test_4 = "true"
    test_5 = {"I": "want", "get": "9", "or": "10"}
    test_6 = {"Python": 7.6, "tr": 2}
    test_7 = "null"
    assert serializer_json(test_1) == json.dumps(test_1)
    assert serializer_json(test_2) == json.dumps(test_2)
    assert serializer_json(test_3) == json.dumps(test_3)
    assert serializer_json(test_4) == json.dumps(test_4)
    assert serializer_json(test_5) == json.dumps(test_5)
    assert serializer_json(test_6) == json.dumps(test_6)
    assert serializer_json(test_7) == json.dumps(test_7)


if __name__ == "__main__":
    test_json()
