#!/usr/bin/env python3.7
# coding=utf-8

# import os
import os.path
import sys
from typing import Dict
import logging.config
from constructors import Data

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), './logging.conf'))
logging.config.fileConfig(logging_conf_path)
logger = logging.getLogger(__name__)

def get_accumulated_sales(sales: Data) -> Dict:
    """ retrieve distinct sales from Sales file
        :param sales : sales data object
        :returns dictionary of the format
            {
                <ProductId_1> : <accumulated_sales>,
                <ProductId_2>: <accumulated_sales>,
                 ...
            }
    """

    data = {}
    for sale in sales:
        product_id = sale['ProductId']

        if product_id not in data:
            data[product_id] = sale['Quantity']
        else:
            data[product_id] = data[product_id] + sale['Quantity']

    logger.debug(f'Accumulated sales by ProductId: {data}')
    return data

def calc_total_units(quantity: int, lot_size: int) -> int:
    """ Calculate the total number of units sold for a product """

    return quantity * lot_size

def calc_gross_revenue(price: float, total_units: int) -> float:
    """ Calculate the gross revenue of sales for a product """

    return price * total_units

def build_product_report(product: Data, accumulated_sales: Dict, build_path: str):
    """ Build ProductReport.txt in the format
            Name,GrossRevenue,TotalUnits
            <Name_1>,<GrossRevenue_1>.<TotalUnits_1>
            <Name_2>,<GrossRevenue_2>.<TotalUnits_2>
            ...
    """

    if os.path.isfile(build_path):
        open(build_path, 'w').close()

    with open(build_path, 'a') as f:
        f.write('Name,GrossRevenue,TotalUnits\n')

        for productId, quantity in accumulated_sales.items():
            selected_product = product[productId-1]
            total_units = calc_total_units(quantity=quantity, lot_size=selected_product['LotSize'])
            gross_revenue = calc_gross_revenue(price=selected_product['Price'], total_units=total_units)
            
            line = f"{selected_product['Name']},{gross_revenue},{total_units}"
            logger.debug(f'writing to file :: {line}')
            f.write(f"{line}\n")

    logger.debug(f'build file :: {build_path} :: FIN')

def main(arguments):
    """ Build Product Report"""

    product_path = None
    sales_path = None
    build_file = None

    for i in range(len(arguments)):
        if arguments[i] == '-product_path':
            product_path = arguments[i+1]
        elif arguments[i] == '-sales_path':
            sales_path = arguments[i+1]
        elif arguments[i] == '-buildfile':
            build_path = arguments[i+1]

    product = Data(file=product_path,
                              headers=['ProductId', 'Name', 'Price', 'LotSize'],
                              delimiter=',',
                              header_dtypes={'ProductId': int, 'Name': str, 'Price': float, 'LotSize': int}).data

    sales = Data(file=sales_path,
                            headers=['SaleId', 'ProductId', 'TeamId', 'Quantity'],
                            delimiter=',',
                            header_dtypes={'SaleId': int,
                                           'ProductId': int,
                                           'TeamId': int,
                                           'Quantity': int}).data

    accumulated_sales = get_accumulated_sales(sales)
    build_product_report(product,accumulated_sales, build_path)

if __name__ == '__main__':
    main(sys.argv)
