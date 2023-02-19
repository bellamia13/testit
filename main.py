interest_rate = float(input('Enter interest rate: '))
initial_investment = float(input('Enter initial investment amount:'))
finalAmount = initial_investment
year = 0

while finalAmount < 3 * initial_investment:
  finalAmount=finalAmount+(finalAmount*(interest_rate/100))
  year+=1
print('The number of years it takes the investment to double is', year)