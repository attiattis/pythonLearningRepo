import turtle

def gotoOrigin(tess):
    # goto origin
    tess.penup()
    tess.goto(0,0)
    tess.pendown()

def draw_rocket():
    wn = turtle.Screen()

    tess = turtle.Turtle()
    radius = 10 # radius of circle
    tess.color("black")
    tess.pensize(2)

    # base
    tess.forward(100)
    # Draw right side
    tess.left(90)
    tess.forward(200)
    curve = 8
    moveLength = 90
    for i in range(curve):  # for curver
        tess.left(i)
        tess.forward(5)
    tess.forward(moveLength)

    # Draw leftside
    gotoOrigin(tess)
    tess.setheading(90)
    tess.forward(200)
    for i in range(curve): # for curver
        tess.right(i)
        tess.forward(5)
    tess.forward(moveLength)
    gotoOrigin(tess)

    # Draw thr circles
    tess.setheading(0)
    tess.forward(60)
    tess.left(90)
    tess.penup()
    tess.forward(160)
    tess.pendown()
    tess.circle(radius) 

    # second circle
    tess.penup()
    tess.forward(50)
    tess.pendown()
    tess.circle(radius)
    

    # Draw the left wing
    gotoOrigin(tess)
    wingLength = 60
    tess.setheading(220)
    tess.forward(wingLength)
    tess.right(150)
    tess.forward(2*wingLength+10)

    # Draw the left wing
    gotoOrigin(tess)
    tess.setheading(0)
    tess.forward(100)
    tess.right(40)
    tess.forward(wingLength)
    tess.left(150)
    tess.forward(2*wingLength+10)

    # Draw the bottom small triangles
   
    for i in [20,50,80]:
        gotoOrigin(tess)
        tess.setheading(0)
        tess.forward(i)
        tess.right(30)
        for i in range(10):
            tess.forward(1)
            tess.right(1)
        tess.setheading(270)
        tess.forward(5)
        tess.right(90)
        tess.forward(20)

        tess.right(90)
        tess.forward(5)
        tess.setheading(50)
        for i in range(10):
            tess.forward(1)
            tess.right(1)
    turtle.done()
draw_rocket()