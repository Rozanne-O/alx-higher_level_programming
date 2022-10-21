#!/usr/bin/python3
""" Return True is the object is an instance of a class inherited from the specified class """

def is_kind_of_class(obj, a_class):
    """
    Return true is the object is an instance of a class inherited from the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
