from tkinter import *
from ball import Ball

master= Tk()
canvas = Canvas(master, width=800, height=800)
canvas.pack()

canvas.create_rectangle(0, 0, 400, 400, fill = "#ffffff")
ball = Ball((200, 250), (2, 2), 20)

while True:
    ball.move()
    bbox = ball.get_bbox()
    canvas.create_rectangle(0, 0, 400, 400, fill = "#ffffff")
    canvas.create_oval(bbox[0], bbox[1], bbox[2], bbox[3], fill = "#000000")
    canvas.after(1000//60)
    canvas.update()

mainloop()
