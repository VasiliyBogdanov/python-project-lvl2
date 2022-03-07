from gendiff.formatters.render_diff import render_diff
from gendiff.formatters.render_diff import OUTPUT_FORMAT_STYLISH
from gendiff.formatters.statuses import STATUS
from gendiff.parsers.file_parser import parse_file_format
from gendiff.parsers.file_parser import read_file


def build_diff(data_old, data_new):
    keys = sorted(data_old | data_new)
    output = []

    for key in keys:
        if key in data_old and key not in data_new:
            output.append({
                "key": key,
                "status": STATUS.DELETED,
                "value": data_old[key]
            })
        elif key not in data_old and key in data_new:
            output.append({
                "key": key,
                "status": STATUS.ADDED,
                "value": data_new[key]
            })
        elif isinstance(data_old[key], dict) and\
                isinstance(data_new[key], dict):
            output.append({
                "key": key,
                "status": STATUS.NESTED,
                "children": build_diff(data_old[key], data_new[key])
            })
        elif data_old[key] != data_new[key]:
            output.append({
                "key": key,
                "status": STATUS.CHANGED,
                "old_value": data_old[key],
                "new_value": data_new[key]
            })
        else:
            output.append({
                "key": key,
                "status": STATUS.UNCHANGED,
                "value": data_old[key]
            })

    return output


def generate_diff(filepath_a, filepath_b, format_=OUTPUT_FORMAT_STYLISH):
    text_data1, extension1 = read_file(filepath_a)
    text_data2, extension2 = read_file(filepath_b)

    file1 = parse_file_format(text_data1, extension1)
    file2 = parse_file_format(text_data2, extension2)

    diff = build_diff(file1, file2)

    return render_diff(diff, format_)
