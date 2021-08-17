'''@Author: Anusha Manda
@Date: 16-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 16-08-2021 18: 00: 30
@Title: Test Feet_Inch_Yard conversion
'''
import unittest

from yard_feet import Yard_Feet, Feet_Yard, Yard_inch, Inch_Yard


class TestYardToFeet(unittest.TestCase):

    def test_3feet_1yard(self):
        '''Description: the function test_3feet_1yard is defined to check if it true
            Function Arguments: self
            Return: None'''
        yard_feet = Yard_Feet(3, 1)
        res = yard_feet.yard_to_feet_check()
        self.assertEqual(res, True)
