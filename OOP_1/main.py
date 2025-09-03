from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("green")

# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(180)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(200)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(180)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(180)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(200)
# timmy.right(90)
# timmy.forward(100)
# timmy.hideturtle()



# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Bulbasaur", "Grass/Poison"])
# lub
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Electric", "Fire", "Grass/Poison"])


print(table)

