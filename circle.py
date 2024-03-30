import turtle as t
import random as r
tim=t.Turtle()
screen=t.Screen()
def sporange(gap):
    number=int(360/gap)
    for i in range(number):
        tim.circle(100)
        tim.setheading(tim.heading()+10)

sporange(10)









screen.exitonclick()