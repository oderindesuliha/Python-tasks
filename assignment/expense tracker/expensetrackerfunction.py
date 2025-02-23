from datetime import datetime

date_time = []
description_list = []
amount_list = []

def add_expense(date, description, amount):
	date_time.append(date)
	description_list.append(description)
	amount_list.append(amount)
	print("Expenses added!")
	choice = int(input(option_list))
	main_menu(choice)

def view_expenses():
	count = 0
	for count in range(len(description_list)):
		print(f"{count + 1}. Date: {date_time[count]}, Description: {description_list[count]}, Amount: ₦{amount_list[count]:.2f}")	
	choice = int(input(option_list))
	main_menu(choice)

def calculate_expenses():
	total = sum(amount_list)  
	print(f"Total Expenses: ₦{total:.2f}")  
	choice = int(input(option_list))
	main_menu(choice)


def main_menu(choice):
	while choice not in [1, 2, 3, 4]:
		print(option_list)
		choice = int(input("Please enter a valid option: "))

	if choice == 1:
		year=int(input("Please enter year: "))
		while year < 1900 or year > datetime.now().year:
			year = int(input("Invalid year..... enter a year between 1900 and 2025: "))
		month=int(input("Please enter month: "))
		while month < 1 or month > 12:
			month = int(input("Invalid month..... enter a month between 1 and 12: "))
		day=int(input("Please enter day: "))
		while day < 1 or day > 31:
			day = int(input("Invalid day...... enter a day between 1 and 31: "))
			
		#date = datetime(year, month, day).strftime('%Y-%m-%d')
		date = str(year)+"-"+str(month)+"-"+str(day)
		print(f"Enter the date(YYYY-MM-DD): {date}")
		
		description=input("Enter the description: ")
		amount=float(input("Enter the amount: "))
		while amount < 0:
			amount = float(input("Invalid amount"))
		print(add_expense(date, description, amount))

	if choice == 2:
		view_expenses()

	if choice == 3:
		calculate_expenses()

	if choice == 4:
		print("Exiting the app. Goodbye!")



print("WELCOME TO SEMICOLON EXPENSE TRACKER APP")
print("-" * 45)

option_list = ("1. Add an expense\n"
		"2. View all expenses\n"
		"3. Calculate total expenses\n"
		"4. Exit\n"
		"Enter your choice: ")

choice = int(input(option_list))
main_menu(choice) 








		
		