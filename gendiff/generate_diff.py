import json
import os
import yaml
from gendiff.K import STATUS
from gendiff.formatters.stylish import render_stylish


def _prepare_file(filepath):
    file_format = os.path.splitext(filepath)[-1]
    if file_format == ".json":
        with open(filepath, mode="r") as f:
            file = json.load(f)
    elif file_format in (".yml", ".yaml"):
        with open(filepath, mode="r") as f:
            file = yaml.safe_load(f)
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


def choose_format(meta_tree, format_):
    if format_ == "stylish":
        return render_stylish(meta_tree)


def generate_diff(filepath_a, filepath_b):
    file1 = _prepare_file(filepath_a)
    file2 = _prepare_file(filepath_b)
    return build_diff_meta_tree(file1, file2)
