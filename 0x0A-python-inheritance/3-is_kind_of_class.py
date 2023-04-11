#!/usr/bin/python3
"""Defines the object is an instance of, or if the object is an instance of a class that inherited from, the specified class"""

def is_kind_of_class(obj, a_class):
	"""Checks the object instance of a class that inherits from a specific class.

	Args:
		obj (any): The object to check.
		a_class (type): Class to match the type of obj to.
	Returns:
		If the obj is the exact instance or inherited instance of a_class - True
		Otherwise - False.
	"""

	if isinstance(obj, a_class):
		return True
	return False
