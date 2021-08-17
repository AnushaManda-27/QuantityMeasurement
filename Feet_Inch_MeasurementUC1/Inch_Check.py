'''@Author: Anusha Manda
@Date: 16-08-2021 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 16-08-2021 18: 00: 30
@Title: Inch equal to Inch check
'''


class Inch_Quantity(object):
    '''Description: the class Inch_Quantity is defined to check given 2 feet Equality
          Arguments: inch1, inch2'''

    def __init__(self, inch1, inch2):
        self.inch1 = inch1
        self.inch2 = inch2

    def inch_Equal_inch(self):
        '''Description: the function inch_to_inch is defined to check given 2 inches are equal
            Arguments: self
            Return: 'Equal' '''
        if self.inch1 == self.inch2:
            return 'Equal'
        else:
            return 'Not Equal'

    def inch_Not_None(self):
        '''Description: the function inch_Not_None is defined to check given 2 inches are Not None
            Arguments: self
            Return: 'Not None' '''
        try:
            if self.inch1 == None or self.inch2 == None:
                raise Exception
        except Exception:
            print("Value is None")
            return 'Values is None'
        return 'Not None'

    def type_check(self):
        '''Description: the function type_check is defined to check the type of given 2 inches 
            Arguments: self
            Return: 'Type match' '''
        try:
            if type(self.inch1) != int or type(self.inch2) != int:
                raise Exception

        except Exception:
            #print('Type incorrect')
            return 'Type incorrect'
        return 'Type match'


if __name__ == '__main__':
    obj1 = Inch_Quantity(12, 12)
    type = obj1.type_check()
    print(type)
    not_none = obj1.inch_Not_None()
    print(not_none)
    equal = obj1.inch_Equal_inch()
    print(equal)

    instance = isinstance(obj1, Inch_Quantity)
    print(instance)
