import json
from gendiff.K import STATUS


def render_json(json_meta_tree, indent=0):
    return json.dumps(build_json_meta(json_meta_tree), indent=indent)


def build_json_meta(meta_tree):  # noqa C901
    output = []

    for item in meta_tree:
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
