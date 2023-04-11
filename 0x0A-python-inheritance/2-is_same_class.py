#!/usr/bin/python3
"""
Defines function that checks the exact instance of a specified class"""

def is_same_class(obj, a_class):
	"""Check the exact instance of a specified class

	Args:
		obj (any): The object to check.
		a_class (type): Class to match obj type to.
	Returns:
		If the obj is the exact instance of a_class - True.
		Otherwise - False.
	"""
	if type(obj) == a_class:
		return True
	return False
