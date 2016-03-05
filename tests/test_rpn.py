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

    def test_stack_is_cleared_when_error(self):
        try:
            self.rpn.convert_infix_to_postfix('(5+4)*3-2 &')
        except ValueError:
            pass
        self.assertListEqual([], self.rpn.stack)


class TestPostfixExpressionEvaluation(unittest.TestCase):
    def setUp(self):
        self.rpn = RPN()

    def test_simple_postfix_expression_evaluation(self):
        result = self.rpn.evaluate_postfix('2 3 +')
        self.assertEqual(5, result)

    def test_complex_postfix_expression_evaluation(self):
        result = self.rpn.evaluate_postfix('1 2 + 4 * 3 +')
        self.assertEqual(15, result)

    def test_invalid_expression_with_too_many_operands_raises_error(self):
        with self.assertRaises(ValueError):
            self.rpn.evaluate_postfix('1 2 3 +')

    def test_invalid_expression_with_not_enough_operands_raises_error(self):
        with self.assertRaises(ValueError):
            self.rpn.evaluate_postfix('3 *')

    def test_invalid_character_raises_error(self):
        with self.assertRaises(ValueError):
            self.rpn.evaluate_postfix('&')

class TestEvalMethod(unittest.TestCase):
    def setUp(self):
        self.rpn = RPN()

    def test_simple_expression_evaluation(self):
        result = self.rpn.eval('2+2*2')
        self.assertEqual(6, result)

    def test_complex_expression_evaluation(self):
        result = self.rpn.eval('3 + (4 * 2 + 1) / (1 - 5)')
        self.assertEqual(0.75, result)


if __name__ == '__main__':
    unittest.main()