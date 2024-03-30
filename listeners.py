import turtle as t
col=["red","green","blue","yellow","brown","violet"]
screen=t.Screen()
screen.setup(width=600,height=600)
l=[-120,-80,-40,0,40,80 ]
screen.listen()
prediction=screen.textinput(title="make ur bet" ,prompt="which turtle will win the race")
print (prediction)
for i in range(0,6):
    timmy=t.Turtle(shape="turtle")
    timmy.penup()
    timmy.color(col[i])
    timmy.goto(x=-250,y=l[i])
    timmy.pendown()

screen.exitonclick()