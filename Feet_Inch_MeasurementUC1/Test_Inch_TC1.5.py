'''@Author: Anusha Manda
@Date: 16-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 16-08-2021 18: 00: 30
@Title: Test Inch equal to conversion
'''
import unittest
from Quantity_Inch import Inch_Quantity


class TestQuantity(unittest.TestCase, Exception):

    def test_inches_equalto_inches(self):
        '''Description: test_inches_equalto_inches is defined to check if inch equal to inch
            Function Parameters: self
            Return: None'''
        quantity = Inch_Quantity(10, 10)
        res = quantity.inch_Equal_inch()
        self.assertEqual(res, 'Equal')
