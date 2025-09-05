from turtle import Turtle, Screen

tim = Turtle()
tim.shape("classic")
tim.color("black")
tim.pensize(2)

def forwards():
    tim.forward(5)

def backwards():
    tim.backward(5)

def counter_clockwise():
    tim.left(5)

def clockwise():
    tim.right(5)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.title("Etch-A-Sketch")
screen.listen()

screen.onkeypress(forwards, "w")
screen.onkeypress(backwards, "s")
screen.onkeypress(counter_clockwise, "a")
screen.onkeypress(clockwise, "d")
screen.onkeypress(clear, "c")

screen.mainloop()
