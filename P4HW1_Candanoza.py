# Nicholas Candanoza
# 11/5/2024
# P6HW1
# Assignment: Collect Scores and Display Results

def get_valid_score():
    """Function to get a valid score between 0 and 100."""
    while True:
        try:
            score = float(input("Enter a score between 0 and 100: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(average):
    """Function to calculate letter grade based on the average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Ask user how many scores they want to enter
num_scores = int(input("How many scores would you like to enter? "))

# Initialize an empty list to store the valid scores
score_list = []

# Loop to collect the scores
for i in range(num_scores):
    print(f"Enter score {i + 1}:")
    score = get_valid_score()  # Get valid score
    score_list.append(score)   # Add valid score to the list

# Find the lowest score
lowest_score = min(score_list)

# Create a modified list of scores by removing the lowest score
modified_score_list = [score for score in score_list if score != lowest_score]

# Calculate the average of the modified score list
average_score = sum(modified_score_list) / len(modified_score_list)

# Determine the letter grade for the average
grade = calculate_grade(average_score)

# Display the results
print("---------Results---------")
print(f"\nLowest Score entered: {lowest_score}")
print(f"Modified List: {modified_score_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade for the average: {grade}")


