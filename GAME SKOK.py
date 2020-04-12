from tkinter import *
import time
import random

t = Tk()
t.title("Game Skok")
t.resizable(0, 0)
t.wm_attributes("-topmost", 1)
c = Canvas(t, width = 800, height = 600, bd = 0, highlightthickness=0)
c.pack()
t.update()

class ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10, 25, 25, fill= color)
        self.canvas.move(self.id, 400, 300)
        starts = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.shuffle(starts)
        self.x = starts[0]
        random.shuffle(starts)
        self.y = starts[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width() 
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            #self.y = -1 * self.y
            self.y = random.randint(1, 5)
        if pos [3] >= self.canvas_height:
            #self.y = -1 * self.y
            self.y = random.randint(-5, -1)
        if pos [0] <= 0:
            #self.x = -1 * self.x
            self.x = random.randint(1, 5)
        if pos [2] >= self.canvas_width:
            #self.x = -1 * self.x
            self.x = random.randint(-5, -1)
        
b = ball(c, "red")

while 1:
    b.draw()
    t.update_idletasks()
    t.update()
    time.sleep(0.01)
