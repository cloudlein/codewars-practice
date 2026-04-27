import pytest
from solution import  string_to_array


@pytest.mark.parametrize("input_value, expected", [
    ("Robin Singh", ["Robin", "Singh"]),
    ("CodeWars", ["CodeWars"]),
    ("I love arrays they are my favorite", ["I", "love", "arrays", "they", "are", "my", "favorite"]),
    ("1 2 3", ["1", "2", "3"]),
    ("", [""]),
])
def test_string_to_array(input_value, expected):
    assert string_to_array(input_value) == expected
