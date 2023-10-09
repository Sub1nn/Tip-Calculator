# print("Welcome to the tip calculator!")
# Total = float(input("how much was the total cost?"))
# print(Total)
# Tip = float(input("what is the tip in percentage?"))
# print(Tip)
# percentage = (Tip / 100) * Total
# print("The tip amount is: ", percentage)
# All_Total = Total + percentage
# print("Total cost including tip: ", All_Total)

print("Welcome to the tip calculator")
total_bill = float(input("what is the total bill?"))
print(total_bill)
people_num = float(input("How many people are sharing the bill?"))
print(people_num)
tip_percent = float(
    input("How much would you like to tip? 10, 15 or 20 percentage"))
print(tip_percent)
total_tip = (tip_percent / 100) * total_bill
all_total = total_bill + total_tip
print("The total amount including the tip is: ", all_total)
each_share = all_total / people_num
print("Each Person should pay: ", each_share)
