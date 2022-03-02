from gendiff.parser.arg_parser import check_file_format
from gendiff.formatters.choose_format import choose_format
from gendiff.parser.loader import load_file
from gendiff.formatters.choose_format import OUTPUT_FORMAT_STYLISH
from gendiff.formatters.statuses import STATUS


# К пункту 3: Зачем нам читать любой файл, если в ТЗ строго прописаны форматы?
def prepare_file(filepath):
    file_format = check_file_format(filepath)
    file = load_file(filepath, file_format)
    return file


def build_diff_meta_tree(data_old, data_new):
    keys = sorted(data_old | data_new)
    meta_tree = []

    for key in keys:
        if key in data_old and key not in data_new:
            meta_tree.append({
                "key": key,
                "status": STATUS.DELETED,
                "value": data_old[key]
            })
        elif key not in data_old and key in data_new:
            meta_tree.append({
                "key": key,
                "status": STATUS.ADDED,
                "value": data_new[key]
            })
        elif isinstance(data_old[key], dict) and\
                isinstance(data_new[key], dict):
            meta_tree.append({
                "key": key,
                "status": STATUS.NESTED,
                "children": build_diff_meta_tree(data_old[key], data_new[key])
            })
        elif data_old[key] != data_new[key]:
            meta_tree.append({
                "key": key,
                "status": STATUS.CHANGED,
                "old_value": data_old[key],
                "new_value": data_new[key]
            })
        else:
            meta_tree.append({
                "key": key,
                "status": STATUS.UNCHANGED,
                "value": data_old[key]
            })

    return meta_tree


def generate_diff(filepath_a, filepath_b, format_=OUTPUT_FORMAT_STYLISH):
    file1 = prepare_file(filepath_a)
    file2 = prepare_file(filepath_b)
    return choose_format(build_diff_meta_tree(file1,
                                              file2), format_)
