'''@Author: Anusha Manda
@Date: 16-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 16-08-2021 18: 00: 30
@Title: Feet equal to feet check
'''


class Feet_Quantity(object):
    def __init__(self, feet1, feet2):
        '''Description: the class Feet_Quantity is defined to check given 2 feet Equality
          Arguments: feet1, feet2'''
        self.feet1 = feet1
        self.feet2 = feet2

    def feet_Equal_feet(self):
        '''Description: the function feet_to_feet is defined to check given 2 feet are equal
            Arguments: self
            Return: 'Equal' '''
        if self.feet1 == self.feet2:
            return 'Equal'
        else:
            return 'Not Equal'

    def feet_Not_None(self):
        '''Description: the function feet_Not_None is defined to check given 2 feet are Not None
            Arguments: self
            Return: 'Not None' '''
        try:
            if self.feet1 == None or self.feet2 == None:
                raise Exception
        except Exception:
            print("Value is None")
            return 'Values is None'
        return 'Not None'

    def type_check(self):
        '''Description: the function type_check is defined to check the type of given 2 feets 
            Arguments: self
            Return: 'Type match' '''
        try:
            if type(self.feet1) != int or type(self.feet2) != int:
                raise Exception

        except Exception:
            #print('Type incorrect')
            return 'Type incorrect'
        return 'Type match'


if __name__ == '__main__':
    obj1 = Feet_Quantity(12, 12)
    type = obj1.type_check()
    print(type)
    not_none = obj1.feet_Not_None()
    print(not_none)
    equal = obj1.feet_Equal_feet()
    print(equal)
    instance = isinstance(obj1, Feet_Quantity)
    print(instance)
