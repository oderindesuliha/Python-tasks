class compound_interest_calculator:
	def interest_calculator(self):
		initial_investment = double(input("enter initial investment: "))
		monthly_contribution = double(input("enter monthly contribution: "))
		years = int(input("enter number of years: "))
		interest_rate = double(input("enter annual interest rate(%): "))
		print("1. Daily\n2. Monthly\n3. Annually")
		compound_frequency = int(input("Choose compound frequency: "))

		
		match(compoundFrequency):
            		case "days":
		amount = initial_investment * ((1 + interest_rate // 365)**(365 * years))
				print(f"Compound interest is %.2f%n , amount")

           		case "month":
		amount = initial_investment * ((1 + interest_rate // 12)**(12 * years))
				print(f"Compound interest is %.2f%n , amount")

          		case "year":
		amount = initial_investment * ((1 + interest_rate // 1)**(1 * years))
				print(f"Compound interest is %.2f%n , amount")	
		
		

		for _ in range years
			 interest = monthlyContribution * Math.pow(1 + interestRate / compoundFrequency , compoundFrequency * (years - (count / 12.0)))
			
		print(f"Total future interest is %.2f%n , interest")

calculator = compound_interest_calculator()
calculator.interest_calculator()