from turtle import Turtle,Screen
timmy=Turtle()
my_screen=Screen()

def square():
    timmy.forward(100)
    timmy.right(90)


timmy.shape("turtle")
for i in range(4):
    square()

#timmy.forward(100)
timmy.left(90)
timmy.dot(20,"green")
timmy.forward(50)
for i in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)





my_screen.exitonclick()