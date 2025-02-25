def get_letters(word, alphabet: str)->bool:	
	for words in alphabet:
		for words in word:
			if word == alphabet:
				return True

			else: return False
word = 'madam'
alphabet = 'damam'
print(get_letters(word, alphabet))


   