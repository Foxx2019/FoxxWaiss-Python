import turtle

def main():
    turtle.hideturtle ()
    turtle.speed(0)
    turtle.setup(width=800 , height=800)
    p = turtle.Pen()
    c = '#268dd6'
    turtle.title("Turtle Graphics")
    p.pencolor(c)
    backGround (p)
    emptyR1 (p)
    fullC (p)
    fullS1 (p)
    drawing5 (p)
    turtle.exitonclick()


def backGround(p):
    turtle.bgcolor("#1de004")
    turtle.pencolor('#268dd6')
    moveT(100, -100)
    turtle.right(90)
    for x in range(0,4):
        turtle.forward(100)
        turtle.left(90)
    moveT (0 , 0)


def emptyR1(p):
    moveT (-100 , -125)
    turtle.pencolor('#e05d1c')
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)


def fullC (p):
    moveT(-200 , 200)
    turtle.pencolor("#ce06ba")
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)


def fullS1(p):
    moveT(100,125)
    turtle.pencolor("#e2df0d")
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)

def drawing5(p):
    moveT (0 , 0)


def moveT (x , y) :
    turtle.penup()
    turtle.setpos(x , y)
    turtle.pendown()

main()
