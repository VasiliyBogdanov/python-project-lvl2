from gendiff.statuses import STATUS
from gendiff.titles import (KEY_TITLE, STATUS_TITLE,
                            VALUE_TITLE, CHILDREN_TITLE,
                            OLD_VALUE_TITLE, NEW_VALUE_TITLE)

PLAIN_MESSAGE = {
    "Added": "Property '{path_added}' was added with value: {value_added}",
    "Deleted": "Property '{path_deleted}' was removed",
    "Changed": "Property '{path_changed}' was updated. From {old_value} to {new_value}"  # noqa E501
}


def render_plain(plain_diff):
    return "\n".join(build_plain(plain_diff))


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif isinstance(value, str):
        return f"'{value}'"

    elif isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    return str(value)


def build_plain(diff, path=""):
    output = []

    for item in diff:
        path_modified = f'{path}{item[KEY_TITLE]}'

        if item[STATUS_TITLE] == STATUS.ADDED:
            output.append(PLAIN_MESSAGE[STATUS.ADDED]
                          .format(path_added=path_modified,
                                  value_added=format_value(item[VALUE_TITLE])))
        elif item[STATUS_TITLE] == STATUS.DELETED:
            output.append(PLAIN_MESSAGE[STATUS.DELETED]
                          .format(path_deleted=path_modified))
        elif item[STATUS_TITLE] == STATUS.CHANGED:
            output.append(PLAIN_MESSAGE[STATUS.CHANGED]
                          .format(path_changed=path_modified,
                                  old_value=format_value(item[OLD_VALUE_TITLE]),
                                  new_value=format_value(
                                      item[NEW_VALUE_TITLE])))
        elif item[STATUS_TITLE] == STATUS.NESTED:
            output.extend(build_plain(item[CHILDREN_TITLE],
                                      f'{path_modified}.'))

    return output
