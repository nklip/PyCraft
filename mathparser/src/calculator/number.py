"""
Created on 01.08.2011

@author: Lipatov
"""

class Number(object):
    value = 0

    def __init__(self):
        self.value = 0

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = float(value)

    def invert_value(self):
        self.value = - self.value
