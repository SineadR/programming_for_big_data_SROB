import math

class Calculator(object):

    # addition
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    # subtraction
    def subtract(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError
    
    # multiplication
    def multiply(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError
    
    # division
    def divide(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x / y
        else:
            raise ValueError
            
    # exponent
    def exponent(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x ** y
        else:
            raise ValueError
            
    # square root
    def sqrt(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return self.exponent(x, 0.5)
        else:
            raise ValueError
    
    # square
    def square(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return self.exponent(x, 2)
        else:
            raise ValueError
            
    # cube
    def cube(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return self.exponent(x, 3)
        else:
            raise ValueError

    # sine
    def sine(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return math.sin(math.radians(x))
        else:
            raise ValueError
    
    # cosine
    def cosine(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return math.cos(math.radians(x))
        else:
            raise ValueError