import turtle as t

def main():
    t.hideturtle ()
    t.speed(0)
    t.setup(width=700 , height=700)
    t.bgcolor('black')
    p = t.Pen()
    Rectangle (p)
    Square (p)
    Triangle (p)
    Circle (p)
    t.exitonclick()

def Rectangle(p):
    t.pencolor('#e05d1c')
    moveT (-175 , -125)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)


def Square (p):
    t.pencolor('blue')
    moveT(-200 , 200)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)

def Triangle (p):
    t.pencolor('magenta')
    moveT(200 , 200)
    t.forward(50)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(50)

def Circle (p):
    t.pencolor('red')
    moveT(200 , -135)
    t.circle(50)


def moveT (x , y) :
    t.penup()
    t.setpos(x , y)
    t.pendown()

main()
