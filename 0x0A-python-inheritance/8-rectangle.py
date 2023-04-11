#!/usr/bin/python3

"""Defines class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
	"""Represents a rectangle using the BaseGeometry."""

	def __init__(self, width, height):
		"""Initializes the new rectangle.

		Args:
			width (int): Width of the Rectangle.
			height (int): Height of the Rectangle.
		"""

		self.integer_validator("width", width)
		self.__width = width
		self.integer_validator("height", height)
		self.__height = height
