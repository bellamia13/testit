print("Welcome!")
Name = input("Enter Company Name: ")
Feets = float(input("Enter the number of feet of fiber optic to be installed: "))
if Feets > 100:
    Cost = Feets * 0.80
elif Feets > 250:
    Cost = Feets * 0.70
elif Feets > 500:
    Cost = Feets * 0.50
else:
    Cost = Feets * 0.87
print("Cost for the Company", Name, "is", Cost)