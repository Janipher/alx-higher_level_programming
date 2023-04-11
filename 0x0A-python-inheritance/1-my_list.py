#!/usr/bin/python3
"""
Contains a Mylist module that
creates a class inheriting from a list
"""

class MyList(list):
"""Mylist class that inherits from the list"""

def print_sorted(self):
"""Prints the list, but sorted (ascending sort)"""
print(sorted(self))
