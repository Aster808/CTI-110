# Nicholas Candanoza 
# 10/24/2024
# P3HW2
# Calculate reg and OT pay, given an employees hours worked

def calculate_pay():
    # Input: Get employee details
    name = input("Enter employee name: ")
    hours_worked = int(input("Enter hours worked: "))
    pay_rate = float(input("Enter pay rate: "))

    # Initialize variables
    overtime_hours = 0
    overtime_pay = 0.0
    regular_pay = 0.0
    gross_pay = 0.0

    # Calculate pay based on hours worked
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
        gross_pay = regular_pay + overtime_pay
    else:
        regular_pay = hours_worked * pay_rate
        gross_pay = regular_pay

    # Output: Display results
    print("\nEmployee Name:", name)
    print("Total Hours Worked:", hours_worked)
    print("Regular Pay Rate: ${:.2f}".format(pay_rate))
    print("Overtime Hours Worked:", overtime_hours)
    print("Overtime Pay: ${:.2f}".format(overtime_pay))
    print("Regular Pay: ${:.2f}".format(regular_pay))
    print("Gross Pay: ${:.2f}".format(gross_pay))

# Run the function
calculate_pay()
