#!/usr/bin/env python3.7
# coding=utf-8

import unittest
import logging
import app

class AppTest(unittest.TestCase):
    """ unit tests around app.py methods """
    logger = logging.getLogger(__name__)

    def test_get_accumulated_sales(self):
        sales = [
            {'SaleId': 1, 'ProductId': 1, 'TeamId': 2, 'Quantity': 10},
            {'SaleId': 2, 'ProductId': 1, 'TeamId': 1, 'Quantity': 1},
            {'SaleId': 3, 'ProductId': 2, 'TeamId': 1, 'Quantity': 5},
            {'SaleId': 4, 'ProductId': 3, 'TeamId': 4, 'Quantity': 1},
            {'SaleId': 5, 'ProductId': 3, 'TeamId': 5, 'Quantity': 2}
        ]

        expected = {1: 11, 2: 5, 3: 3}

        self.accumulated_sales = app.get_accumulated_sales(sales)
        self.assertEqual(expected, self.accumulated_sales)

if __name__ == '__main__':
    unittest.main()