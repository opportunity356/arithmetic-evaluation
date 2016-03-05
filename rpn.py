#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

from operator import add, sub, mul, div


class RPN(object):
    __UNBALANCED_PARENTHESES_ERROR_MSG = 'Unbalanced parentheses'
    __INVALID_CHARACTER_ERROR_MSG = 'Invalid character: {}'
    __INVALID_POSTFIX_EXPRESSION_MSG = 'Invalid postfix expression'
    __OPERATORS = {
        '+': (add, 0),
        '-': (sub, 0),
        '*': (mul, 1),
        '/': (div, 1),
    }

    def __init__(self):
        self.stack = list()

    def eval(self, infix_expression):
        postfix_expression = self.convert_infix_to_postfix(infix_expression)

        result = self.evaluate_postfix(postfix_expression)
        return result

    def convert_infix_to_postfix(self, infix_str):
        """
        Implementation of Dijkstra's shunting-yard algorithm.
        Accepts string representing arithmetic expression in infix notation with
        parentheses and binary operators: '+', '-', '*', '/'.
        Returns string with expression converted to postfix notation. Each operator
        and operand in resulting string separated with space character.
        """

        try:
            self.stack = list()
            postfix_str = ''

            for c in infix_str:
                if c.isdigit():
                    postfix_str += c
                elif c == '(':
                    self.stack.append(c)
                elif c == ')':
                    try:
                        c = self.stack.pop()
                        while c != '(':
                            postfix_str += ' ' + c
                            c = self.stack.pop()
                    except IndexError:
                        raise ValueError(self.__UNBALANCED_PARENTHESES_ERROR_MSG)
                elif c in self.__OPERATORS:
                    try:
                        top_elem = self.stack[-1]
                        while self.__OPERATORS[c][1] <= self.__OPERATORS[top_elem][1]:
                            postfix_str += ' ' + self.stack.pop()
                            top_elem = self.stack[-1]
                    except (KeyError, IndexError):  # if stack is empty or top_elem is not an operator
                        pass
                    self.stack.append(c)
                    postfix_str += ' '
                elif c.isspace():
                    pass
                else:
                    raise ValueError(self.__INVALID_CHARACTER_ERROR_MSG.format(c))

            while self.stack:
                elem = self.stack.pop()
                if elem == '(':
                    raise ValueError(self.__UNBALANCED_PARENTHESES_ERROR_MSG)
                else:
                    postfix_str += ' ' + elem

            return postfix_str

        finally:
            self.stack = list()

    def evaluate_postfix(self, postfix_str):
        """
        Method evaluates postfix expression using stack.
        """
        self.stack = list()

        for elem in postfix_str.split(' '):
            if elem.isdigit():
                self.stack.append(float(elem))
            elif elem in self.__OPERATORS:
                try:
                    r_operand = self.stack.pop()
                    l_operand = self.stack.pop()
                except IndexError:
                    raise ValueError(self.__INVALID_POSTFIX_EXPRESSION_MSG)
                self.stack.append(self.__OPERATORS[elem][0](l_operand, r_operand))
            else:
                raise ValueError(self.__INVALID_CHARACTER_ERROR_MSG.format(elem))

        if len(self.stack) != 1:
            raise ValueError(self.__INVALID_POSTFIX_EXPRESSION_MSG)

        return self.stack.pop()
