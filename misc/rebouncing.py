# rebounding ball
from tkinter import *
    
def animation():
    global canvas; global rect
    global dx; global dy
    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))
    x1, y1, x2, y2 = canvas.coords(ball)
    if x2 > width or x1 < 0: 
        dx = - dx
    if y2 > height or y1 < 0:
        dy = - dy
    canvas.move(ball, dx, dy)
    canvas.after(10, animation)

# main program
gui = Tk() 
canvas = Canvas(gui) 
ball = canvas.create_oval(100,100,125,125,fill="red")
canvas.pack()
dx, dy = 1, 1
animation()
mainloop() 