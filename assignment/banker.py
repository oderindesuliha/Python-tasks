class account:
    balance = 0
    def deposit(number):
        num_deposit = float(input('Enter a deposit amount (-1 to exit): '))
        if deposit == -1:
            return deposit  
        number += deposit
        print(f'Net balance: {number}')
    
    def withdrawal(number):
        num_withdrawal = float(input('Enter an amount to withdraw (-1 to exit): '))
        if withdrawal == -1:
            return withdrawal
        number -= withdrawal
        print(f'Net balance: {number}')

 
        while True: 
         option = input("Enter 1 for deposit, 2 for withdrawal, or 0 to exit: ")

       	if option == 1:
         userinput = float(input("Enter deposit amount: "))
        balance += userinput 
        elif option == 2:
        userinput2 = float(input("Enter withdrawal amount: "))
        if userinput2 == -1: 
         balance -= userinput2  

     elif option == 0:
        print(f'Net balance: {balance}')
        

     else:
        print('Please enter "1" for deposit or "2" for withdrawal.')
          