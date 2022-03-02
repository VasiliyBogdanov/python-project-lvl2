from gendiff.formatters.statuses import STATUS

INDENT = " "

INDENT_SIGNS = {
    "Added": "+",
    "Deleted": "-",
    "Unchanged": " ",
    "Nested": " "
}


def render_stylish(meta_tree):
    return "{\n" + "\n".join(build_stylish_meta(meta_tree)) + "\n}"


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


def build_stylish_meta(meta_tree, depth=1):  # noqa C901
    output = []

    for item in meta_tree:
        key = item['key']

        if item['status'] == STATUS.ADDED:
            output.append(format_value(key,
                                       item['value'],
                                       INDENT_SIGNS[STATUS.ADDED],
                                       depth))
        elif item['status'] == STATUS.DELETED:
            output.append(format_value(key,
                                       item['value'],
                                       INDENT_SIGNS[STATUS.DELETED],
                                       depth))
        elif item['status'] == STATUS.CHANGED:
            output.append(format_value(key,
                                       item['old_value'],
                                       INDENT_SIGNS[STATUS.DELETED],
                                       depth))
            output.append(format_value(key,
                                       item['new_value'],
                                       INDENT_SIGNS[STATUS.ADDED],
                                       depth))
        elif item['status'] == STATUS.UNCHANGED:
            output.append(format_value(key,
                                       item['value'],
                                       INDENT_SIGNS[STATUS.UNCHANGED],
                                       depth))
        elif item['status'] == STATUS.NESTED:
            indent = get_indent(depth)

            output.append(f"{indent}{INDENT_SIGNS[STATUS.NESTED]} {key}: {{")
            output.extend(build_stylish_meta(item['children'], depth + 1))
            output.append(f"  {indent}}}")

    return output
