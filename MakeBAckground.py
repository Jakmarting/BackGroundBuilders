import turtle
import random

sizex=1960
sizey=920

window = turtle.Screen()
window.screensize(sizex, sizey)
window.setup(width=1.0, height=1.0, startx=None, starty=None)

colors = ["Green","Lime","Lightgreen","White"]

color_palette2 = ["Lime","Blue","Red","Orange","White","Pink","Yellow","Purple"]


turtle.Turtle(visible=False)
turtle.bgcolor("Black")
turtle.pencolor("Lime")
turtle.visible = False

def reset(x,y,h):
    # turtle.setheading(h)
    ChooseAngle()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def ChooseAngle():
    turtle.setheading(random.randint(0,360))

def DoLine():
    turtle.pendown()
    turtle.fd(random.randint(1,4)*40)
    turtle.left(random.randint(-10,10))
    turtle.penup()

def node(depth,lvl):
    (x,y) = turtle.pos()
    h = turtle.heading()

    while depth > 0:
        while ((-sizex/2 < turtle.pos()[0] < sizex/2) and (-sizey/2 < turtle.pos()[1] < sizey/2)):
            DoLine()
            """
            if (random.randint(0,lvl*100) == 0):
                print(lvl)
                lvl += 1
                if (lvl > len(colors)):
                    return
                node(random.randint(0,2), lvl)
            """
        reset(x,y,h)
        depth -= 1
    #turtle.pencolor(colors[lvl])
"""
turtle.pencolor(colors[0])
node(100, 1)
turtle.pencolor(colors[1])
node(70, 1)
turtle.pencolor(colors[2])
node(30, 1)
turtle.pencolor(colors[3])
node(10,1)
"""
for c in color_palette2:
    node(5,1)
    turtle.pencolor(c)

turtle.pencolor = "Black"
turtle.penup()
turtle.goto(1000,1000)
