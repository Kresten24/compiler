from enum import Enum

class INVALID_KINDS(Enum):
    INVALIDCHAR = "INVALIDCHAR"
    INVALIDNUM = "INVALIDNUM"
    INVALIDID = "INVALIDID"
    UNKNOWN = "UNKNOWN"

    def is_invalid(kind):
        try:
            INVALID_KINDS(kind)
            return True
        except ValueError as ve:
            return False
