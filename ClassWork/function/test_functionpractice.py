import unittest
import functionpractice
import dollartonaira

class TestCubeFunction(unittest.TestCase):

	def test_that_cube_function_exists(self):
		functionpractice.get_cube(3)

	def test_that_cube_function_returns_correct_value(self):
		self.assertEqual(functionpractice.get_cube(3), 27)

		self.assertEqual(functionpractice.get_cube(5), 125)

	def test_that_cube_function_returns_invalid_data(self):
		self.assertEqual(functionpractice.get_cube(3) , 27)
	
	def test_that_cube_function_returns_decimal_value(self):
		actual = functionpractice.get_cube(3.25)
		result = 34.328
		self.assertEqual(actual, result)

	def test_that_cube_function_returns_invalid_data_with_invalid_input(self):
		actual = functionpractice.get_cube('a')
		result = 'invalid data'
		self.assertEqual(actual, result)

class TestDollarToNairaFunction(unittest.TestCase):

	def test_that_takes_dollar_amount_as_input_and_returns_the_equivalent_as_amount_in_naira(self):
		dollartonaira.get_naira(1550)

	def test_that_takes_dollar_amount_and_returns_as_naira(self):
		actual = dollartonaira.get_naira(100)
		result = 155,000
		self.assertEqual(actual,result)

	def test_that_conversion_rate_return_invalid_data_with_invalid_input(self):
		actual = functionpractice.convert_dollar_to_naira('x')
		result = 'invalid data'
		self.assertEqual(actual, result)

	def test_that_conversion_rate_returns_an_invalid_amount(self):
		actual = functionpractice.convert_dollar_to_naira(-200)
		result = 'invalid data'
		self.assertEqual(actual, result)
	
	def test_that_decimal_number_is_valid_during_conversion(self):
		actual = functionpractice.convert_dollar_to_naira(120.67)
		result = 187,040.90
		self.assertEqual(actual, result)

	def test_that_negative_decimal_is_invalid_during_conversion(self):
		actual = functionpractice.convert_dollar_to_naira(-5)
		result = 'invalid data'
		self.assertEqual(actual, result)

	def test_that_conversion_rate_returns_invalid_data_with_empty_space(self):
		actual = functionpractice.convert_dollar_to_naira(' ')
		result = 'invalid input'
		self.assertEqual(actual, result)


	