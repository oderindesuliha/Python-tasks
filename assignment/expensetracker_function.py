from datetime import datetime

expenses = []

def add_expense(date, description, amount):
	expenses.append({"date": date, "description": description, "amount": amount})  	
	print("Expenses added!\n")
	choice = int(input(option_list))
	main_menu(choice)
	

def view_expenses():
	print("\nExpenses:")
	count = 0
	for count in range(len(expenses)):
		expense_list = expenses[count]
		print(f"{count + 1}. Date: {expense_list['date']}, Description: {expense_list['description']}, Amount: ₦{expense_list['amount']:.2f}\n")
			
	choice = int(input(option_list))
	main_menu(choice)

def calculate_total():
	
	total = sum(expense_list['amount']for expense_list in expenses)
	print(f"\nTotal Expenses: ₦{total:.2f}\n")  
	choice = int(input(option_list))
	main_menu(choice)


def main_menu(choice):
	while choice not in [1, 2, 3, 4]:
		print(option_list)
		choice = int(input("Please enter a valid option: "))

	if choice == 1:
		date = str(input("Enter the date: "))
		
		#year=int(input("Please enter year: "))
		while year < 1900 or year > datetime.now().year:
			#year = int(input("Invalid year..... enter a year between 1900 and 2025: "))
		#month=int(input("Please enter month: "))
			while month < 1 or month > 12:
			#month = int(input("Invalid month..... enter a month between 1 and 12: "))
		#day=int(input("Please enter day: "))
				while day < 1 or day > 31:
			#day = int(input("Invalid day...... enter a day between 1 and 31: "))
					date =  f"{year}-{month:02d}-{day:02d}"		
			
		
		print(f"\nEnter the date(YYYY-MM-DD): {date}")
		
		description=input("Enter the description: ")
		amount=float(input("Enter the amount: "))
		while amount < 0:
			amount = float(input("Invalid amount"))
		add_expense(date, description, amount)

	if choice == 2:
		view_expenses()

	if choice == 3:
		calculate_total()

	if choice == 4:
		print("Exiting the app. Goodbye!")



print("WELCOME TO SEMICOLON EXPENSE TRACKER APP")
print("-" * 45)

option_list = ("1. Add an expense\n"
		"2. View all expenses\n"
		"3. Calculate total expenses\n"
		"4. Exit\n"
		"\nEnter your choice: ")

choice = int(input(option_list))
main_menu(choice)