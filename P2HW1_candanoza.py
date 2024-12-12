# Nicholas Candanoza

# 9/27/2024

# P2HW1

# Travel Expense Calculator



# Input budget and expenses

budget = float(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

gas_expense = float(input("How much do you think you will spend on gas? "))

accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))

food_expense = float(input("Last, how much do you need for food? "))



# Calculate total expenses and remaining balance

total_expenses = gas_expense + accommodation_expense + food_expense

remaining_balance = budget - total_expenses



# Display travel expenses

print("\n-----Travel Expenses-----")

print(f"Location: {destination}")

print(f"Initial Budget: {budget}")

print(f"Fuel: {gas_expense}")

print(f"Accommodation: {accommodation_expense}")

print(f"Food: {food_expense}")

print(f"Remaining Balance: {remaining_balance}")

