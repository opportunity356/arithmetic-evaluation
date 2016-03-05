#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'opportunity356'

import unittest

from rpn import RPN


class TestInfixToPostfixConversion(unittest.TestCase):

    def setUp(self):
        self.rpn = RPN()

    def test_operators_precedence(self):
        result = self.rpn.convert_infix_to_postfix('2+3*4')
        self.assertEqual('2 3 4 * +', result)

    def test_parentheses_precedence(self):
        result = self.rpn.convert_infix_to_postfix('(2+3)*4')
        self.assertEqual('2 3 + 4 *', result)

    def test_unrecognized_character_raises_error(self):
        with self.assertRaises(ValueError):
            self.rpn.convert_infix_to_postfix('5 $ 4')

    def test_unbalanced_parentheses_raises_error(self):
        with self.assertRaises(ValueError):
            self.rpn.convert_infix_to_postfix('(()')


if __name__ == '__main__':
    unittest.main()