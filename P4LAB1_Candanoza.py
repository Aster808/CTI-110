# Nicholas Candanoza
# P4LAB1
# 10/29/2024
# Use loops and turtle library to draw a house

# Import turtle library
import turtle

# set up the window and turtle object
window = turtle.Screen()
tom = turtle.Turtle()

# change features of turtle
tom.pensize(10)
tom.pencolor("green")
tom.shape("arrow")

# While loop that runs 4 times
movement = 0

while movement <= 3:
    movement += 1
    tom.forward(150)
    tom.right(90)
    

# For loop to run 3 times
for side in range(3):
    tom.forward(150)
    tom.left(120)
    
