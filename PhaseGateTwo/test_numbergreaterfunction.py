import unittest
import numbergreaterfunction

class Testnumbersgreaterthan75(unittest.TestCase):

	def test_that_number_greater_function_exists(self):
		numbergreaterfunction.get_numbergreater( [1,50,75,90,22,12,20])
	
	def test_that_number_greater_function_return_list_of_numbers_equal_and_greater_than_75(self):
		actual = numbergreaterfunction.get_numbergreater( [1,50,75,90,22,12,20])
		expected = [75, 90]
		self.assertEqual(actual, expected)

	def test_that_number_greater_function_returns_empty_list_if_all_numbers_are_less_than_75(self):
		actual = numbergreaterfunction.get_numbergreater([1,50,20,5,10,22,12,20])
		expected = []
		self.assertEqual(actual, expected)

	def test_that_number_greater_function_returns_invalid_if_there_is_a_letter_in_the_list(self):
		actual = numbergreaterfunction.get_numbergreater([1,50,20,5,'g',22,12,20])
		expected = 'Invalid input'
		self.assertEqual(actual, expected)

	def test_that_number_greater_function_returns_if_there_is_a_decimal_number_in_the_list(self):
		actual = numbergreaterfunction.get_numbergreater([1,50,20.5,5.5,75.5,80.5])
		expected = [75.5, 80.5]
		self.assertEqual(actual, expected)





if __name__ =='__main__':
	unittest.main()