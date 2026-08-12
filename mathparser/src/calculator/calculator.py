#!/usr/bin/env python3
"""
Created on 29.07.2011
Updated to python 3 and PEP8 on 07.03.2020

@author: Nikita Lipatov
"""

import math

from calculator.number import Number
from calculator.variables import Variables


class Calculator(object):
    """
        Enums
    """
    TYPE_NONE = 1
    TYPE_DELIMITER = 2
    TYPE_NUMBER = 3
    TYPE_FUNCTION = 4
    TYPE_VARIABLE = 5

    TYPE_DEGREE = 1
    TYPE_GRADUS = 2
    typeTangentUnit = TYPE_DEGREE

    '''
        Variables
    '''
    id_string = 0
    stored_string = ""
    stored_token = ""
    type_token = ""

    def __init__(self):
        self.id_string = 0
        self.stored_string = ""
        self.stored_token = ""
        self.type_token = ""
        self.variables = Variables()

    def calculate(self, expression):
        if len(expression) > 1024:
            raise Exception("Too much expression")
        self.stored_string = expression.lower().replace(" ", "")
        self.id_string = 0
        self.__get_token()
        if self.stored_token == "":
            raise Exception("Not found tokens!")
        result = Number()
        self.__first_step_parsing(result)
        return result.get_value()

    def __first_step_parsing(self, number):
        if self.type_token == self.TYPE_VARIABLE:
            token = self.stored_token
            temp_type = self.TYPE_VARIABLE
            if self.variables.contains(token) is False:
                self.variables.add(token, 0.0)
            self.__get_token()
            if self.stored_token != "=":
                self.__put_back()
                if self.variables.contains(token) is False:
                    self.variables.remove(token)
                self.stored_token = token
                self.type_token = temp_type
            else:
                self.__get_token()
                self.__second_step_parsing(number)
                self.variables.add(token, number.get_value())
                return
        self.__second_step_parsing(number)

    def __put_back(self):
        i = 0
        while i < len(self.stored_token):
            self.id_string -= 1
            i += 1

    def __find_var(self, key):
        if self.variables.contains(key) is False:
            raise Exception("Variable not found!")
        return self.variables.get(key)

    def __second_step_parsing(self, number):
        self.__third_step_parsing(number)
        token = self.stored_token
        while token == "+" or token == "-":
            self.__get_token()
            temp = Number()
            self.__third_step_parsing(temp)
            if token == "-":
                number.set_value(number.get_value() - temp.get_value())
            elif token == "+":
                number.set_value(number.get_value() + temp.get_value())
            token = self.stored_token

    def __third_step_parsing(self, number):
        self.__fourth_step_parsing(number)
        token = self.stored_token
        while token == "*" or token == "/" or token == "%":
            self.__get_token()
            temp = Number()
            self.__fourth_step_parsing(temp)
            if token == "/":
                if temp.get_value() == 0.0:
                    raise Exception("Division by zero!")
                number.set_value(number.get_value() / temp.get_value())
                token = self.stored_token
            elif token == "%":
                if temp.get_value() == 0.0:
                    raise Exception("Division by zero!")
                number.set_value(number.get_value() % temp.get_value())
                token = self.stored_token
            elif token == "*":
                number.set_value(number.get_value() * temp.get_value())
                token = self.stored_token

    def __fourth_step_parsing(self, number):
        self.__fifth_step_parsing(number)
        if self.stored_token == "^":
            self.__get_token()
            temp = Number()
            self.__fourth_step_parsing(temp)
            number.set_value(math.pow(number.get_value(), temp.get_value()))

    def __fifth_step_parsing(self, number):
        local_token = ""
        if ((self.type_token == self.TYPE_DELIMITER) and
                (self.stored_token == "+" or self.stored_token == "-")):
            local_token = self.stored_token
            self.__get_token()
        self.__sixth_step_parsing(number)
        if local_token == "-":
            number.invert_value()

    def __sixth_step_parsing(self, number):
        if self.stored_token == "(":
            self.__get_token()
            self.__second_step_parsing(number)
            if self.stored_token != ")":
                raise Exception("Brackets unbalance")
            self.__get_token()
        else:
            self.__seventh_step_parsing(number)

    def __seventh_step_parsing(self, number):
        if self.stored_token == "e":
            number.set_value(math.e)
            self.__get_token()
            return
        elif self.stored_token == "pi":
            number.set_value(math.pi)
            self.__get_token()
            return
        else:
            self.__atom(number)

    def __atom(self, number):
        match self.type_token:
            case self.TYPE_NUMBER:
                number.set_value(self.stored_token)
                self.__get_token()
            case self.TYPE_FUNCTION:
                self.__functions(number)
            case self.TYPE_VARIABLE:
                number.set_value(self.__find_var(self.stored_token))
                self.__get_token()
            case _:
                number.set_value(0.0)
                raise Exception("Syntax error")

    def __functions(self, number):
        function_name = self.stored_token
        match function_name:
            case "abs" | "log10" | "sqrt" | "acos" | "asin" | "atan" | "cos" | "sin" | "tan" | "ceil" | "floor":
                self.__one_parameter_functions(function_name, number)
            case "pow" | "log":
                self.__two_parameter_functions(function_name, number)
            case "min" | "max" | "avg" | "sum":
                self.__multi_parameter_functions(function_name, number)

    def __one_parameter_functions(self, function_name, number):
        self.__get_token()
        self.__sixth_step_parsing(number)
        match function_name:
            case "abs":
                number.set_value(math.fabs(number.get_value()))
            case "log10":
                number.set_value(math.log10(number.get_value()))
            case "sqrt":
                number.set_value(math.sqrt(number.get_value()))
            case "acos":
                number.set_value(math.acos(self.__grad2rad(number.get_value())))
            case "asin":
                number.set_value(math.asin(self.__grad2rad(number.get_value())))
            case "atan":
                number.set_value(math.atan(self.__grad2rad(number.get_value())))
            case "cos":
                number.set_value(math.cos(self.__grad2rad(number.get_value())))
            case "sin":
                number.set_value(math.sin(self.__grad2rad(number.get_value())))
            case "tan":
                number.set_value(math.tan(self.__grad2rad(number.get_value())))
            case "ceil":
                number.set_value(math.ceil(number.get_value()))
            case "floor":
                number.set_value(math.floor(number.get_value()))

    def __grad2rad(self, result):
        match self.typeTangentUnit:
            case self.TYPE_DEGREE:
                result = result * math.pi / 180
            case self.TYPE_GRADUS:
                result = result * math.pi / 200
        return result

    def __two_parameter_functions(self, function_name, number):
        self.__get_token()
        self.__get_token()
        self.__first_step_parsing(number)
        if self.stored_token == ",":
            self.__get_token()
            temp = Number()
            self.__first_step_parsing(temp)
            match function_name:
                case "pow":
                    number.set_value(math.pow(number.get_value(), temp.get_value()))
                case "log":
                    number.set_value(math.log(temp.get_value()) / math.log(number.get_value()))
            if self.stored_token == ",":
                raise Exception("Syntax error")
            elif self.stored_token != ")":
                raise Exception("Brackets unbalance")
            self.__get_token()
        else:
            raise Exception("Syntax error")

    def __multi_parameter_functions(self, function_name, number):
        self.__get_token()
        self.__get_token()
        self.__first_step_parsing(number)
        i = 1
        while True:
            if self.stored_token == ",":
                self.__get_token()
                temp = Number()
                self.__first_step_parsing(temp)
                if function_name == "min" and number.get_value() > temp.get_value():
                    number.set_value(temp.get_value())
                elif function_name == "max" and number.get_value() < temp.get_value():
                    number.set_value(temp.get_value())
                elif function_name == "avg":
                    number.set_value(number.get_value() + temp.get_value())
                    i += 1
                elif function_name == "sum":
                    number.set_value(number.get_value() + temp.get_value())
                    i += 1
            elif self.stored_token == ")":
                if function_name == "avg":
                    number.set_value(number.get_value() / i)
                self.__get_token()
                break
            else:
                raise Exception("Brackets unbalance")

    def __get_token(self):
        self.type_token = self.TYPE_NONE
        self.stored_token = ""
        str_buffer = ""

        if self.id_string == len(self.stored_string):
            return

        if self.is_delimiter(self.stored_string[self.id_string]):
            str_buffer += self.stored_string[self.id_string]
            self.id_string += 1
            self.type_token = self.TYPE_DELIMITER
        elif self.is_character(self.stored_string[self.id_string]):
            length_name = 0
            while self.is_delimiter(self.stored_string[self.id_string]) is False:
                str_buffer += self.stored_string[self.id_string]
                self.id_string += 1
                if self.id_string >= len(self.stored_string):
                    break
                length_name += 1
                if length_name >= 32:
                    raise Exception("Expression is too long")
            if self.id_string < len(self.stored_string) and self.stored_string[self.id_string] == '(':
                self.type_token = self.TYPE_FUNCTION
            else:
                self.type_token = self.TYPE_VARIABLE
        elif self.is_digit(self.stored_string[self.id_string]):
            while self.is_delimiter(self.stored_string[self.id_string]) is False:
                str_buffer += self.stored_string[self.id_string]
                self.id_string += 1
                if self.id_string >= len(self.stored_string):
                    break
            self.type_token = self.TYPE_NUMBER
        self.stored_token = str_buffer

    @staticmethod
    def is_delimiter(char):
        if " +-/\\*%^=(),".find(char) != -1:
            return True
        else:
            return False

    @staticmethod
    def is_digit(char):
        if "0123456789".find(char) != -1:
            return True
        else:
            return False

    @staticmethod
    def is_character(char):
        if "abcdefghljklmnopqrstuvwxyz".find(char) != -1:
            return True
        else:
            return False
