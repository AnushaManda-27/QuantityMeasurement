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

    def test_Inch_equalto_Inch_Null_check(self):
        '''Description: test_Inch_equalto_Inch_Null_check is defined to check if inch not none
            Function Parameters: self
            Return: None'''
        quantity = Inch_Quantity(0, 0)
        res = quantity.inch_Not_None()
        self.assertEqual(res, 'Not None')

    def test_Inch_equalto_Inch_Reference_check(self):
        '''Description: test_Inch_equalto_Inch_Reference_check is defined to check if reference is equal
            Function Parameters: self
            Return: None'''
        #quant = 30
        quantity = Inch_Quantity(12, 30)
        res = self.assertIsInstance(quantity, Inch_Quantity)
        self.assertEqual(res, None)

    def test_type_check(self):
        '''Description: test_type_check is defined to check type of data
            Function Parameters: self
            Return: None'''
        quantity = Inch_Quantity(12, '78')
        res = quantity.type_check()
        self.assertEqual(res, 'Type incorrect')


if __name__ == '__main__':
    unittest.main()
