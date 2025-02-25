def check_two_numbers(numbers):
	result = []
	for count in numbers:
		if count == 5 or count == 24:	
			result.append(count)
	return result
numbers = [5, 46, 7, 12,24]
result_num = check_two_numbers(numbers)
print(result_num)	