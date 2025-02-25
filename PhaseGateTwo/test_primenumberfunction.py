import unittest
import primenumberfunction

class Testprimenumber(unittest.TestCase):

	def test_that_prime_number_function_exists(self):
		primenumberfunction.get_primenumber(7)

	def test_that_prime_number_function_works(self):
		actual = primenumberfunction.get_primenumber(7)
		expected = True
		self.assertTrue(actual, expected)
		
	def test_that_prime_number_function_works(self):
		actual = primenumberfunction.get_primenumber(25)
		expected = False
		self.assertEqual(actual, expected)

	



if __name__ =='__main__':
	unittest.main()