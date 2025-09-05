from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
turtles = []
colors = ["blue", "red", "green", "yellow", "pink", "orange"]
y = [100, 70, 40, 10, -20, -50]

def create_turtles():
    for i in range(0, 6):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-230, y[i])
        turtles.append(new_turtle)
create_turtles()

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the")

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You win! The {winner} turtle is the winner!")
            else:
                print(f"You lose! The {winner} turtle is the winner!")

screen.exitonclick()