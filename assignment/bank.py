class bankaccount: 
	def self_balance(self):
	 self_balance = 0
	 self_balance += deposit 
	def depositamount(self_balance):
	 self_deposit = float(input('enter a deposit amount(-1 to exit): '))
	 if deposit == 1:
	     return
	user_input = int(input("enter a number(or -1 to exit): "))	
	match user_input:
		case 3: 
		  balance()
		case 0:
		  mainmenu()
	transact_input = int(input('choose an option: '))

	def withdrawalamount(self):
	 self_withdrawal = float(input('enter an amount to withdraw(-1 to exit): '))
	 if withdrawal == 1:
	     return
	self_balance -= withdrawal
	match userinput:
		case 3: 
		  balance()
		case 0:
		  mainmenu()
	transact_input = int(input('choose an option: '))
	
	def options():
	   print("""
	   1. deposit
	   2. withdrawal
	   3. balance
	   """)
	   if user_input == 1:
            print("deposit")
	   elif user_input == 2:
            print("withdrawal")
	   elif user_input == 3:
            print("balance")
	   else:
	    print("exit")
	
	match user_input:
		case 1:
		  deposit()
		case 2:
		  withdrawal()
		case 3: 
		  balance()
		case 0:
		  mainmenu()
	transact_input = int(input('choose an option: '))
	
	print(f"Net balance: " ,{balance})