# Nicholas Candanoza
# P4LAB2
# 10/31/2024
# Program ask user for integer and displays multiplication table for positive

# While loop to control program running continuously
run_again = "yes"

while run_again == "yes" or run_again == "y" :
    user_int = int(input("Enter an integer: "))
    print()
    if user_int >= 0:
        # Print multiplication table
        print("simulate math printing...")
        for num in range(1,13):
            print(f"{user_int} * {num} = {user_int * num}")
    else:
        print("Cannot accept negative values!!")
        
    print()
    run_again = input("Would you like to run the program again?").lower()[0]
    valid_inputs = ["yes", "y","no","n"]
    # Validate the user's input
    while run_again not in valid_inputs:
        print("INVALID RESPONSE ENTERED!")
        run_again = input("Would you like to run the program again?").lower()[0]

# Loop breaks
print("Exiting program...")

