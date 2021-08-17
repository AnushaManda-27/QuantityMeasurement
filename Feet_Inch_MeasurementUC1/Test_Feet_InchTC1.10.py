'''@Author: Anusha Manda
@Date: 16-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 16-08-2021 18: 00: 30
@Title: Test Feet to Inch conversion
'''

from Feet_Inch_conv import Inches_Feet
import unittest
from Feet_Inch_conv import Feet_Inches


class feet_inches_test(unittest.TestCase):

    def test_12feet_1inches(self):
        '''Description: the function test_12feet_1inches is defined to check
            Function Arguments: self
            Return: None'''
        feet_inches = Feet_Inches(1, 12)
        res = feet_inches.feet_to_inches_check()
        self.assertEqual(res, True)

    def test_1feet_NotEqual_1Inch(self):
        '''Description: the function test_1feet_NotEqual_1Inch is defined to check
            Function Arguments: self
            Return: None'''
        feet_inch = Feet_Inches(1, 1)
        res = feet_inch.feet_to_inches_check()
        self.assertEqual(res, False)
