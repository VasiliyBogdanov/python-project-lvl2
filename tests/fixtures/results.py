flat_result_meta = [
    {'key': 'follow', 'status': 'Deleted', 'value': False},
    {'key': 'host', 'status': 'Unchanged', 'value': 'hexlet.io'},
    {'key': 'proxy', 'status': 'Deleted', 'value': '123.234.53.22'},
    {'key': 'timeout', 'new_value': 20, 'old_value': 50, 'status': 'Changed'},
    {'key': 'verbose', 'status': 'Added', 'value': True}
]

nested_result_meta = [
    {'children': [
        {'key': 'follow', 'status': 'Added', 'value': False},
        {'key': 'setting1', 'status': 'Unchanged', 'value': 'Value 1'},
        {'key': 'setting2', 'status': 'Deleted', 'value': 200},
        {'key': 'setting3', 'new_value': None, 'old_value': True, 'status': 'Changed'},
        {'key': 'setting4', 'status': 'Added', 'value': 'blah blah'},
        {'key': 'setting5', 'status': 'Added', 'value': {'key5': 'value5'}},
        {'children': [
            {'children': [
                {'key': 'wow', 'new_value': 'so much', 'old_value': '', 'status': 'Changed'}
            ],
                'key': 'doge', 'status': 'Nested'},
            {'key': 'key', 'status': 'Unchanged', 'value': 'value'},
            {'key': 'ops', 'status': 'Added', 'value': 'vops'}
        ],
            'key': 'setting6', 'status': 'Nested'}
    ],
        'key': 'common',
        'status': 'Nested'},
    {'children': [
        {'key': 'baz', 'new_value': 'bars', 'old_value': 'bas', 'status': 'Changed'},
        {'key': 'foo', 'status': 'Unchanged', 'value': 'bar'},
        {'key': 'nest', 'new_value': 'str', 'old_value':
            {'key': 'value'},
         'status': 'Changed'}
    ],
        'key': 'group1',
        'status': 'Nested'},
    {'key': 'group2',
     'status': 'Deleted',
     'value': {
         'abc': 12345,
         'deep': {
             'id': 45
         }
     }
     },
    {'key': 'group3',
     'status': 'Added',
     'value': {
         'deep': {
             'id': {
                 'number': 45}
         },
         'fee': 100500
     }
     }
]

stylish_flat_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

plain_flat_result = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

plain_nested_result = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

json_flat_result = '[{"key": "follow", "status": "Deleted", "value": false}, {"key": "host", "status": "Unchanged", "value": "hexlet.io"}, {"key": "proxy", "status": "Deleted", "value": "123.234.53.22"}, {"key": "timeout", "status": "Changed", "old_value": 50, "new_value": 20}, {"key": "verbose", "status": "Added", "value": true}]'  # noqa E501

json_nested_result = '[{"key": "common", "status": "Nested", "children": [{"key": "follow", "status": "Added", "value": false}, {"key": "setting1", "status": "Unchanged", "value": "Value 1"}, {"key": "setting2", "status": "Deleted", "value": 200}, {"key": "setting3", "status": "Changed", "old_value": true, "new_value": null}, {"key": "setting4", "status": "Added", "value": "blah blah"}, {"key": "setting5", "status": "Added", "value": {"key5": "value5"}}, {"key": "setting6", "status": "Nested", "children": [{"key": "doge", "status": "Nested", "children": [{"key": "wow", "status": "Changed", "old_value": "", "new_value": "so much"}]}, {"key": "key", "status": "Unchanged", "value": "value"}, {"key": "ops", "status": "Added", "value": "vops"}]}]}, {"key": "group1", "status": "Nested", "children": [{"key": "baz", "status": "Changed", "old_value": "bas", "new_value": "bars"}, {"key": "foo", "status": "Unchanged", "value": "bar"}, {"key": "nest", "status": "Changed", "old_value": {"key": "value"}, "new_value": "str"}]}, {"key": "group2", "status": "Deleted", "value": {"abc": 12345, "deep": {"id": 45}}}, {"key": "group3", "status": "Added", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}}]' # noqa E501
