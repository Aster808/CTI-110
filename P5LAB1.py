# Nicholas Candanoza
# P5LAB
# 11/15/2024
# Use functions to simulate self-checkout

import random

def calcCashBack():
    # Generate a random float for amount owed to store
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed :.2f}")
    cash = float(input("How much cash will you put in the self-checkout?"))
    # Calculate cash back
    cash_back = cash - total_owed
    return cash_back
    






def disperseCashBack(change):
    # Get the money value from user as a float

    # Convert money to a whole number
    change = int(round(change * 100, 2))

    print(change)

    if change == 0:
        print("No Change Due")

    # Calculate the amount of dollars in the money variable
    num_dollars = change // 100
    print(f"Dollars : {num_dollars}")

    # Remove the dollars from money variable
    change = change - (num_dollars * 100)
    # Calculate the amount of quarters in the money variable
    num_quarters = change // 25
    print(f"Quarters: {num_quarters}")

    # Remove the quarters from money varible
    change = change - (num_quarters * 25)

    # Calculate the amount of dimes in the money variable
    num_dimes = change // 10
    print(f"Dimes: {num_dimes}")

    # Remove the dimes from money varible
    change = change - (num_dimes * 10)

    # Calculate the amount of nickels in the money variable
    num_nickel = change // 5
    print(f"Nickel: {num_nickel}")

    # Remove the nickels from money varible
    change = change - (num_nickel * 5)

    # Create a variable for pennies
    num_pennies = change
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


# Define the main
def main():
    print("*******Welcome to the self-checkout!!!*******")
    cash_back = calcCashBack()
    print("Change is ${cash_back:.2f}")
    disperseCashBack(cash_back)
    

# Call the main
if __name__ == "__main__":
    main()

