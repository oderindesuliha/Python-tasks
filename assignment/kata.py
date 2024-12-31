class kata:
	def iseven(number):
	  if number % 2 == 0:
      		return True
	  else :
     	 	return False
	number = int(input('enter an even number(or not): '))
	result = iseven(number)
	print(result)
	
	def isPrimeNumber(number):
	   if number <= 1:
	      return False	
	   counter = 0	
	   for count in range(1, number + 1):
	      if number % count == 0:
	       counter += 1
	   if counter == 2:
	       return True
	   else :
	       return False
	
	number = int(input('enter a prime number(or not): '))
	result = isPrimeNumber(number)
	print(f"Is {number} a prime number? {result}")
	
	def subtract(number1 , number2):
		if number2 > number1:
		   return number2 - number1
		else :
		   return number1 - number2
	
	number1 = int(input('enter a number: '))
	number2 = int(input('enter a number: '))
	result = subtract(number1, number2)
	print(result)

	def divide(firstnumber , secondnumber):
		if secondnumber == 0:
		    return 0
		else :
		    return firstnumber / secondnumber
	  
	firstnumber = int(input('enter a number: '))
	secondnumber = int(input('enter a number: '))
	result = divide(firstnumber , secondnumber)
	print(result)
	
	def factorOf(digit):
	  count = 0
	  for counter in range (1, digit + 1):
	    if digit % counter == 0:
	       count += 1
	  return count
	digit = int(input('enter a number(factor): '))
	count = factorOf(digit)
	print(f"the factors of {digit} are {count}")

	def isSquare(number3):
	  for counter in range(1, number3 + 1):	
	    if counter * counter == number3:
	       return True	
	  return False
	number3 = int(input('enter a number(isSquare): '))
	result = isSquare(number3)
	print(result)
	
	def isPalindrome(number):
	   lastDigit = number // 10000
	   fourthDigit = number // 1000 % 10             
	   secondDigit = number // 10 % 10
	   firstDigit = number % 10

	   if firstDigit == lastDigit and secondDigit == fourthDigit: 
	       return True
	   return False	
	number = int(input('enter a number(Palindrome): '))
	result = isPalindrome(number)       
	print(f"Is the number {number} palindrome? {result}")

	def factorialOf(number):
		count = 1
		for counter in range(2, number + 1):
			count *= counter
		return count
	number = int(input('enter a number(factorial): '))
	result = factorialOf(number)       
	print(f"The factorial of {number} is {result}")

	def squareOf(number):
		return number * number
	number = int(input('enter a number(square): '))
	result = squareOf(number)       
	print(f"The square of {number} is {result}")











