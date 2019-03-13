#!/usr/bin/env python3.7
# coding=utf-8

from os.path import abspath
import unittest
from constructors import Data
# from ..data import Data

class DataTest(unittest.TestCase):
    """ unit tests around Data class """

    def test_cast_data(self):
        """ test cast data """
        data = '1'

        converted_int = Data.cast_primitive_dtype(data=data, dtype=int)
        converted_float = Data.cast_primitive_dtype(data=data, dtype=float)
        converted_str = Data.cast_primitive_dtype(data=data, dtype=str)
        converted_bool = Data.cast_primitive_dtype(data=data, dtype=bool)

        self.assertEqual(type(converted_int), int)
        self.assertEqual(type(converted_float), float)
        self.assertEqual(type(converted_str), str)
        self.assertEqual(type(converted_bool), bool)

    def test_construct_data_object(self):
        """ test data constructor """

        expected = [
            {'ProductId': '1', 'Name': 'Minor Widget', 'Price': 0.25, 'LotSize': 250},
            {'ProductId': '2', 'Name': 'Critical Widget', 'Price': 5.00, 'LotSize': 10},
            {'ProductId': '3', 'Name': 'Complete System (Basic)', 'Price': 500.0, 'LotSize': 1},
            {'ProductId': '4', 'Name': 'Complete System (Deluxe)', 'Price': 625.0, 'LotSize': 1}
        ]

        file_path = abspath('files/ProductMaster.txt')
        product = Data(file=file_path,
                       headers=['ProductId', 'Name', 'Price', 'LotSize'],
                       delimiter=',',
                       header_dtypes={'ProductId': str, 'Name': str, 'Price': float, 'LotSize': int})

        self.assertEqual(expected, product.data)

if __name__ == '__main__':
    unittest.main()
