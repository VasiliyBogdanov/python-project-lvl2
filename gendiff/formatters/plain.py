from gendiff.formatters.statuses import STATUS

PLAIN_MESSAGE = {
    "Added": "Property '{path_added}' was added with value: {value_added}",
    "Deleted": "Property '{path_deleted}' was removed",
    "Changed": "Property '{path_changed}' was updated. From {old_value} to {new_value}"  # noqa E501
}


def render_plain(plain_diff):
    return "\n".join(build_plain_meta(plain_diff))


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'

    if isinstance(value, str):
        return f"'{value}'"

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return 'null'

    return str(value)


def build_plain_meta(diff, path=""):
    output = []

    for item in diff:
        path_modified = f'{path}{item["key"]}'

        if item['status'] == STATUS.ADDED:
            output.append(PLAIN_MESSAGE[STATUS.ADDED]
                          .format(path_added=path_modified,
                                  value_added=format_value(item['value'])))
        if item['status'] == STATUS.DELETED:
            output.append(PLAIN_MESSAGE[STATUS.DELETED]
                          .format(path_deleted=path_modified))
        if item['status'] == STATUS.CHANGED:
            output.append(PLAIN_MESSAGE[STATUS.CHANGED]
                          .format(path_changed=path_modified,
                                  old_value=format_value(item['old_value']),
                                  new_value=format_value(item['new_value'])))
        if item['status'] == STATUS.NESTED:
            output.extend(build_plain_meta(item['children'],
                                           f'{path_modified}.'))

    return output
