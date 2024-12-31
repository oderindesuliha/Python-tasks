class arraykata:
	def maximum_in(number):
		maximum = number[0]	
		for count in number:
			if count > maximum:
				maximum = count
			return maximum
	number = [-10, -2, 500, -3, 20, -9]
	maximum_number = maximum_in(number)
	print("The maximum number is :" , maximum_number) 

	def minimum_in(number):
		minimum = number[0]
		for count in number:
			if count < minimum:
				minimum = count
		return minimum
	number = [10, 200, 500, 30, 85, 90]
	minimum_number = minimum_in(number)
	print("The minimum number is :" , minimum_number) 

	def sum_of_list(element):
		sum = 0 
		for count in element:
			sum += count
		return sum
	element = [10, 20, 30, 10, 20, 10]
	sum_total = sum_of_list(element)
	print("The sum of elements in the list is:" , sum_total)

	def sum_of_even(number):
		sum_even = 0
		for count in number:
			if count % 2 == 0:
				sum_even += count
		return sum_even	
	number = [2, 3, 1, 2, 10, 2]
	even_sum_total = sum_of_even(number)
	print("The sum of even numbers in the list is:" , even_sum_total)

	def sum_of_odd(element): 
		sum_odd = 0
		for count in element:
			if count % 2 == 1:
				sum_odd += count
		return sum_odd
	element = [2, 5, 25, 4, 8, 1]
	odd_sum_total = sum_of_odd(element)
	print("The sum of odd numbers in the list is:" , odd_sum_total)

	def maximum_minimum(number):
		minimum = number[0]
		maximum = number[0]
		for count in number:
			if count < minimum:
					minimum = count
		for count in number:
			if count > maximum:
					maximum = count 
		return [maximum, minimum]
	number = [2, 5, 25, 4, 8, 1]
	maximum_and_minimum = maximum_minimum(number)
	print(f"The maximum number in the list is:" , maximum_and_minimum)

	def number_of_odd(element): 
		count = 0
		for odd in element:
			if odd % 2 == 1:
				count += 1
		return count
	element = [2, 5, 25, 4, 8, 1]
	odd_numbers = number_of_odd(element)
	print("The count of odd numbers in the list is:" , odd_numbers)

	def number_of_even(element): 
		count = 0
		for even in element:
			if even % 2 == 0:
				 count += 1
		return count
	element = [2, 42, 22, 45, 80, 12]
	even_numbers = number_of_even(element)
	print("The count of even numbers in the list is:" , even_numbers)
		
	def even_numbers(element): 
		even = []
		for count in element:
			if count % 2 == 0:
				even.append(count)
		return even
	element = [2, 42, 22, 45, 80, 12]
	even_list = even_numbers(element)
	print("The even numbers in the list are:" , even_list)

	def odd_list(element): 
		odd = []
		for count in element:
			if count % 2 == 1:
				odd.append(count)
		return odd 
	element = [2, 5, 25, 4, 8, 1]
	odd_numbers = odd_list(element)
	print("The odd numbers in the list are:" , odd_numbers)

	def square_of_numbers(numbers): 
		number_square = []
		for count in numbers:
				number_square.append(count ** 2)
		return number_square
	numbers = [2, 7, 9, 4, 11, 12]
	squared_numbers = square_of_numbers(numbers)
	print("The square of numbers in the list are:" , squared_numbers)