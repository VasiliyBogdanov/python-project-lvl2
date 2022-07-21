from collections import namedtuple

_STATUS = namedtuple("Status",
                     ["ADDED", "CHANGED", "DELETED", "NESTED", "UNCHANGED"])
STATUS = _STATUS("Added", "Changed", "Deleted", "Nested", "Unchanged")
