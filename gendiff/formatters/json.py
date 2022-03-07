import json
from gendiff.formatters.statuses import STATUS


def render_json(json_diff):
    return json.dumps(build_json_meta(json_diff))


def build_json_meta(diff):  # noqa C901
    output = []

    for item in diff:
        value = {
            'key': item['key'],
            'status': item['status']
        }

        if item['status'] == STATUS.ADDED:
            value['value'] = item['value']
        elif item['status'] == STATUS.DELETED:
            value['value'] = item['value']
        elif item['status'] == STATUS.CHANGED:
            value['old_value'] = item['old_value']
            value['new_value'] = item['new_value']
        elif item['status'] == STATUS.UNCHANGED:
            value['value'] = item['value']
        elif item['status'] == STATUS.NESTED:
            value['children'] = build_json_meta(item['children'])

        output.append(value)

    return output
