import math

print("Hello! Please choose either 'Investment' or 'Bond' from the menu below to proceed:")

print("Investment   - to calculate the amount of interest you'll earn on interest")
print("Bond         - to calculate the amount you'll have to pay on a home loan\n")
print("From this we will ask you to put through information needed to calculate the above.")
# started with a variable that requires the user to choose between investment or bond

inv_bond = input("Enter Here: ")
# to adhere to the task i used the .lower() on the variable to allow the user to enter variations of each word
# used an if statement for the choice made by user
print("\n")
if inv_bond.lower() =="bond":        
    value = float(input("Enter the present value of your property: R"))
    inrate = float(input("Enter the interest rate.(do not add %): "))
    months = int(input("Enter the number of months needed to pay back the bond: "))
    # as per feedback i corrected the monthly interest rate
    mon_intrate = float(inrate/100)/12
    # as per feedback i corrected the bond formula.
    total_amt = (mon_intrate * value)/(1-(1 + mon_intrate)**(-months))
    print("Your monthly repayment is calculated as: R",round(total_amt, 2))

# continued with an elif and moved the else to the end of the statement to avoid errors.
elif inv_bond.lower() =="investment":
    deposit = float(input("Enter the amount you would like to deposit: R"))
    rate = float(input("Enter the interest rate.(do not add %): "))
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("What type of interest would you prefer - Simple or Compound?: ")
    # used nested if statements for the interest formulas 
    if interest.lower() =="simple": 
       total_amt = deposit * (1 + (rate/100) * years)
       print("Your amount earned on simple interest :R",round(total_amt, 2))
    elif interest.lower() == "compound":
       total_amt = deposit * math.pow(1 + (rate/100), years) 
       print("Your amount earned on compound interest :R",round(total_amt, 2))
    else:
         print("Incorrect input")
else :
     print("Error,incorrect input")

# I thank you for your constructive feedback and appreciated the guidelines and tips, hope this one can better my results.
