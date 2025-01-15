import unittest
import taskfourfunction

class TestIntegerFunction(unittest.TestCase):

	def test_that_an_taskfourfunction_exists(self):
		taskfourfunction.get_integer(932)


	def test_that_an_taskfourfunction_returns_correct_value(self):
		actual = integer(999)
		result = 9 + 9 + 9
		self.assertEqual(actual,result)
	
	def test_that_an_taskfourfunction_returns_invalid_value(self):
		actual = integer(-100)
		result = 'invalid data'
		self.assertEqual(actual,result)

	def test_that_an_taskfourfunction_returns_invalid_space(self):
		actual = integer(" ")
		result = 'invalid input'
		self.assertEqual(actual,result)