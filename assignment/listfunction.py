def largest_element(numbers):
	largest = numbers[0]
	for count in numbers:
		if count > largest:
			largest = count
	return largest	
numbers = [5, -1, 10, 20, 2]
largest_result = largest_element(numbers)
print ("The largest number is: ", largest_result)

def reverse(numbers):
	return numbers[::-1]
numbers = [5, -1, 10, 20, 2]
reverse_result = reverse(numbers)
print ("The reverse of the numbers: ", reverse_result)

def element_occurrence(user_input, element):
    return element in user_input
element = 10
numbers = [5, -1, 10, 20, 2]
if element_occurrence(numbers, element):
    print("The element", element, "exists in the list.")
else:
    print("The element", element, "does not exist in the list.")

def odd_positions(elements):
    result = []
    for count in range(len(elements)):
        if count % 2 == 1:
           result.append(elements[count]) 
    return result
elements = [5, 10, 15, 20, 25, 30, 45, 15, 35, 50]
oddly_placed_elements = odd_positions(elements)
print("The oddly placed elements :", oddly_placed_elements)

def even_positions(elements):
	result = []
	for count in range(len(elements)):
		if count % 2 == 0:
			result.append(elements[count])
	return result
elements = [15, 30, 24, 55, 37, 21, 4, 10, 33, 56]
evenly_placed_elements = even_positions(elements)
print("The evenly placed elements :", evenly_placed_elements)

def total(elements):
	total = 0
	for number in elements:
		total += number
	return total
elements = [10, 20, 30, 40]
total_sum = total(elements)
print("The sum total of all elements is: " , total_sum)

def ispalindrome(string):
	if string == string[::-1]:
		return "is palindrome"
	else:
		return "is not palindrome"
string = input("enter string: ")
print(string , ispalindrome(string))

def for_sum(numbers):
	sum = 0
	for count in numbers:
		sum += count
	return sum
numbers = [-2, 5, 10, 10]
sum_total = for_sum(numbers)
print("The for_sum total of all numbers is: " , sum_total)

def while_sum(numbers):
	total = 0
	count = 0
	while count < len(numbers):
		total += numbers[count]
		count += 1
	return total
numbers = [5, 5, 5, 5, 5]
total_while = while_sum(numbers) 
print("The while_sum total of all numbers is: " , total_while)

def concatenate(characters, numbers):
	result = []
	return characters + numbers
characters = ['a', 'b', 'c']
numbers = [1, 2, 3]
concatenate_result = concatenate(characters, numbers)
print("The result is:" , concatenate_result)

def combine_list(characters, numbers):
	combined_list = []    
	for char, number in zip(characters, numbers):
		combined_list.append(char)
		combined_list.append(number)
	combined_list.extend(characters[len(numbers):])
	combined_list.extend(numbers[len(characters):])
	return combined_list
characters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combined_list = combine_list(characters, numbers)
print("The result is:" , combined_list)

def return_list(numbers):
	numbers = [int(count) for count in numbers.split()]
	return numbers
numbers = input("enter numbers: ")
number_list = return_list(numbers)
print('List of digits:', number_list)







