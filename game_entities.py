import random 
import math 
 
class GameObject: 
    def __init__(self): 
        self.x = 0 
        self.y = 0 
        self.width = 40 
        self.height = 40 
        self.parts = [] 
 
    def move(self, dx, dy): 
        for part in self.parts: 
            try: self.canvas.move(part, dx, dy) 
            except: pass 
        self.x += dx 
        self.y += dy 
 
    def delete(self): 
        for part in self.parts: 
            try: self.canvas.delete(part) 
            except: pass 
 
class Player(GameObject): 
    def __init__(self, canvas, x, y): 
        super().__init__() 
        self.canvas = canvas 
        self.x = x 
        self.y = y 
        self.width = 44 
        self.height = 48 
        self.speed = 25 
        self._draw() 
 
    def _draw(self): 
        x, y = self.x, self.y 
        body = self.canvas.create_polygon(x + 22, y, x + 40, y + 44, x + 4,  y + 44, fill="#2255AA", outline="#66AAFF", width=2) 
        flame1 = self.canvas.create_polygon(x + 18, y + 50, x + 22, y + 62, x + 26, y + 50, fill="#FF6600") 
        self.parts = [body, flame1] 
        self.flame_parts = [flame1] 
        self.flame_state = True 
        self.flame_tick = 0 
 
    def animate_flame(self): 
        self.flame_tick += 1 
        if self.flame_tick % 4 == 0: 
            self.flame_state = not self.flame_state 
            self.canvas.itemconfig(self.flame_parts[0], fill="#FF6600" if self.flame_state else "#FF9900") 
 
    def move_left(self): 
        if self.x > -10: self.move(-self.speed, 0) 
 
    def move_right(self): 
        if self.x < 356: self.move(self.speed, 0) 
 
class Enemy(GameObject): 
    def __init__(self, canvas, speed): 
        super().__init__() 
        self.canvas = canvas 
        self.x = random.randint(10, 350) 
        self.y = -50 
        self.speed = speed 
        self._draw() 
 
    def _draw(self): 
        rock = self.canvas.create_rectangle(self.x, self.y, self.x+40, self.y+40, fill="#7A6548") 
        self.parts = [rock] 
 
    def update(self): 
        self.move(0, self.speed) 
 
class Stars: 
    def __init__(self, canvas, count=60): 
        self.canvas = canvas 
        self.stars = [] 
        for _ in range(count): 
            x, y = random.randint(0, 400), random.randint(0, 500) 
            sid = canvas.create_oval(x, y, x+2, y+2, fill="#FFFFFF", outline="") 
            self.stars.append({"id": sid, "x": x, "y": y, "speed": random.uniform(0.5, 1.5)}) 
 
    def update(self): 
        for s in self.stars: 
            s["y"] += s["speed"] 
            if s["y"] > 500: s["y"] = 0 
            self.canvas.coords(s["id"], s["x"], s["y"], s["x"]+2, s["y"]+2) 
