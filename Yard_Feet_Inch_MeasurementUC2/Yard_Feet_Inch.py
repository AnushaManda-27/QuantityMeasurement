
'''@Author: Anusha Manda
@Date: 16-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 16-08-2021 18: 00: 30
@Title: Yard -Feet-Inch Conversion
'''


class Yard_Feet:
    '''Description: the class Yard_Feet is defined to conert given yard in to feet
          Arguments: yard, feet'''

    def __init__(self, yard, feet):
        self.feet = feet
        self.yard = yard

    def yard_to_feet_check(self):
        '''Description: the function yard_to_feet_check is defined to check 1yard is equal to 3 Feet
            Arguments: self
            Return: 'Value is None' '''
        try:
            if self.feet == None or self.yard == None:
                raise Exception
        except Exception:
            print("Value is None")
            return 'Values is None'

        if self.feet == self.yard/3:
            return True
        else:
            return False


class Feet_Yard:

    '''Description: the class Feet_Yard is defined to conert given feet in to yard
          Arguments: feet, yard'''

    def __init__(self, feet, yard):
        self.feet = feet
        self.yard = yard

    def feet_to_yard_check(self):
        '''Description: the function feet_to_yard_check is defined to check 3 feet is equal to 1 yard
            Arguments: self
            Return: 'Value is None' '''

        try:
            if self.yard == None or self.feet == None:
                raise Exception
        except Exception:
            print("Value is None")
            return 'Values is None'

        if self.feet * 3 == self.yard:
            return True
        else:
            return False


class Inch_Yard:

    '''Description: the class Inch_Yard is defined to conert given inch in to yard
          Arguments: inch, yard'''

    def __init__(self, inch, yard):
        self.inch = inch
        self.yard = yard

    def inch_to_yard_check(self):
        '''Description: the function inch_to_yard_check is defined to check 36 inch is equal to 1 yard
            Arguments: self
            Return: 'Value is None' '''
        try:
            if self.yard == None or self.inch == None:
                raise Exception
        except Exception:
            print("Value is None")
            return 'Values is None'

        if self.inch * 36 == self.yard:
            return True
        else:
            return False


class Yard_inch:

    def __init__(self, yard, inch):
        '''Description: the class Yard_Inch is defined to conert given yard in to inch
          Arguments: yard, ich
          Return: None'''
        self.inch = inch
        self.yard = yard

    def inch_to_yard_check(self):
        '''Description: the function inch_to_yard_check is defined to check 36 inch is equal to 1 yard
            Arguments: self
            Return: 'Value is None' '''

        try:
            if self.yard == None or self.inch == None:
                raise Exception
        except Exception:
            print("Value is None")
            return 'Values is None'

        if self.inch * 36 == self.yard:
            return True
        else:
            return False
