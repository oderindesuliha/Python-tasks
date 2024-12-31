def sum_of_even(number):
		even = 0
		for count in number:
			if count % 2 == 0:
				even += count
			return even	
number = [12, 31, 21, 16, 10, 2]
even_sum_total = sum_of_even(number)
print("The sum of even numbers in the list is:" , even_sum_total) 