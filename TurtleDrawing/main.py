from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def main():
    screen = Screen()
    screen.colormode(255)

    turtle = Turtle()
    turtle.speed("fastest")

    for _ in range(36):
        turtle.color(random_color())
        draw_square(turtle)
        turtle.right(10)

    screen.exitonclick()

if __name__ == "__main__":
    main()