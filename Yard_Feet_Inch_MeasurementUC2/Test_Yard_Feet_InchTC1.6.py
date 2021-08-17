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

    def test_1feet_NotEqual_1yard(self):
        '''Description: the function test_1feet_NotEqual_1yard is defined to check if it is False
            Function Arguments: self
            Return: None'''
        yard_feet = Yard_Feet(1, 1)
        res = yard_feet.yard_to_feet_check()
        self.assertEqual(res, False)

    def test_36inches_1yard(self):
        '''Description: the function test_36inches_1yard is defined to check if it is True
            Function Arguments: self
            Return: None'''
        inch_yard = Inch_Yard(1, 36)
        res = inch_yard.inch_to_yard_check()
        self.assertEqual(res, True)

    def test_1inches_Not_1yard(self):
        '''Description: the function test_1inches_Not_1yard is defined to check if it is True
            Function Arguments: self
            Return: None'''
        inch_yard = Inch_Yard(1, 1)
        res = inch_yard.inch_to_yard_check()
        self.assertEqual(res, False)

    def test_1yard_36inch(self):
        '''Description: the function test_1yard_36inch is defined to check if it is True
            Function Arguments: self
            Return: None'''
        inches_feet = Yard_inch(36, 1)
        res = inches_feet.inch_to_yard_check()
        self.assertEqual(res, True)

    def test_1yard_Not_Equal_1inch(self):
        '''Description: the function test_1yard_Not_Equal_1inch is defined to check if it is True
            Function Arguments: self
            Return: None'''
        inches_feet = Yard_inch(1, 1)
        res = inches_feet.inch_to_yard_check()
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()
