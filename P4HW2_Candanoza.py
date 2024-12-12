# Nicholas Candanoza
# P4HW2
# 11/7/2024
# 

def calculate_pay(rate, hours):
    # Calculate regular pay (up to 40 hours)
    regular_hours = min(hours, 40)
    regular_pay = regular_hours * rate

    # Calculate overtime pay (anything over 40 hours)
    overtime_hours = max(0, hours - 40)
    overtime_pay = overtime_hours * rate * 1.5

    # Calculate gross pay (regular pay + overtime pay)
    gross_pay = regular_pay + overtime_pay

    return regular_pay, overtime_pay, gross_pay


def main():
    total_regular_pay = 0
    total_overtime_pay = 0
    total_gross_pay = 0
    employee_count = 0

    while True:
        # Ask for employee's name
        employee_name = input("Enter employee's name (or type 'Done' to Terminate): ").strip()

        if employee_name.lower() == 'done':
            break

        # Ask for pay rate and hours worked
        try:
            pay_rate = float(input(f"Enter {employee_name}'s pay rate ($/hour): "))
            hours_worked = float(input(f"Enter {employee_name}'s hours worked: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for pay rate and hours worked.")
            

        # Calculate pay details
        regular_pay, overtime_pay, gross_pay = calculate_pay(pay_rate, hours_worked)

        # Display individual employee's pay details
        print(f"\n{employee_name}'s Pay Details:")
        print(f"Regular Pay: ${regular_pay:.2f}")
        print(f"Overtime Pay: ${overtime_pay:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}\n")

        # Accumulate totals
        total_regular_pay += regular_pay
        total_overtime_pay += overtime_pay
        total_gross_pay += gross_pay
        employee_count += 1

    # Display Exit on employee's name or "Done"
    print("\n--- Enter employee's name (or type 'Done' to Terminate ---")
    print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
    print(f"Total Regular Pay: ${total_regular_pay:.2f}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Number of Employees Entered: {employee_count}")

# When function uses user's name 
if __name__ == "__main__":
    main()

