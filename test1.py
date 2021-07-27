import turtle
# We can make one screen only.
screen1 = turtle.Screen()
screen1.bgcolor("white")
turtle.setup(800,600)
screen2 = turtle.Screen()
screen2.bgcolor("cyan")
turtle.setup(800,600)

while True:
    screen1.update()
# while True:
#     screen2.update()
