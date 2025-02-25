def get_capitalizefirstletters(words: list)-> str:

	words= ([word.capitalize() for word in words])
	return (words)

words: ["apple", "banana", "cherry"]
print(get_capitalizefirstletters(words))
