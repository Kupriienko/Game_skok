from tkinter import *
import time
import random
import Oleg
from tkinter import messagebox as mb
 
t = Tk()
t.title("Game Skok")
t.resizable(0, 0)
t.wm_attributes("-topmost", 1)
c = Canvas(t, width = 800, height = 600, bd = 0, highlightthickness=0)
c.pack()
t.update()


rack = Oleg.racket(c, "blue")
Ball = Oleg.ball(c, rack, "red")
life = 5
c.create_text(400,20, text = 'lives left = %s' % life, font = ('Times', 18), tag = 'delete')
h = time.time()
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

        
        
