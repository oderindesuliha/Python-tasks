total = 0
for counter in range(1, 11):
	number = 1
	if counter % 4 == 0:
		for count in range(1,6):
			number = counter * number
			total += number
		
print(total, end=" ")	