#!/usr/bin/python3

"""Defines a class BaseGeometry."""

class BaseGeometry:
	"""Represents a base geometry."""

	def area(self):
		"""Not implemented."""
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
	"""Value input as an integer.

	Args:
		name (str): string.
		value (int): Parameter to validate.
	Raises:
		TypeError: If value != integer.
		TypeError: If value is <= 0.
	"""

	if type(value) != int:
		raise TypeError("{} must be an integer".format(name))
	if value <= 0:
		raise TypeError("{} must be greater than 0".format(name))
