import unittest
import todolistfunction

class Testtodolist(unittest.TestCase):

	def test_that_to_do_list_function_exists(self):
		self.todolist()	
	
	def test_to_add_task(self):
		task = "Buy Groceries"
		self.assertEqual(tasks[0]['task'], task)

