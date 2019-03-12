#!/usr/bin/env python3.7
# coding=utf-8

import os
from typing import List, Dict

""" Data object constructor wrapped around file """
class DataConstructor:

    def __init__(self, file: str, headers: List[str], delimiter: str):
        self.object = self.construct_data_object(file, headers, delimiter)

    def construct_data_object(self, file: str, headers: List[str], delimiter: str) -> List[Dict]:
        """ construct data object that will hold file data
            :param file: filepath
            :param headers: list of headers used to construct data object
            :param delimiter: delimiter of file

            :returns List[Dict] in the format:

            [
                { <header_1> : value_1,
                  <header_2> : value_2
                },
                { <header_1> : value_1,
                  <header_2> : value_2
                }
                ...
            ]
        """
        raise NotImplementedError
