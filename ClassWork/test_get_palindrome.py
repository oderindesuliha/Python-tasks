import unittest
import functionpalindrome
	
class TestPalindromeFunction(unittest.TestCase):
	
	def test_that_palindrome_function_exists(self):
		functionpalindrome.get_palindrome(112211)
	
	def test_that_palindrome_function_returns_true_or_false(self):
		result = functionpalindrome.get_palindrome(112211)
		self.assertTrue(result)
	
	def test_that_palindrome_function_returns_invalid_data_for_decimal_number(self):
		actual = functionpalindrome.get_palindrome(122.221)
		result = 'invalid input'
		self.assertTrue(actual, result)

	def test_that_palindrome_function_returns_invalid_for_charactersr(self):
		actual = functionpalindrome.get_palindrome("a")
		result =  'input a number!!'
		self.assertTrue(actual, result)

	def test_that_palindrome_function_returns_invalid_for_blank_space(self):
		actual = functionpalindrome.get_palindrome(" ")
		result =  'input a number!!'
		self.assertTrue(actual, result)
	
	def test_that_palindrome_function_returns_false_for_not_palindrome(self):
		actual = functionpalindrome.get_palindrome(564784)
		result =  'false'
		self.assertTrue(actual, result)

	def test_that_palindrome_function_returns_invalid_for_a_single_digit(self):
		actual = functionpalindrome.get_palindrome(564784)
		result =  'invalid!!'
		self.assertTrue(actual, result)

	def test_that_palindrome_function_returns_invalid_for_special_characters(self):
		actual = functionpalindrome.get_palindrome('#$%@^&')
		result =  'invalid input!!'
		self.assertTrue(actual, result)