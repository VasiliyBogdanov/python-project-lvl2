from gendiff.statuses import STATUS
from gendiff.titles import (KEY_TITLE, STATUS_TITLE,
                            VALUE_TITLE, CHILDREN_TITLE,
                            OLD_VALUE_TITLE, NEW_VALUE_TITLE)
INDENT = " "

INDENT_SIGNS = {
    "Added": "+",
    "Deleted": "-",
    "Unchanged": " ",
    "Nested": " "
}


def render_stylish(stylish_diff):
    return "{\n" + "\n".join(build_stylish(stylish_diff)) + "\n}"


def get_indent(depth):
    return INDENT * (4 * depth - 2)


def format_value(key, value, sign, depth):
    indent = get_indent(depth)

    if isinstance(value, dict):
        nested_str = [f"{indent}{sign} {key}: {{"]

        for key in value:
            nested_str.append(format_value(key,
                                           value[key],
                                           INDENT_SIGNS[STATUS.NESTED],
                                           depth + 1))

        nested_str.append(f"  {indent}}}")
        return "\n".join(nested_str)
    else:
        if isinstance(value, bool):
            output_value = str(value).lower()
        elif value is None:
            output_value = "null"
        else:
            output_value = value

        return f"{indent}{sign} {key}: {output_value}"


def build_stylish(diff, depth=1):  # noqa C901
    output = []

    for item in diff:
        key = item[KEY_TITLE]

        if item[STATUS_TITLE] == STATUS.ADDED:
            output.append(format_value(key,
                                       item[VALUE_TITLE],
                                       INDENT_SIGNS[STATUS.ADDED],
                                       depth))
        elif item[STATUS_TITLE] == STATUS.DELETED:
            output.append(format_value(key,
                                       item[VALUE_TITLE],
                                       INDENT_SIGNS[STATUS.DELETED],
                                       depth))
        elif item[STATUS_TITLE] == STATUS.CHANGED:
            output.append(format_value(key,
                                       item[OLD_VALUE_TITLE],
                                       INDENT_SIGNS[STATUS.DELETED],
                                       depth))
            output.append(format_value(key,
                                       item[NEW_VALUE_TITLE],
                                       INDENT_SIGNS[STATUS.ADDED],
                                       depth))
        elif item[STATUS_TITLE] == STATUS.UNCHANGED:
            output.append(format_value(key,
                                       item[VALUE_TITLE],
                                       INDENT_SIGNS[STATUS.UNCHANGED],
                                       depth))
        elif item[STATUS_TITLE] == STATUS.NESTED:
            indent = get_indent(depth)

            output.append(f"{indent}{INDENT_SIGNS[STATUS.NESTED]} {key}: {{")
            output.extend(build_stylish(item[CHILDREN_TITLE], depth + 1))
            output.append(f"  {indent}}}")

    return output
