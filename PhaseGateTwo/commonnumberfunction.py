def get_commonnumber(firstList,secondList)-> int:
	common_number =[]
	for count in firstList:
		for counter in secondList:
			if count == counter:
				common_number.append(count)
	return common_number

firstList = [1, 2, 3]
secondList = [3,4,6]
print(get_commonnumber(firstList,secondList))