import random

class ball:
    def __init__(self, canvas, rack, bot_rack, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10, 25, 25, fill= color)
        self.canvas.move(self.id, 400, 300)
        self.rack = rack
        self.bot_rack = bot_rack
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
        if self.hit_RackBot(pos) == True:
            self.y = -3
        if pos[1] <= 0:
            self.y = random.randint(1, 5)
        if pos [3] >= self.canvas_height:
            self.bottom = True
        if pos [0] <= 0:
            self.x = random.randint(1, 5)
        if pos [2] >= self.canvas_width:
            self.x = random.randint(-5, -1)
            return False
    def hit_rack(self, pos):
        rack_pos = self.canvas.coords(self.rack.id)
        if pos [0] <= rack_pos[2] and pos [2] >= rack_pos[0]:
            if pos [3] >= rack_pos[1] and pos [1] <= rack_pos[3]:
                return True
        return False
    def hit_RackBot(self, pos):
        RackBot_pos = self.canvas.coords(self.bot_rack.id)
        if pos [0] <= RackBot_pos[2] and pos [2] >= RackBot_pos[0]:
            if pos [3] >= RackBot_pos[1] and pos [1] <= RackBot_pos[3]:
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
        self.x = 20
        self.draw('right')

    def left(self, evt):
        self.x = -20
        self.draw('left')
        
class bot_racket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 11, 120, 19, fill= color)
        self.canvas.move(self.id, 380, 555)
        starts = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        random.shuffle(starts)
        self.x = starts[0]
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos [0] <= 0:
            self.x = random.randint(3, 5)
        elif pos [2]>= self.canvas_width:
            self.x = random.randint(-5, -3)

class brick:
    def __init__(self, canvas, color,x1,y1,x2,y2):
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_rectangle(x1,y1, x2, y2, fill= color, outline = 'black', width = 2)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas_width = self.canvas.winfo_width()
    def hit_Ball(self, bx1, by1, bx2, by2):
        if bx1 >= self.x1 and bx1 <= self.x2 and by1 <= self.y2 and by1 >= self.y1:
            return True
        else:
            return False

