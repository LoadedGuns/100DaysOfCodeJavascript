print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to leave? 10 12 15 "))
people = int(input("How many total people to split the bill? "))
tipAsPercent = tip / 100
totalTipAmmunt = bill * tipAsPercent
totalBill = bill + totalTipAmmunt
billPerPerson = totalBill / people
finalAmount = round(billPerPerson, 2)
print(f"Each person should pay: ${finalAmount}")