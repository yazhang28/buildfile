#!/usr/bin/env python3.7
# coding=utf-8
import os
import unittest
from ..data_constructor import DataConstructor
from buildfile import log
""" unit tests around DataConstructor class """
class DataConstructorTest(unittest.TestCase):

    def test_cast_data(self):
        """ test cast data """
        data = '1'

        converted_int = DataConstructor.cast_primitive_dtype(data=data, dtype=int)
        converted_float = DataConstructor.cast_primitive_dtype(data=data, dtype=float)
        converted_str = DataConstructor.cast_primitive_dtype(data=data, dtype=str)
        converted_bool = DataConstructor.cast_primitive_dtype(data=data, dtype=bool)

        self.assertEquals(type(converted_int), int)
        self.assertEquals(type(converted_float), float)
        self.assertEquals(type(converted_str), str)
        self.assertEquals(type(converted_bool), bool)

    def test_construct_data_object(self):
        """ test data constructor """

        expected = [
            {'ProductId': '1', 'Name': 'Minor Widget', 'Price': 0.25, 'LotSize': 250},
            {'ProductId': '2', 'Name': 'Critical Widget', 'Price': 5.00, 'LotSize': 10},
            {'ProductId': '3', 'Name': 'Complete System (Basic)', 'Price': 500.0, 'LotSize': 1},
            {'ProductId': '4', 'Name': 'Complete System (Deluxe)', 'Price': 625.0, 'LotSize': 1}
        ]

        file = os.getcwd() + '/buildfile/tests/files/ProductMaster.txt'
        product = DataConstructor(file=file,
                                  headers=['ProductId', 'Name', 'Price', 'LotSize'],
                                  delimiter=',',
                                  header_dtypes={'ProductId': str, 'Name': str, 'Price': float, 'LotSize': int})

        self.assertEquals(expected, product.data)

if __name__ == '__main__':
    unittest.main()
