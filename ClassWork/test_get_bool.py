def get_truefalse_for_evenold(elements)-> bool:
	result = []
	count = 0
	for element in range(0, len(elements)-1):
		if count % 2 == 0:
			result.append(True)
		else: count % 2 != 0
	result.append(False) 
	return result
		  
elements = [8, 0, -2, 5, 8, 4, -6, "k"]	
list_of_boolean = get_truefalse_for_evenold(elements)
print(list_of_boolean)
