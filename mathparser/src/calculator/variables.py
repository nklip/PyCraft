"""
Created on 04.08.2011

@author: Lipatov
"""

class Variables(object):
    """
    classdocs
    """
    variables = ""

    def __init__(self):
        self.variables = dict()

    def add(self, key, value):
        self.variables[key] = value

    def contains(self, key):
        return self.variables.__contains__(key)

    def remove(self, key):
        del self.variables[key]

    def get(self, key):
        return self.variables.get(key)
