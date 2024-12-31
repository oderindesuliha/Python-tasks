total = 0
average = 1
numbers = 0
product = 1
largest = 0
smallest = 3343567889568
for numbers in range(1,4):
	numbers = int(input("Enter a number: "))
	total += numbers 
	average = total/3
	product *= numbers
	if(numbers > largest):
		largest = numbers
	if(numbers < smallest):
		smallest = numbers
	
	
	
print("total is",total)
print("average is",average)
print("product is",product)
print("largest is",largest)
print("smallest is",smallest)
