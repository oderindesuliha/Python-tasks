import unittest
import expensetrackerfunction

class Testexpensetracker(unittest.TestCase):
    
	
	def test_to_throw_exception_when_date_is_not_correct(self):
        	self.assertRaises(ValueError, expensetrackerfunction.add_expense, "2022-34-22", "adelakun", "1234")

	def test_to_throw_exception_when_date_is_empty(self):
		self.assertRaises(ValueError, expensetrackerfunction.add_expense, "", "adelakun", "1234")

	def test_to_throw_exception_when_description_is_empty(self):    
		self.assertRaises(ValueError, expensetrackerfunction.add_expense, "2022-12-14", " ", "1234")

	def test_to_throw_exception_when_amount_is_alphabet(self):
		self.assertRaises(ValueError, expensetrackerfunction.add_expense, "2022-12-14", "AAdelal", "adbsbs")

	def test_to_throw_exception_when_amount_is_negative(self):
		self.assertRaises(ValueError, expensetrackerfunction.add_expense, "2022-12-14", "tatat", "-1234")
	
	def test_to_throw_exception_when_no_expenses_is_added(self):
		self.assertRaises(ValueError, expensetrackerfunction.add_expense, "2022-12-14", "tatat", "-1234")







if __name__ == '__main__':
    unittest.main()
