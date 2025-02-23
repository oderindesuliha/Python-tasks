import unittest
import expensetrackerfunction

class Testexpensetracker(unittest.TestCase):
	
	def test_that_the_expense_tracker_function_exists(self):
		expensetrackerfunction.get_expensetracker()

	



if __name__ =='__main__':
	unittest.main()