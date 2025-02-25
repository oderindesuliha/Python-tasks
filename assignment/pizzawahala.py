class pizzawahala:
	def pizza_order():
		menu()
		
	def menu():

		number_of_guests = 0

	print("WELCOME TO IYA MOSES PIZZA JOINT!!!")
 
	number_of_guests = int(input("Enter the total number of guests: "))

	
	print("""
		pizza_type		number_of_slices		price_per_box
		1. Sapa size			4			    2,500 
		2. Small money		6			    2,900
		3. Big boys			8			    4,000
		4. Odogwu			12			    5,200
	""")
	
	pizza_type = int(input("enter the pizza type: "))
	
	while pizza_type not in [1, 2, 3, 4]:
		pizza_type = int(input("invalid input!.......Enter either 1, 2, 3, 4 to choose pizza type: "))
	
	slices = 0
	price = 0
	pizza_type_name = ""

	match(pizza_type):
		case 1:
			slices = 4
			price = 2500
			pizza_type_name = "Sapa size"
			
		case 2:	
			slices = 6
			price = 2900
			pizza_type_name = "Small money"

		case 3:	
			slices = 8
			price = 4000
			pizza_type_name = "Big boys"

		case 4:	
			slices = 12
			price = 5200
			pizza_type_name = "Odogwu"

	total_slices = number_of_guests
	number_of_boxes = total_slices // slices
	if(total_slices % slices != 0):
		number_of_boxes += 1
	print("Your ordered" , number_of_boxes , pizza_type_name , "box(es)")
	
	slices_left = number_of_boxes * slices - total_slices
	total_price = number_of_boxes * price
	print("Number of slices left after serving is" , slices_left, "slices")
	print("Your order is" , number_of_boxes , pizza_type_name , "pizza box(es) for" , total_price)