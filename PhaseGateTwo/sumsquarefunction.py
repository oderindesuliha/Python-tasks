def get_square(number: list)->int:
	total = 0
	for counter in number:	
		 total += counter * counter 
		
	return total

number =[1,2,3,4]
print(get_square(number))
