from tkinter import *
import time
import random
from tkinter import messagebox as mb

class ball:
    def __init__(self, canvas, rack, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10, 25, 25, fill= color)
        self.canvas.move(self.id, 400, 300)
        self.rack = rack
        self.x = random.randint(-7,-1)
        self.y = random.randint(-7,-1)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.bottom = False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if self.hit_rack(pos) == True:
            self.y = -3
        if pos[1] <= 0:
            self.y = random.randint(1, 5)
        if pos [3] >= self.canvas_height:
            self.bottom = True
        if pos [0] <= 0:
            self.x = random.randint(1, 5)
        if pos [2] >= self.canvas_width:
            self.x = random.randint(-5, -1)
    def hit_rack(self, pos):
        rack_pos = self.canvas.coords(self.rack.id)
        if pos [0] <= rack_pos[2] and pos [2] >= rack_pos[0]:
            if pos [3] >= rack_pos[1] and pos [1] <= rack_pos[3]:
                return True
        return False

class racket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(-20,-4, 120, 10, fill= color)
        self.canvas.move(self.id, 380, 550)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>', self.right)
        self.canvas.bind_all('<KeyPress-Left>', self.left)
    def draw(self, direction):
        pos = self.canvas.coords(self.id)
        if pos [0] <= 0 and direction == 'left':
            self.x = 0
        elif pos [2]>= self.canvas_width and direction == 'right':
            self.x = 0
        self.canvas.move(self.id, self.x, 0)
        
    def right(self, evt):
        self.x = 10
        self.draw('right')

    def left(self, evt):
        self.x = -10
        self.draw('left')
 
t = Tk()
t.title("Game Skok")
t.resizable(0, 0)
t.wm_attributes("-topmost", 1)
c = Canvas(t, width = 800, height = 600, bd = 0, highlightthickness=0)
c.pack()
t.update()    

rack = racket(c, "blue")
Ball = ball(c, rack, "red")
life = 5
c.create_text(400,20, text = 'lives left = %s' % life, font = ('Times', 18), tag = 'delete')
while 1:
    Ball.draw()
    if Ball.bottom == True:
        life = life - 1
        c.delete('delete')
        c.create_text(400,20, text = 'lives left = %s' % life, font = ('Times', 18), tag = 'delete')
        
        if life >= 1:
            mb.showinfo("The ball is fall down","Try Again")
        else:
            mb.showinfo("Oh, no!","you lost")
            break
        
        Ball.bottom = False
        c.coords(Ball.id,10,10, 25, 25)
        c.move(Ball.id, 400, 300)
        Ball.x = random.randint(-5,-1)
        Ball.y = random.randint(-5,-1)
    t.update_idletasks()
    t.update()
    time.sleep(0.01)

        
        
