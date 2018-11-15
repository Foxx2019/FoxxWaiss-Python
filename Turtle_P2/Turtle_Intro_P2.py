import turtle as t


def main () :
    t.setup(width=800 , height=800)
    t.title("Object Made")
    t.bgcolor("#1de047")
    t.hideturtle()
    t.speed(1)
    newInfo ()
    t.exitonclick ()

def newInfo () :
    c = input ('Input a color to draw with - ')
    l = int(input('length of sides - '))
    s = int(input('number of sides - '))
    if s<=2 :
        error()
    object (c , l , s)


def object (c , l , s) :
    t.pencolor(c)
    t.penup()
    b = (l / -2)
    c = (l / 2)
    t.setpos(b , c)
    t.pendown ()
    a = 360 / s
    for x in range(0,s) :
        t.forward(l)
        t. right(a)

def error () :
    p = input('You cant have polygon with 2 or less sides')


main ()
