# from turtle import Turtle, Screen
# new_turtle = Turtle()
# print(new_turtle)
#
# new_turtle.color("red")
# new_turtle.shape("turtle")
# new_turtle.forward(100)
# new_turtle.left(90)
# new_turtle.forward(100)
# new_turtle.left(90)
# new_turtle.forward(100)
# new_turtle.left(90)
# new_turtle.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["Alice", "Bob", "Charlie"])
table.add_column("Age", [25, 30, 22])
table.add_column("Country", ["USA", "Germany", "UK"])
table.align = "l"

print(table)