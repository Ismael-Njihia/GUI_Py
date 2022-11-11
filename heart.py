import turtle

pen = turtle.Turtle()

#method for the curve
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
#methode for full heart
def heart():
    pen.fillcolor('red')
    #fill the color
    pen.begin_fill()

    #for the left line
    pen.left(140)
    pen.forward(113)

    #for the left curve
    curve()
    pen.left(120)

    #right curve
    curve()

    #draw the right line
    pen.forward(112)

    #at the end fill the color
    pen.end_fill()

#method to write text
def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('aqua')
    pen.write("Ismael-Njihia", font=("Verdana", 15, "italic"))

#draw the heart
heart()
#write my name
txt()
