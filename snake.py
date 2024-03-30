from turtle import Turtle,Screen
screen=Screen()
size=[0,-20,-40]
screen.setup(width=600,height=600)
screen.bgcolor("pink")
screen.title("Snake Game")
for i in range(0,3):
    timmy=Turtle(shape="square")
    timmy.goto(x=size[i],y=0)

    screen.exitonclick()