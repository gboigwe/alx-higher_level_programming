#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Suite test for max_integer function"""

    def test_maximum_int(self):
        """Testing for maximum integer
        using unittest
        """

        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def test_nil_list(self):
        """Testing an empty list
        using unittest module
        """

        self.assertEqual(max_integer([]), None)

    def test_num_repeat(self):
        """Testing with a repeated large number
        Using unittest
        """

        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_nums_decimal(self):
        """Testing a float number with decimals
        Using unittest
        """

        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def text_maximum_ope_int(self):
        """Testing a maximum operation integer
        Using unittest
        """

        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_thenegative_nums(self):
        """Testing negative numbers
        Using unittest
        """

        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_begin_max(self):
        """Testing the begining of numbers up to the maximum
        Using unittest
        """

        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_nums_that_zero(self):
        """Testing numbers like zero 0
        Using unittest
        """

        self.assertEqual(max_integer([0, 0]), 0)

    def test_large_list(self):
        """Testing a large list of numbers
        Using unittest
        """

        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def testing_list_loop(self):
        """Testing a list with a loop
        Using unittest
        """

        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def testing_num_of_list(self):
        """Testing a number in a list

        Testing a sigle number like 1 in a list

        Using unittest
        """

        self.assertEqual(max_integer([1]), 1)

    def testing_str_list(self):
        """Testing a string in a list

        More like a single quote string

        Using unittest
        """

        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def testing_tuple_list(self):
        """Testing a tuple in a list
        Using unittest
        """

        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def _testing_dict(self):
        """Testing a dictionary with an index and a value
        USing unittest
        """

        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def testing_the_num(self):
        """Testing any number
        Using unittest
        """

        with self.assertRaises(TypeError):
            max_integer(1)
