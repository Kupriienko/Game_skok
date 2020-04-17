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
    for j in range (0,52,13):
        brick_list.append(Oleg.brick(c,'brown',i,j,i+80,j+13))
        
length = random.randint(0,len(brick_list))
c.itemconfig(brick_list[length].id, fill='black')
brick_list[length].color='black'

yell = random.randint(0,len(brick_list))
c.itemconfig(brick_list[yell].id, fill='yellow')
brick_list[yell].color='yellow'

rack = Oleg.racket(c, "blue")
Ball = Oleg.ball(c, rack, "red")
rack_length = False
Super_Power = False
h = time.time()
while 1: 
    Ball.draw()
    b_pos = c.coords(Ball.id)
    
    if Super_Power and time.time() - h > 5.00:
        Super_Power = False
        c.delete('delete')
        c.itemconfig(rack.id, c.create_rectangle(-20,-4, 120, 10, fill= 'black'))
    elif Super_Power and time.time() - h < 5.00:
        c.delete('delete')
        c.create_text(400,580, text = 'You got sure powerit will end in ' +str(round(5.00 - (time.time() - h),2)) + 'seconds', font = ('Times', 17), tag = 'delete')

    if rack_length and time.time() - h > 10.00:
        rack_length = False
        c.coords(rack.id, 20, -4, 120, 10)
        c.move(rack.id, 380, 550)
        c.itemconfig(rack.id, fill='blue')
        c.delete('delete')
    elif rack_length and time.time() - h < 10.00:
        c.delete('delete')
        c.create_text(400,580, text = 'You got sure powerit will end in ' +str(round(10.00 - (time.time() - h),2)) + 'seconds', font = ('Times', 17), tag = 'delete')
        
    for x in brick_list:
        if x.hit_Ball(b_pos[0], b_pos[1], b_pos[2], b_pos[3]) == True:
            c.delete(brick_list.pop(brick_list.index(x)).id)
            if x.color=='black':
                h = time.time()
                c.create_text(400,580, text = 'The length of racket has increased, it will end in' +str(round(10.00 - (time.time() - h),2)) + 'seconds' , font = ('Times', 17), tag = 'delete')
                c.coords(rack.id, 20, -4, 220, 10)
                c.move(rack.id, 380, 550)
                c.itemconfig(rack.id, fill='black')
                rack_length = True
            if x.color=='yellow':
                h = time.time()
                c.create_text(400,580, text = 'You got sure powerit will end in ' +str(round(5.00 - (time.time() - h),2)) + 'seconds' , font = ('Times', 17), tag = 'delete')
                c.itemconfig(Ball.id, fill='yellow')
                Super_Power = True
            if not Super_Power:
                Ball.x = random.randint(1,5)
                Ball.y = random.randint(1,5)
                
    if Ball.bottom == True:
        life = life - 1
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

        
        
