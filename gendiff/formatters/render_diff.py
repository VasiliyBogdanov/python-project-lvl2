from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json

OUTPUT_FORMAT_STYLISH = "stylish"
OUTPUT_FORMAT_PLAIN = "plain"
OUTPUT_FORMAT_JSON = "json"


def render_diff(diff, format_):
    format_ = format_.lower()
    if format_ == OUTPUT_FORMAT_STYLISH:
        return render_stylish(diff)
    elif format_ == OUTPUT_FORMAT_PLAIN:
        return render_plain(diff)
    elif format_ == OUTPUT_FORMAT_JSON:
        return render_json(diff)
