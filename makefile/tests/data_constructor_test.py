#!/usr/bin/env python3.7
# coding=utf-8

import unittest
from ..data_constructor import DataConstructor

""" unit tests around DataConstructor class """
class DataConstructorTest(unittest.TestCase):

    def test_construct_data_object(self):
        """ test data constructor """

        expected = [
            {'ProductId': 1, 'Name': 'Minor Widget', 'Price': 0.25, 'LotSize': 250},
            {'ProductId': 2, 'Name': 'Critical Widget', 'Price': 5.00, 'LotSize': 10},
            {'ProductId': 3, 'Name': 'Complete System(Basic)', 'Price': 500, 'LotSize': 1},
            {'ProductId': 4, 'Name': 'Complete System(Deluxe)', 'Price': 625, 'LotSize': 1}
        ]

        product = DataConstructor(file='files/ProductMaster.txt',
                                  headers=['ProductId', 'Name', 'Price', 'LotSize'],
                                  delimiter=',')

        self.assertEquals(expected, product)

if __name__ == '__main__':
    unittest.main()
