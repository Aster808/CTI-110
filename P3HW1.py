 # Candanoza, Nicholas

 # 10/10/2024

 # P3HW1

 # Grading Results

# Allow user to give list items
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))
num4 = float(input("Enter a number: "))
num5 = float(input("Enter a number: "))


# Empty list
num_list = []

'''
# Add variables to the list
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)
num_list.append(num5)

'''

# Create the list with the variables
num_list = [num1, num2, num3, num4, num5]



# Print list
print(num_list)

# Using functions with list
print(f"Lowest Grade: {min(num_list)} !!")
print(f"Highest Grade: {max(num_list)} !!")
print(f"Sum of Grades: {sum(num_list)} !!")
print(f"Average: {sum(num_list)/len(num_list)} !!")

print("---------------------------------------")

# Branching to determine the letter grade
letter_grade = ""
avg = sum(num_list)/len(num_list)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else: # letter_grade less than 60
    letter_grade = "F"

print()
print(f"Your grade is: {letter_grade}")

