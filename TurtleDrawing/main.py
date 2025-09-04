from turtle import Turtle, Screen
import prettytable

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#     tim.backward(100)

for _ in range(50):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()
    tim.right(10)

screen = Screen()
screen.exitonclick()
