from collections import namedtuple

_STATUS = namedtuple("Status",
                     ["ADDED", "CHANGED", "DELETED", "NESTED", "UNCHANGED"])
STATUS = _STATUS("Added", "Changed", "Deleted", "Nested", "Unchanged")

INDENT = " "
INDENT_SIGNS = {
    "Added": "+",
    "Deleted": "-",
    "Unchanged": " ",
    "Nested": " "
}

PLAIN_MESSAGE = {
    "Added": "Property '{path_added}' was added with value: {value_added}",
    "Deleted": "Property '{path_deleted}' was removed",
    "Changed": "Property '{path_changed}' was updated. From {old_value} to {new_value}"  # noqa E501
}
