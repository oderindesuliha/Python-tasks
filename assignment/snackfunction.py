class snackfunction:
	def logistics(successful_deliveries):
		successful_deliveries = int(input("enter the number of successful deliveries: "))
		riders_pay = 0

		if successful_deliveries < 50:
			 riders_pay = successful_deliveries * 160 + 5000

		elif successful_deliveries >= 50 and successful_deliveries <= 59:
			riders_pay = successful_deliveries * 200 + 5000

		elif successful_deliveries >= 60 and successful_deliveries <= 69:
			riders_pay = successful_deliveries * 250 + 5000	

		else:
			riders_pay = successful_deliveries * 500 + 5000
	
		
		print("Rider's pay is: " , riders_pay,"Naira")
		return riders_pay
		

function = snackfunction()
function.logistics()
	