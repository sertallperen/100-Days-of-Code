# CREATE TIP CALCULATOR

# First, need a total bill.
# Second, need a percent of tip.        
# Third, need a information about how many people split the total price. 
# And find how much payment each person.

print("Welcome to tip calculator ! ")

bill = float(input("What was the total bill ? "))
tip = int(input("How much tip would you like to give ?  10, 12 or 15 ?"))
split = int(input("How many people to split the bill ? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / split

print("Each person should pay: ", "$",bill_per_person)