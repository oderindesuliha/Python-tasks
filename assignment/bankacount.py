class Bankaccount:
	def bank_transaction(self):
		balance = 0.00
		user_input = 0

		while user_input != -1 :
			print("""
			transaction_options:
			1. Deposit
			2. Withdraw
			3. Check balance
			""")
			user_input = int(input("enter an option(or -1 to exit): "))

			match(user_input):
				case 1:
					user_input = float(input("enter an amount(or -1 to exit): "))
					if user_input <= 0:	
						print("invalid deposit amount")
					else: balance += user_input
					print("The new balance is: " , balance)

				case 2:
					user_input = float(input("enter an amount(or -1 to exit): "))
					if user_input <= 0:	
						print("invalid withdrawal amount")
					elif user_input > balance:
						print("Insufficient funds ")
					else: balance -= user_input
					print("The new balance is: " , balance)

				case 3:
					print("Your current balance is: ", balance)



account = Bankaccount()
account.bank_transaction()