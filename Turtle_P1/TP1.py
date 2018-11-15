import turtle as t


def main():
    t.hideturtle ()
    t.speed(0)
    t.setup(width=650 , height=650)
    p = t.Pen()
    Line (p)
    Square (p)
    Circle (p)
    Triangle (p)
    t.exitonclick()




def Line(p):
    t.pencolor('cyan')
    moveT (0 , -50)
    t.left(90)
    t.forward(100)

def Square(p):
    t.pencolor('red')
    moveT (0, -100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)

def Circle(p):
    t.pencolor('#ffe063')
    moveT (0, 300)
    t.circle(300)

def Triangle(p):
    t.pencolor('magenta')
    moveT (0, -173.2051)
    t.forward(200)
    t.right(120)
    t.forward(400)
    t.right(120)
    t.forward(400)
    t.right(120)
    t.forward(200)




def moveT (x , y) :
    t.penup()
    t.setpos(x , y)
    t.pendown()

main()
