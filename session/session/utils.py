""" Module for service utilties.
"""

#TODO to be moved to a base service project to be created

from functools import wraps

class RequestTypeError(Exception):
    pass

def methods(request_types):
    """ Validate request types for a service methods.
    """
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request_type = kwargs.pop('__method__', None)
            if request_type and request_type not in request_types:
                return {
                    "error": "Method {} not allowed".format(request_type)
                }, 405
            return func(*args, **kwargs)
        return wrapper
    return inner
