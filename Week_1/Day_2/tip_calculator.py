#Tip Calculator

#Program Intro
print("Welcome to your Tip calculator")

#Getting Bill Value
bill_value_without_tip = float(input("What was the total bill? $"))
#Getting group size
people = float(input("How many people is in your group?" ))
#Diving the bill
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?" ))

if tip == 10:
    tip_value = bill_value_without_tip + (bill_value_without_tip* 0.10)
elif tip == 12:
    tip_value = bill_value_without_tip + (bill_value_without_tip* 0.12)
elif tip == 15:
    tip_value = bill_value_without_tip + (bill_value_without_tip* 0.15)

#Value that each person will need to pay
pay_per_person = tip_value / people
print(f"Each person should pay: ${round(pay_per_person,2)}")