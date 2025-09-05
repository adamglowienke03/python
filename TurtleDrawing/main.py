from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#     tim.backward(100)

# dotted line
# for _ in range(50):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()
#     tim.right(10)

# triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# for i in range(3,11):
#     tim.pencolor(random.random(), random.random(), random.random())
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(360/i)

screen = Screen()
screen.exitonclick()
