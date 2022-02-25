plain_result_meta = [
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

stylish_plain_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

stylish_nested_result = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""