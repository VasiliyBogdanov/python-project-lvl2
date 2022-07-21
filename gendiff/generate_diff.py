import os

from gendiff.formatters.render_diff import OUTPUT_FORMAT_STYLISH
from gendiff.formatters.render_diff import render_diff
from gendiff.parsers.file_parser import parse_file_format
from gendiff.parsers.file_parser import read_file
from gendiff.statuses import STATUS
from gendiff.titles import (KEY_TITLE, STATUS_TITLE,
                            VALUE_TITLE, CHILDREN_TITLE,
                            OLD_VALUE_TITLE, NEW_VALUE_TITLE)


def build_diff(data_old, data_new):
    keys = sorted(data_old | data_new)
    output = []

    for key in keys:
        if key in data_old and key not in data_new:
            output.append({
                KEY_TITLE: key,
                STATUS_TITLE: STATUS.DELETED,
                VALUE_TITLE: data_old[key]
            })
        elif key not in data_old and key in data_new:
            output.append({
                KEY_TITLE: key,
                STATUS_TITLE: STATUS.ADDED,
                VALUE_TITLE: data_new[key]
            })
        elif isinstance(data_old[key], dict) and\
                isinstance(data_new[key], dict):
            output.append({
                KEY_TITLE: key,
                STATUS_TITLE: STATUS.NESTED,
                CHILDREN_TITLE: build_diff(data_old[key], data_new[key])
            })
        elif data_old[key] != data_new[key]:
            output.append({
                KEY_TITLE: key,
                STATUS_TITLE: STATUS.CHANGED,
                OLD_VALUE_TITLE: data_old[key],
                NEW_VALUE_TITLE: data_new[key]
            })
        else:
            output.append({
                KEY_TITLE: key,
                STATUS_TITLE: STATUS.UNCHANGED,
                VALUE_TITLE: data_old[key]
            })

    return output


def generate_diff(filepath_a: os.PathLike,
                  filepath_b: os.PathLike,
                  format_=OUTPUT_FORMAT_STYLISH) -> str:
    """
    Return diff between two files of json or yaml format.
    :param filepath_a: Path to first file
    :param filepath_b: Path to second file
    :param format_: Output format.
    Can be of these values: 'stylish', 'plain', 'json'.
    :return: Diff in specified format.
    """
    text_data1, extension1 = read_file(filepath_a)
    text_data2, extension2 = read_file(filepath_b)

    file1 = parse_file_format(text_data1, extension1)
    file2 = parse_file_format(text_data2, extension2)

    diff = build_diff(file1, file2)

    return render_diff(diff, format_)
