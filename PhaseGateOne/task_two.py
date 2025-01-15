number = 0
thirdDigit = number // 10
secondDigit = number // 10% 10             
firstDigit = number % 10	
number = int(input('enter a number between 0 and 100: '))
result = firstDigit + secondDigit +thirdDigit
print(result)   
