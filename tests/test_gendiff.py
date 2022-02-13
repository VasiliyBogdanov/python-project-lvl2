import pytest

from gendiff import generate_diff

# Plain JSON
plain_json_filepath1 = "tests/fixtures/file1.json"
plain_json_filepath2 = "tests/fixtures/file2.json"
plain_json_result_filepath = "tests/fixtures/plain_result.txt"
plain_yaml_filepath1 = "tests/fixtures/file1.yml"
plain_yaml_filepath2 = "tests/fixtures/file2.yaml"

@pytest.fixture
def plain_json_result():
    with open(plain_json_result_filepath, mode="r") as f:
        result = f.read()
    return result


def test_gendiff_plain_json(plain_json_result):
    assert generate_diff(plain_json_filepath1, plain_json_filepath2, "json") == plain_json_result


def test_gendiff_plain_yaml(plain_json_result):
    assert generate_diff(plain_yaml_filepath1, plain_yaml_filepath2, "json") == plain_json_result


def test_gendiff_json_to_yaml(plain_json_result):
    assert generate_diff(plain_yaml_filepath1, plain_json_filepath2, "json") == plain_json_result
