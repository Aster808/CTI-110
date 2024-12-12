# Candanoza, Nicholas
# 10/22/2024
# P3LAB
# Calculate coin combinations for given value

'''
# Regular Division
print(100/3)

# Floor Division/- returns the whole number
print(100/3)
# Module Division/ return the remainder only as an integer
print(100%3)
print(7%4)
'''

# Get the money value from user as a float
money = float(input("Enter the amount of money as a float: $"))

# Convert money to a whole number
money = round(money * 100)

#print(money)

# Calculate the amount of dollars in the money variable
num_dollars = money // 100
print(f"Dollars : {num_dollars}")

# Remove the dollars from money variable
money = money - (num_dollars * 100)
# Calculate the amount of quarters in the money variable
num_quarters = money // 25
print(f"Quarters: {num_quarters}")

# Remove the quarters from money varible
money = money - (num_quarters * 25)

# Calculate the amount of dimes in the money variable
num_dimes = money // 10
print(f"Dimes: {num_dimes}")

# Remove the dimes from money varible
money = money - (num_dimes * 10)

# Calculate the amount of nickels in the money variable
num_nickel = money // 5
print(f"Nickel: {num_nickel}")

# Remove the nickels from money varible
money = money - (num_nickel * 5)

# Create a variable for pennies
num_pennies = money
print(f"Pennies: {num_pennies}")

# Print dollar amount gramatically
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} dollar")
    else: # variable is greater than one
        print(f"{num_dollars} dollars")

# Print quarters amount gramatically
if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} quarters")
    else: # variable is greater than one
        print(f"{num_quarters} quarters")

# Print dimes amount gramatically
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} dimes")
    else: # variable is greater than one
        print(f"{num_dimes} dimes")

# Print nickels amount gramatically
if num_nickel > 0:
    if num_nickel == 1:
        print(f"{num_nickel} nickel")
    else: # variable is greater than one
        print(f"{num_nickel} nickel")

# Print pennies amount gramatically
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} pennies")
    else: # variable is greater than one
        print(f"{num_pennies} pennies")



