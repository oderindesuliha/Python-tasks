number =int(input('enter a number between 0 and 1000: '))
total = 0
while number > 0 :
	digit = number % 10
	total += digit
	number //= 10

print(total)
	
