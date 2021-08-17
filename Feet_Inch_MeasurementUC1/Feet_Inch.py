
'''@Author: Anusha Manda
@Date: 16-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 16-08-2021 18: 00: 30
@Title: Feet to Inch conversion
'''


class Feet_Inches:

    def __init__(self, feet, inches):
        '''Description: the class Feet_Inches is defined to conert given feet in to inches
          Arguments: feet, inches'''
        self.feet = feet
        self.inches = inches

    def feet_to_inches_check(self):
        '''Description: the function feet_to_inches_check is defined to check feet is equal to 12 inches
            Arguments: self
            Return: 'Value is None' '''
        try:
            if self.feet == None or self.inches == None:
                raise Exception
        except Exception:
            print("Value is None")
            return 'Values is None'

        if self.feet == self.inches/12:
            return True
        else:
            return False


class Inches_Feet:

    def __init__(self, inches, feet):
        '''Description: the class Inches_Feet is defined to conert given feet in to inches
          Arguments: inches, feet'''
        self.feet = feet
        self.inches = inches

    def inches_to_feet_check(self):
        '''Description: the function feet_to_inches_check is defined to check feet is equal to 12 inches
            Arguments: self
            Return: 'Value is None' '''
        try:
            if self.inches == None or self.feet == None:
                raise Exception
        except Exception:
            print("Value is None")
            return 'Values is None'

        if self.feet * 12 == self.inches:
            return True
        else:
            return False
