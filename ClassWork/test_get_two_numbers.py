import unittest
import functiontwonumbers

class TestTwoNumbersFunctions(unittest.TestCase):

	def test_if_two_numbers_function_exists(self):
		functiontwonumbers.get_two_numbers([5, 46, 7, 12, 24])
	
	def test_if_the_function_returns_an_array_of_two_numbers(self):
		actual = functiontwonumbers.get_two_numbers([5, 46, 7, 12, 24])
		expected = [5, 24]
		self.assertEqual(actual, expected)

	def test_if_the_function_returns_invalid_if_an_alphabet_and_special_characters_are_in_the_list(self):
		actual = functiontwonumbers.get_two_numbers([5, 4, " a", "@",  24])
		expected = 'invalid'
		self.assertEqual(actual, expected)