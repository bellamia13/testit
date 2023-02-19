



print("Welcome to my program!")

#ask the user for company name
company_name = input("Enter company name: ")

#ask user how many feet of fiber is needed
feets_of_fiber= float(input("Enter the number of feet of fiber optic to be installed: "))
cost_of_fiber= 0.0

# create if-elif statement
if feets_of_fiber >= 100 and feets_of_fiber < 250:
    cost = feets_of_fiber * .80
elif feets_of_fiber>=250 and feets_of_fiber<500:
    cost = feets_of_fiber* .70
elif feets_of_fiber>=500:
    cost = feets_of_fiber*.50
elif feets_of_fiber<100:
    cost = feets_of_fiber*.87
  #display total cost to the user
print("The cost for the company",company_name,"is",cost)