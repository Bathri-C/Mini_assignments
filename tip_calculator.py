print("Welcome to Tip Calculator.")
total_bill=float(input("What was the Total Bill ? : Rs."))
tip=int(input("How much tip would you like to give 10,12,15 : "))
people=int(input("How many people to split the bill? : "))
total_amount=(total_bill+(total_bill*(tip/100)))/people
print(f"Each person should pay {round(total_amount,2)}")
