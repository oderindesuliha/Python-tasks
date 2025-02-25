def get_factorialOf(number)-> int:
		count = 1
		for counter in range(2, number + 1):
			count *= counter
		return count
number = 5
print(get_factorialOf(number))