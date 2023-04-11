#!/usr/bin/python3
"""Defines the object is an instance of a class that inherited (directly or indirectly) from the specified class"""

def inherits_from(obj, a_class):
	"""Check the inherited instance of object be it directly or indirectly of a class.

	Args:
		obj (any): The object to check.
		a_class (type): The class to match object type to.
	Returns:
		If obj is an inherited instance of a_class - True.
		Otherwise - False.
	"""

	if issubclass(type(obj), a_class) and type(obj) != a_class:
		return True
	return False
