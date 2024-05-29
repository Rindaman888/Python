#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Hello Test!!")
bill = float(input("What was the total bill? $"))
tip = int(input("How Much Tip would you like to give? 10, 12, or 15? "))
p = int(input("How many people to split the bill? "))
total_as_percent = tip / 100
total_tip_amount = bill * total_as_percent
total_bills = bill + total_tip_amount
bill_per_person = total_bills / p
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(final_amount)