#!/usr/bin/python3
""" return true if the object is an instance of a class inherited from a specified class """

def inherits_from(obj, a_class):
    """
    return true if the object is an instance of a class inherited from a specific class 
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
