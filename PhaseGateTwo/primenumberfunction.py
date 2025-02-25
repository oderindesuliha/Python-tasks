def get_primenumber(number)-> bool:	
	   counter = 0	
	   for count in range(1, number + 1):
	      if number % count == 0:
	       counter += 1
	   if counter == 2:
	       return True
	   else :
	       return False
	
number = 7
print(get_primenumber(number))
	