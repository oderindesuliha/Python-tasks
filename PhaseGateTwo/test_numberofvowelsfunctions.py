import unittest
import numberofvowelsfunction

class Testnumberofvowel(unittest.TestCase):

	def test_that_number_of_vowel_function_exists(self):
		actual = numberofvowelsfunction.get_thenumberofvowels( "python is sweet")
		expected = 4
		self.assertEqual(actual, expected)

	def test_that_number_of_vowel_function_returns_0_when_only_consonants_are_entered(self):
		actual = numberofvowelsfunction.get_thenumberofvowels( "prympt")
		expected = 0
		self.assertEqual(actual, expected)

	def test_that_number_of_vowel_function_returns_invalid_when_numbers_are_entered(self):
		actual = numberofvowelsfunction.get_thenumberofvowels( "664971")
		expected = 'invalid'
		self.assertEqual(actual, expected)








if __name__ =='__main__':
	unittest.main()