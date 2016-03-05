#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

from operator import add, sub, mul, div


class RPN(object):
    __UNBALANCED_PARENTHESES_ERROR_MSG = 'Unbalanced parentheses'
    __INVALID_CHARACTER_ERROR_MSG = 'Invalid character: {}'
    __OPERATORS = {
        '+': (add, 0),
        '-': (sub, 0),
        '*': (mul, 1),
        '/': (div, 1),
    }

    def __init__(self):
        self.stack = None
        self.postfix_str = None

    def convert_infix_to_postfix(self, infix_str):
        """
        Accepts string representing arithmetic expression in infix notation with
        parentheses and binary operators: '+', '-', '*', '/'.
        Returns string with expression converted to postfix notation. Each operator
        and operand in resulting string separated with space character.
        """

        self.stack = list()
        self.postfix_str = ''

        for c in infix_str:
            if c.isdigit():
                self.postfix_str += c
            elif c == '(':
                self.stack.append(c)
            elif c == ')':
                try:
                    c = self.stack.pop()
                    while c != '(':
                        self.postfix_str += ' ' + c
                        c = self.stack.pop()
                except IndexError:
                    raise ValueError(self.__UNBALANCED_PARENTHESES_ERROR_MSG)
            elif c in self.__OPERATORS:
                try:
                    top_elem = self.stack[-1]
                    while self.__OPERATORS[c][1] <= self.__OPERATORS[top_elem][1]:
                        self.postfix_str += ' ' + self.stack.pop()
                        top_elem = self.stack[-1]
                except (KeyError, IndexError):  # if stack is empty or top_elem is not an operator
                    pass
                self.stack.append(c)
                self.postfix_str += ' '
            elif c.isspace():
                pass
            else:
                raise ValueError(self.__INVALID_CHARACTER_ERROR_MSG.format(c))

        while self.stack:
            elem = self.stack.pop()
            if elem == '(':
                raise ValueError(self.__UNBALANCED_PARENTHESES_ERROR_MSG)
            else:
                self.postfix_str += ' ' + elem

        return self.postfix_str
