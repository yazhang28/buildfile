#!/usr/bin/env python3.7
# coding=utf-8

from typing import List, Dict, Union
import logging

class Data:
    logger = logging.getLogger(__name__)

    """ Data object constructor wrapped around file """

    def __init__(self, file: str, headers: List[str], delimiter: str, header_dtypes:Dict):
        self.data = self.construct_data_object(file, headers, delimiter, header_dtypes)

    def construct_data_object(self, file: str, headers: List[str], delimiter: str, header_dtypes:Dict) -> List[Dict]:
        """ construct data object that will hold file data
            :param file: filepath
            :param headers: list of headers used to construct data object
            :param delimiter: delimiter of file
            :param header_dtypes: dictionary containing the data types of each header column and its data

                {
                    <header_1> : <data_type>,
                    <header_2> : <data_type>,
                    ...
                }

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
        logging.debug(f'Building Data object for :: {file}')
        data = []
        try:
            with open(file) as f:
                for line in f:
                    row_dict = {header: Data.
                        cast_primitive_dtype(value,header_dtypes[header])
                                for header, value in zip(headers, line.rstrip().split(delimiter))}

                    data.append(row_dict)
            return data
        except Exception as e:
            self.logger.error(f'{e} :: specify the correct path to file')

    @staticmethod
    def cast_primitive_dtype(data, dtype) -> Union[int, str, bool, float]:
        """ casts data to its declared type
            :param data: object to be cast
            :param dtype: type to be cast
            :returns data after casting
        """

        if dtype == str:
            return str(data)
        elif dtype == int:
            return int(data)
        elif dtype == bool:
            return bool(data)
        elif dtype == float:
            return float(data)


