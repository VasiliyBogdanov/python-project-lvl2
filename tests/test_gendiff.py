from gendiff import generate_diff

# Plain JSON
plain_json_filepath1 = "tests/fixtures/file1.json"
plain_json_filepath2 = "tests/fixtures/file2.json"
plain_json_result_filepath = "tests/fixtures/plain_json_result.txt"


def test_gendiff():
    with open(plain_json_result_filepath, mode="r") as f:
        result = f.read()
    assert generate_diff(plain_json_filepath1, plain_json_filepath2) == result
