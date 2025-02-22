date = []
description = []
amount = []
def choice():
	option = 0
		
	print("Welcome to Semicolon Expense Tracker App")
	print("-----------------------------------------------------------")
		

	print("""
		options:
		1. Add an expense
		2. View all expenses
		3. Calculate total expenses
		4. Exit 
		""")
	option = int(input("Enter your choice: "))
	while option not in [1, 2, 3, 4]:
		option = int(input("invalid input!.......Enter either 1, 2, 3, 4 : "))
		
		if  option == 1:
	
		option = int(input("Enter the date(YYYY-MM-DD): "))
		option = str(input("Enter the description: "))
		option = int(input("Enter the amount: "))
print("Expense added!")


print(choice())