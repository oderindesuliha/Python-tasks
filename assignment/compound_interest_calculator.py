class CompoundInterestCalculator:
    def compound_interest(number):
        try:
            
            initial_investment = float(input("Enter your initial investment($): "))
            if initial_investment <= 0:
                print("Invalid!!... Enter a valid Initial investment.")
                return

            
            monthly_contribution = float(input("Enter your monthly contribution($): "))
            if monthly_contribution < 0:
                print("Invalid!!... Enter a valid monthly contribution.")
                return

            
            years = int(input("Enter number of years: "))
            if years <= 0:
                print("Invalid!!... Retry!")
                return

            
            interest_rate = float(input("Enter the annual interest rate (%): "))
            if interest_rate <= 0:
                print("Invalid!!... Re-enter interest rate.")
                return
            interest_rate /= 100 

            
            print("Choose compound frequency: ")
            print("1. Daily\n2. Monthly\n3. Annually\n4. Bi-annually\n5. Quarterly")
            choice = int(input("Enter an option (1-5): "))
            compound_frequencies = {
                1: 365,
                2: 12, 
                3: 1, 
                4: 2,    
                5: 4     
            }
            compound_frequency = compound_frequencies.get(choice, None)
            if not compound_frequency:
                print("Invalid choice! Please enter a valid option (1-5).")
                return

            
            amount = initial_investment
            periodic_rate = interest_rate / compound_frequency

            for count in range(1, years * compound_frequency + 1):
                amount += monthly_contribution / (compound_frequency / 12.0)
                amount *= (1 + periodic_rate)

            interest = amount - (initial_investment + monthly_contribution * years * 12)
            print(f"Total Interest Earned($): {interest:.2f}")
            print(f"Future Investment Value($): {amount:.2f}")

        except ValueError:
            print("Invalid input! Please enter numeric values where required.")


calculator = CompoundInterestCalculator()
calculator.compound_interest()
