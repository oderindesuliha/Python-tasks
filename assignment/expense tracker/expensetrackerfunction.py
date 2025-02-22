date = []
description = []
amount = []
def choice():
	option = 0
		
	print("Welcome to Semicolon Expense Tracker App")
	print("----------------------------------------------------")
		

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
	
		option = str(input("Enter the date(YYYY-MM-DD): "))
		option = str(input("Enter the description: "))
		option = float(input("Enter the amount: "))
	print("Expense added!")

	choice()
	
	if  option == 2:
		print("Expenses: ")
		option = str(input("Enter the date(YYYY-MM-DD): "))
		option = str(input("Enter the description: "))
		option = float(input("Enter the amount: "))

	choice()

	if  option == 3:
		option = float(input("Total Expenses: "))

	choice()

	if  option == 4:
		print("Exiting the app. Goodbye!")

	


print(choice())