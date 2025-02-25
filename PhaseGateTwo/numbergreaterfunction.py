def get_numbergreater(numbers : list)-> int:
	for number in numbers:
		if type (number) == str:
			return 'Invalid input'
	
	numbers_greater_than_75=([number for number in numbers if number >= 75])
	return numbers_greater_than_75
	 
	

