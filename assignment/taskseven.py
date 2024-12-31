for counter in range(1, 10):
	number = 1
	total = 0
	if counter % 4 == 0:
		for count in range(1, 6):
			number = counter * number
			total += number
		print(total,end=" ")			
			