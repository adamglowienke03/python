from turtle import Turtle, Screen
import time
import random

delay = 0.1
step = 20

score = 0

screen = Screen()
screen.title("Snake")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

head = Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = []

food = Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 16, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# ruch głowy
def move():
    x = head.xcor()
    y = head.ycor()
    if head.direction == "up":
        head.sety(y + step)
    if head.direction == "down":
        head.sety(y - step)
    if head.direction == "left":
        head.setx(x - step)
    if head.direction == "right":
        head.setx(x + step)

def update_score():
    pen.clear()
    pen.write(f"Score: {score}", align="center", font=("Courier", 16, "normal"))
    
while True:
    screen.update()

    if head.distance(food) < 20:
        x = random.randint(-14, 14) * step
        y = random.randint(-14, 14) * step
        food.goto(x, y)

        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        update_score()

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        print("Game over!")
        break

    for segment in segments:
        if head.distance(segment) < 20:
            print("Game over!")
            screen.bye()
            quit()

    time.sleep(delay)

screen.mainloop()
