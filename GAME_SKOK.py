from tkinter import *
import time
import random
import Oleg
from tkinter import messagebox as mb
 
t = Tk()
t.title("Game Skok")
t.resizable(0, 0)
t.wm_attributes("-topmost", 1)
life = 5
c = Canvas(t, width = 800, height = 600, bd = 0, highlightthickness=0)
l = Label(text='Залишилось життів: %s' % life, font="Arial 18", bg = 'lightgreen')
l.pack()
c.pack()
t.update()

def end():
    if len(brick_list) == 0:
        mb.showinfo("Congratulations","You won")
        return 1

brick_list =[]

for i in range(0,800,80):
    for j in range (0,39,13):
        brick_list.append(Oleg.brick(c,'brown',i,j,i+80,j+13))

rack = Oleg.racket(c, "blue")
Ball = Oleg.ball(c, rack, "red")

while 1:
    Ball.draw()
    b_pos = c.coords(Ball.id)
    k = 0
    for x in brick_list:
        if x.hit_Ball(b_pos[0], b_pos[1], b_pos[2], b_pos[3]) == True:
            Ball.x = random.randint(1,5)
            Ball.y = random.randint(1,5)
            c.delete(brick_list.pop(k).id)
        else:
            k = k + 1
    if Ball.bottom == True:
        life = life - 1
        #c.delete('delete')
        #c.create_text(400,50, text = 'lives left = %s' % life, font = ('Times', 17), tag = 'delete')
        l.config(text = 'Залишилось життів: %s' % life )
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
        if end() == 1:
            break
    t.update_idletasks()
    t.update()
    time.sleep(0.01)

        
        
