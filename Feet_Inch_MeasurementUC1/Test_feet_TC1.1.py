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

   
