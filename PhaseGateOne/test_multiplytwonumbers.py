import multiplyfunction:

	test_That_Checks_To_Multiply_Numbers_Without_Operator(self):
		actual = multiplyfunction.get_multiply(10, 10)
		result = 100
		self.assertEqual(actual, result)
		