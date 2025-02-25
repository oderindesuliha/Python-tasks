def get_thenumberofvowels(words)-> int:
	number_of_vowels = 0
	for letter in words:	
		if letter == 'a' or letter == 'e' or letter == 'i' or letter ==  'o' or letter == 'u':
			number_of_vowels += 1
	return number_of_vowels
words = "PYTHON IS SWEET"
print(get_thenumberofvowels(words))