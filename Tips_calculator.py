print("Welcome to the tip calculator")
total_bill=float(input("What is the total bill?: "))
tip=float(input("What percent of tip you want to give? 10,12 or 15? "))
total_pay=total_bill+tip
person_to_split=float(input("How many person you want to split the bil?: "))
bill_per_person=(total_pay/person_to_split)
final_amount=round(bill_per_person,2)
print(f"Each person should pay $ {final_amount}")