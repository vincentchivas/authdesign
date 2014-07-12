import random, string
from datetime import datetime
from time import mktime
from hashlib import md5


_SALT = 'Do1phin'


def unix_time(value = None):
    if not value:
        value = datetime.utcnow()
    try:
        return int(mktime(value.timetuple()))
    except AttributeError:
        return None


def flatten_dict(dct):
    if not dct:
        return None
    return dict([ (str(k), dct.get(k)) for k in dct.keys() ])


def md5digest(string = None):
    salted_str = string + _SALT
    return md5(salted_str.encode('utf-8')).hexdigest().upper()


def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
