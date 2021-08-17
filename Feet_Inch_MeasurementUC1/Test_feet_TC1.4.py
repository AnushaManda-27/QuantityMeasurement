'''@Author: Anusha Manda
@Date: 16-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 16-08-2021 18: 00: 30
@Title: Test Feet equal to conversion
'''

import unittest
from Quantity_Feet import Feet_Quantity


class TestQuantity(unittest.TestCase, Exception):

    def test_feet_equalto_feet(self):
        '''Description: test_feet_equalto_feet is defined to check if feet equal to feet
            Function Parameters: self
            Return: None'''
        quantity = Feet_Quantity(12, 12)
        res = quantity.feet_Equal_feet()
        self.assertEqual(res, 'Equal')

    def test_feet_equalto_feet_Null_check(self):
        '''Description: test_feet_equalto_feet_Null_check is defined to check if feet not none
            Function Parameters: self
            Return: None'''
        quantity = Feet_Quantity(0, 0)
        res = quantity.feet_Not_None()
        self.assertEqual(res, 'Not None')

    def test_feet_equalto_feet_Reference_check(self):
        '''Description: test_feet_equalto_feet_Reference_check is defined to check if reference is equal
            Function Parameters: self
            Return: None'''
        #quant = 30
        quantity = Feet_Quantity(12, 30)
        res = self.assertIsInstance(quantity, Feet_Quantity)
        self.assertEqual(res, None)

    def test_type_check(self):
        '''Description: test_type_check is defined to check type of data
            Function Parameters: self
            Return: None'''
        quantity = Feet_Quantity(12, 78)
        res = quantity.type_check()
        self.assertEqual(res, 'Type incorrect')


if __name__ == '__main__':
    unittest.main()
