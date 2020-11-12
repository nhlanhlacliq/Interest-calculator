#finance calculators

#module imports
import math

#Getting user to select which calculator they want to use.
print("Choose either 'investment' or 'bond' calculator from the menu below to proceed:")
print("(TIP: You can type in the first 3 letters of your response. That works too.)\n")
calc_type = str(input("investment   -to calculate the amount of interest you'll earn on interest\nbond         -to calculate the amount you'll have to pay on a home loan \n> "))

#Converting input to lowercase letters so it isnt affected by any capitilization
calc_type = calc_type.lower()

#allowing user to type in just the first 3 letters of response for faster use, or if they spell the rest of the response incorrectly.
#getting details of the investment and displaying result.
if calc_type == "investment" or calc_type[:3] == "inv":
    invest_money = float(input("How much are you depositing?\n> "))
    rate = float(input("How much is the interest rate? e.g. 8.5 :\n> "))
    invest_years = int(input("How many years are you planning to invest for?\n> "))
    interest = input("Are you utilizing 'simple' or 'compound' interest :\n> ").lower()

    #calculating result based on users selection, asking user to try again if selection is incorrect
    if interest == 'simple' or interest[:3] == "sim":
        total_amount = invest_money * (1 + (rate/100) * invest_years)
    elif interest == 'compound' or interest[:3] == "com":
        total_amount = invest_money * math.pow((1 + (rate/100)), invest_years)
    else:
        print("That interest type isn't recognized. please try again.")    

    print(f"The amount you will have after your investment matures is {round(total_amount, 2)}.")

#if the user chooses bond calculator 
#the bond repayment amount is calculated using the bond repayment formula
elif calc_type == "bond" or calc_type[:3] == "bon":
    house_value = float(input("What is the present value of the house? e.g. 10000 :\n> "))
    bond_rate = float(input("How much is the interent rate? e.g. 7\n> "))/100
    bond_months = int(input("How many months do you plan to take to repay the bond? e.g. 120 \n> "))
    monthly_rate = bond_rate / 12 
    
    bond_repay_amount = (monthly_rate * house_value) / (1 - (math.pow((1 + monthly_rate), (-1 * bond_months))))
    
    print(f"You will have to pay {round(bond_repay_amount, 2)} every month for this bond.")

#The programs asks the user to try again if they chose neither bond or investment calculator
else:
    print("Your input unfortunately cannot be used. please try again")