def get_anagram(firstWord, secondWord: str)->bool:
	anagram = 0
	for word in secondWord:
		if sorted(word) == sorted(firstWord):
			anagram.append(word)
			return True
		else:
			return False
firstWord = 'listen'
secondWord = 'silent'
print(get_anagram(firstWord, secondWord))