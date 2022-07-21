import json

from gendiff.statuses import STATUS
from gendiff.titles import (KEY_TITLE, STATUS_TITLE,
                            VALUE_TITLE, CHILDREN_TITLE,
                            OLD_VALUE_TITLE, NEW_VALUE_TITLE)


def render_json(json_diff):
    return json.dumps(build_json(json_diff))


def build_json(diff):  # noqa C901
    output = []

    for item in diff:
        value = {
            KEY_TITLE: item[KEY_TITLE],
            STATUS_TITLE: item[STATUS_TITLE]
        }

        if item[STATUS_TITLE] == STATUS.ADDED:
            value[VALUE_TITLE] = item[VALUE_TITLE]
        elif item[STATUS_TITLE] == STATUS.DELETED:
            value[VALUE_TITLE] = item[VALUE_TITLE]
        elif item[STATUS_TITLE] == STATUS.CHANGED:
            value[OLD_VALUE_TITLE] = item[OLD_VALUE_TITLE]
            value[NEW_VALUE_TITLE] = item[NEW_VALUE_TITLE]
        elif item[STATUS_TITLE] == STATUS.UNCHANGED:
            value[VALUE_TITLE] = item[VALUE_TITLE]
        elif item[STATUS_TITLE] == STATUS.NESTED:
            value[CHILDREN_TITLE] = build_json(item[CHILDREN_TITLE])

        output.append(value)

    return output
