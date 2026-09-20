bill = int(input("how much did the meal cost?"))
tip_perc = int(input("What percent of the bill would you like to pay as a tip?"))
tip = 0


def total_calc():
    tip = bill*(tip_perc/100)
    print(bill+tip)

total_calc()
