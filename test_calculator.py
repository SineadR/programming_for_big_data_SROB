import unittest
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
    
# test the calculator functionality
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

	# this tests the add functionality
	# 2 + 2 = 4
	# 2 + 4 = 6
	# 2 + (-2) = 0
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)

    # subtraction
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)
    
    # multiplication
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2,4)
        self.assertEqual(8, result)
        result = self.calc.multiply(2, -5)
        self.assertEqual(-10, result)
        
    # division
    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(8,2)
        self.assertEqual(4, result)
        result = self.calc.divide(9,3)
        self.assertEqual(3, result)
        
    # exponent
    def test_calculator_exponent_method_returns_correct_result(self):
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(3,3)
        self.assertEqual(27, result)
        result = self.calc.exponent(5,3)
        self.assertEqual(125, result)
    
    # square root
    def test_calculator_sqrt_method_returns_correct_result(self):
        result = self.calc.sqrt(4)
        self.assertEqual(2, result)
        result = self.calc.sqrt(9)
        self.assertEqual(3, result)
        result = self.calc.sqrt(25)
        self.assertEqual(5, result)
    
    # square
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square(4)
        self.assertEqual(16, result)
        result = self.calc.square(9)
        self.assertEqual(81, result)
        result = self.calc.square(5)
        self.assertEqual(25, result)
        
    # cube
    def test_calculator_cube_method_returns_correct_result(self):
        result = self.calc.cube(4)
        self.assertEqual(64, result)
        result = self.calc.cube(2)
        self.assertEqual(8, result)
        result = self.calc.cube(3)
        self.assertEqual(27, result)
    
    # sine
    def test_calculator_sine_method_returns_correct_result(self):
        result = self.calc.sine(1)
        self.assertEqual(0.01745, round(result,5))
        result = self.calc.sine(2)
        self.assertEqual(0.0349, round(result,5))
        result = self.calc.sine(3)
        self.assertEqual(0.05234, round(result,5))
        
    # cosine
    def test_calculator_cosine_method_returns_correct_result(self):
        result = self.calc.cosine(1)
        self.assertEqual(0.99985, round(result,5))
        result = self.calc.cosine(2)
        self.assertEqual(0.99939, round(result,5))
        result = self.calc.cosine(3)
        self.assertEqual(0.99863, round(result,5))
    
    # test value checking
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        self.assertRaises(ValueError, self.calc.subtract, 'two', 'three')
        self.assertRaises(ValueError, self.calc.multiply, 'two', 'three')
        self.assertRaises(ValueError, self.calc.divide, 'two', 'three')
        self.assertRaises(ValueError, self.calc.exponent, 'two', 'three')
        self.assertRaises(ValueError, self.calc.sqrt, 'two')
        self.assertRaises(ValueError, self.calc.square, 'two')
        self.assertRaises(ValueError, self.calc.cube, 'two')
        self.assertRaises(ValueError, self.calc.sine, 'two')
        self.assertRaises(ValueError, self.calc.cosine, 'two')
    

if __name__ == '__main__':
    unittest.main()
