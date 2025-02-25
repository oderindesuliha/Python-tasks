def sum_all_input(number):
	total = 0
	for count in str(number):
		total += int(count)

	return total

numbers_sum =  (sum_all_input(72349))
print(numbers_sum)
		