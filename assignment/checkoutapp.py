from datetime import datetime
items = []
quantity = []
price = []
total = []
date_Time = datetime.now()
sub_Total = 0
discountAmount = 0
price_Total = 0
choice = "yes"

name =  input("Customer's name: ")
while choice == "yes" and choice != "no" :		
	item = input("What did the Customer buy?: ")	
	items.append(item)
	pieces = int(input("How many pieces?: "))
	quantity.append(pieces)
	amount = int(input("How much per unit?: "))
	price.append(amount)
	stotal = amount * pieces
	sub_Total += stotal
	total.append(stotal)

	choice = input("Do you want to add more items?: ")
	while choice.lower() != "yes" and choice.lower() != "no":
		choice = input("Wrong input, please kindly choose yes or no ")
	while choice == "yes" and choice != "no"and choice != "Yes" and choice != "yEs" and choice != "yeS"and choice != "No"and choice != "nO" and choice != "NO" and choice != "YES":
		break
cashier_name = input("What is the cashier name?: ")
amount = 0
pieces = 0
discount_percentage = int(input("Enter percentage discount(%): "))
sub_Total = price_Total
discountAmount = price_Total * (discount_percentage / 100)
vat = (17.50 / 100) * (sub_Total - discountAmount)
bill = sub_Total - discountAmount + vat

print("")
print("")
print("SEMICOLON STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL: 09093372810")
print(f"CASHIER: {cashier_name}\nCUSTOMER NAME: {name}\t")
print(f"DATE: {date_Time}\n")
print("==========================================")
print("ITEM\tQTY\tPRICE\tTOTAL(NGN)")

for count in range(len(items)):
   print(f'{items[count]}\t\t{quantity[count]}\t\t{price[count]}\t\t{total[count]} ')
print("-------------------------------------------")
print('\t\t\t' ,"Total: ", price_Total)
print('\t\t\t' ,"Discount: ", discountAmount)
print('\t\t\t' ,"VAT @ 17.50%: ",  vat)
print("==========================================")
print('\t\t\t',"Bill Total: ", bill)
print("==========================================")
print('\t',"THIS IS NOT A RECEIPT. KINDLY PAY: ",  bill )
print("==========================================\n")


print("")
paid_Amount = int(input("How much did the customer give to you?: "))
balance = paid_Amount - bill

print("")
print("")
print("SEMICOLON STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.\nTEL: 09093372810")
print(f"CASHIER: {cashier_name}\nCUSTOMER NAME: {name}\t")
print(f"DATE: {date_Time}\n")
print("==========================================")
print("ITEM\tQTY\tPRICE\tTOTAL(NGN)")

for count in range(len(items)):
   print(f'{items[count]}\t{quantity[count]}\t{price[count]}\t{total[count]} ')
print("-------------------------------------------")
print('\t\t\t',"Total: ", price_Total )
print('\t\t\t',"Discount: ", discountAmount)
print('\t\t\t',"VAT @ 17.50%: ",  vat)
print("==========================================")
print('\t\t\t', "Bill total: ", bill)
print('\t\t\t', "Amount paid: ", paid_Amount)
print('\t\t\t', "Balance: ", balance)
print("==========================================")
print("THANK YOU FOR YOUR PATRONAGE!!!")
print("==========================================\n")





  
		