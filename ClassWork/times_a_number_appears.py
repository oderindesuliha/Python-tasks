def check_for_the_times_a_number_appears(number, search):
	number = str(number)
	count= 0	
	for counter in number:
		if search ==  int(counter):
			count+=1
	return count


search = int(input("Enter a number: "))
number= check_for_the_times_a_number_appears(3748992, search)
print (number)