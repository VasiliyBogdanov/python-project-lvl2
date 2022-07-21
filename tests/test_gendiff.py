from gendiff.generate_diff import build_diff, generate_diff

from tests.fixtures.build_diff_results import FLAT_RESULT
from tests.fixtures.build_diff_results import NESTED_RESULT
import pytest
from tests.conftest import (prepare_file,
                            open_result_file,
                            FLAT_JSON_FILEPATH1, FLAT_JSON_FILEPATH2,
                            NESTED_JSON_FILEPATH1, NESTED_JSON_FILEPATH2,
                            FLAT_YAML_FILEPATH1, FLAT_YAML_FILEPATH2,
                            NESTED_YAML_FILEPATH1, NESTED_YAML_FILEPATH2,
                            STYLISH_FLAT_RESULT_FILEPATH,
                            STYLISH_NESTED_RESULT_FILEPATH,
                            PLAIN_FLAT_RESULT_FILEPATH,
                            PLAIN_NESTED_RESULT_FILEPATH,
                            JSON_FLAT_RESULT_FILEPATH,
                            JSON_NESTED_RESULT_FILEPATH,
                            )
from gendiff.formatters.render_diff import (OUTPUT_FORMAT_STYLISH,
                                            OUTPUT_FORMAT_PLAIN,
                                            OUTPUT_FORMAT_JSON)


@pytest.mark.parametrize("test_input, expected", [
    # stylish formatter
    (generate_diff(FLAT_JSON_FILEPATH1, FLAT_JSON_FILEPATH2,
                   OUTPUT_FORMAT_STYLISH),
     open_result_file(STYLISH_FLAT_RESULT_FILEPATH)),
    (generate_diff(NESTED_JSON_FILEPATH1, NESTED_JSON_FILEPATH2,
                   OUTPUT_FORMAT_STYLISH),
     open_result_file(STYLISH_NESTED_RESULT_FILEPATH)),
    # plain formatter
    (generate_diff(FLAT_JSON_FILEPATH1, FLAT_JSON_FILEPATH2,
                   OUTPUT_FORMAT_PLAIN),
     open_result_file(PLAIN_FLAT_RESULT_FILEPATH)),
    (generate_diff(NESTED_JSON_FILEPATH1, NESTED_JSON_FILEPATH2,
                   OUTPUT_FORMAT_PLAIN),
     open_result_file(PLAIN_NESTED_RESULT_FILEPATH)),
    # # json formatter
    (generate_diff(FLAT_JSON_FILEPATH1, FLAT_JSON_FILEPATH2,
                   OUTPUT_FORMAT_JSON),
     open_result_file(JSON_FLAT_RESULT_FILEPATH)),
    (generate_diff(NESTED_JSON_FILEPATH1, NESTED_JSON_FILEPATH2,
                   OUTPUT_FORMAT_JSON),
     open_result_file(JSON_NESTED_RESULT_FILEPATH)),
])
def test_generate_diff(test_input, expected):
    assert test_input == expected


@pytest.mark.parametrize("test_input, expected", [
    (build_diff(prepare_file(FLAT_JSON_FILEPATH1),
                prepare_file(FLAT_JSON_FILEPATH2)),
     FLAT_RESULT),
    (build_diff(prepare_file(NESTED_JSON_FILEPATH1),
                prepare_file(NESTED_JSON_FILEPATH2)),
     NESTED_RESULT),
    (build_diff(prepare_file(FLAT_YAML_FILEPATH1),
                prepare_file(FLAT_YAML_FILEPATH2)),
     FLAT_RESULT),
    (build_diff(prepare_file(NESTED_YAML_FILEPATH1),
                prepare_file(NESTED_YAML_FILEPATH2)),
     NESTED_RESULT)
])
def test_build_diff(test_input, expected):
    assert test_input == expected
