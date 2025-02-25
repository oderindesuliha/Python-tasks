import unittest
import expensetrackerfunction

class Testexpensetracker(unittest.TestCase):
    
	
	def test_to_throw_exception_when_date_is_not_correct(self):
        	self.assertRaises(ValueError,expensetrackerfunction.add_expense, "2022-34-22", "adelakun", "1234")

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

	def test_to_view_expenses(self):
		main_expense =({'date': "2025-02-25", 'description': "Beans", 'amount': "3000.0"})
		expected = ({'date': "2025-02-25", 'description': "Bread", 'amount': "100.0"})
		self.assertEqual(main_expense, expected)
    E
	def test_to_calculate_expenses(self):
		expenses=(1.{'date': "2025-02-25", 'description': "Biro", 'amount': "3000.0"})
		(2.{'date': "2025-02-26", 'description': "Books", 'amount': "50.0"})
		expected = "3050.0"
		total = sum(expense['amount'] for expense in expenses)
		self.assertEqual(total, expected)



    
	
