import unittest
import sumevenfunction

class TestSumOfEven(unittest.TestCase):
	
	def test_That_Checks_For_The_Sum_Of_Even_Numbers_Exists(self):
		actual = sumevenfunction.get_evenSum([2, 7, 5, 11, 7, 19, 2, 8, 10])		
		expected = 22
		self.assertEqual(actual, expected)
	
	def test_That_Checks_For_The_Sum_Of_Even_Numbers_Works(self):
		actual = sumevenfunction.get_evenSum([2, 7, 5, 11, 7, 19, 2, 8, 10])		
		expected = 22
		self.assertEqual(actual, expected)

	def test_That_Checks_For_The_Sum_Of_Even_Numbers_Returns_Invalid_For_Negative_numbers(self):
		actual = sumevenfunction.get_evenSum([-2, 7, 5, 19, -2, -8, -10])		
		expected = "Inavlid"
		self.assertEqual(actual, expected)
	
	def test_That_Checks_For_The_Sum_Of_Even_Numbers_Returns_Invalid_For_Decimal_numbers(self):
		actual = sumevenfunction.get_evenSum([2.5, 7, 5.5, 19, 2.4, 8.3, 10])		
		expected = 'Invalid Input'
		self.assertEqual(actual, expected)

	def test_That_Checks_For_The_Sum_Of_Even_Numbers_Returns_Invalid_For_Decimal_numbers(self):
		actual = sumevenfunction.get_evenSum([2.5, 7, 5.5, 19, 2.4, 8.3, 10])		
		expected = 'Invalid Input'
		self.assertEqual(actual, expected)


	
if __name__ =="__main__":
	unittest.main()