
age = int(input("enter the age enter by user: "))
day = "wednesday"

price = 12 if age >=18 else 8

if day == "wednesday":
   price = price - 2

print("Ticket price for you is",price)