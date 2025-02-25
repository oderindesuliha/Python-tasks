import re
expenses = []

def add_expense(date, description, amount):
	date_regex = re.compile(r"^(?P<year>\d{4})-(?P<month>0[1-9]|1[0-2])-(?P<day>0[1-9]|[12]\d|3[01])$")
	
	match = date_regex.match(date)
	if not match:
		raise ValueError("Invalid date")

	if description.startswith(" "):
		raise ValueError("Invalid description")

	if not amount.isdigit():
		raise ValueError("Invalid amount")

	if int(amount) < 0:
		raise ValueError("Invalid amount")

	expenses.append({'date': date,'description': description,'amount': amount})
	
	return "Expense added!"
	
def view_all_expenses():
		
	for count in range(len(expenses)):
		expense_list = expenses[count]
	                   
	return(f"{count + 1}. Date: {expense_list['date']}, Description: {expense_list['description']}, Amount: ₦{float(expense_list['amount']):.2f}\n")

def calculate_total():
	
	total = sum(float(expense_list['amount'])for expense_list in expenses)
	return(f"\nTotal Expenses: ₦{total:.2f}\n")  




