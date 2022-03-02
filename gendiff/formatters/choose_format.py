from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json

OUTPUT_FORMAT_STYLISH = "stylish"
OUTPUT_FORMAT_PLAIN = "plain"
OUTPUT_FORMAT_JSON = "json"


def choose_format(meta_tree, format_):
    format_ = format_.lower()
    if format_ == "stylish":
        return render_stylish(meta_tree)
    elif format_ == "plain":
        return render_plain(meta_tree)
    elif format_ == "json":
        return render_json(meta_tree)
