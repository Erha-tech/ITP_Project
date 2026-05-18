import random 
import math 
 
class GameObject: 
    """Базовый класс для всех объектов игры (Инкапсуляция координат).""" 
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
 
    def update(self): 
        pass 
 
class Player(GameObject): 
    """Корабль игрока — высокодетализированный векторный объект.""" 
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
        wing_l = self.canvas.create_polygon(x + 2, y + 28, x - 10, y + 48, x + 16, y + 40, fill="#1A3A6E", outline="#4488CC") 
        wing_r = self.canvas.create_polygon(x + 42, y + 28, x + 54, y + 48, x + 28, y + 40, fill="#1A3A6E", outline="#4488CC") 
        body = self.canvas.create_polygon(x + 22, y, x + 40, y + 44, x + 4,  y + 44, fill="#2255AA", outline="#66AAFF", width=2) 
        cockpit = self.canvas.create_polygon(x + 22, y + 8, x + 32, y + 28, x + 12, y + 28, fill="#0D1F44", outline="#3366BB") 
        stripe = self.canvas.create_line(x + 22, y + 8, x + 22, y + 44, fill="#4499FF") 
        nozzle = self.canvas.create_rectangle(x + 15, y + 42, x + 29, y + 50, fill="#333355", outline="#6666AA") 
        flame1 = self.canvas.create_polygon(x + 18, y + 50, x + 22, y + 62, x + 26, y + 50, fill="#FF6600") 
        flame2 = self.canvas.create_polygon(x + 16, y + 50, x + 19, y + 58, x + 22, y + 50, fill="#FF9900") 
        flame3 = self.canvas.create_polygon(x + 22, y + 50, x + 25, y + 58, x + 28, y + 50, fill="#FF9900") 
 
        self.parts = [wing_l, wing_r, body, cockpit, stripe, nozzle, flame1, flame2, flame3] 
        self.flame_parts = [flame1, flame2, flame3] 
        self.flame_state = True 
        self.flame_tick = 0 
 
    def animate_flame(self): 
        self.flame_tick += 1 
        if self.flame_tick % 4 == 0: 
            self.flame_state = not self.flame_state 
            color1 = "#FF6600" if self.flame_state else "#FF9900" 
            color2 = "#FFAA00" if self.flame_state else "#FF6600" 
            self.canvas.itemconfig(self.flame_parts[0], fill=color1) 
            self.canvas.itemconfig(self.flame_parts[1], fill=color2) 
            self.canvas.itemconfig(self.flame_parts[2], fill=color2) 
 
    def move_left(self): 
        if self.x > -10: self.move(-self.speed, 0) 
 
    def move_right(self): 
        if self.x < 356: self.move(self.speed, 0) 
 
class Enemy(GameObject): 
    """Астероид — процедурно генерируемый многоугольник (Полиморфизм).""" 
    def __init__(self, canvas, speed): 
        super().__init__() 
        self.canvas = canvas 
        self.x = random.randint(10, 350) 
        self.y = -50 
        self.speed = speed 
        self._draw() 
 
    def _draw(self): 
        cx, cy = self.x + 20, self.y + 20 
        num_points = random.randint(7, 10) 
        pts = [] 
        for i in range(num_points): 
            angle = (360 / num_points) * i + random.uniform(-10, 10) 
            r = random.randint(14, 22) 
            pts += [cx + r * math.cos(math.radians(angle)), cy + r * math.sin(math.radians(angle))] 
 
        color = random.choice(["#7A6548", "#8B7355", "#9C8464", "#6B5840"]) 
        rock = self.canvas.create_polygon(pts, fill=color, outline="#4A3828") 
        crater1 = self.canvas.create_oval(cx - 8, cy - 6, cx - 2, cy, fill="#4A3828") 
        crater2 = self.canvas.create_oval(cx + 2, cy + 4, cx + 8, cy + 9, fill="#4A3828") 
 
        self.parts = [rock, crater1, crater2] 
 
    def update(self): 
        self.move(0, self.speed) 
 
class Stars: 
    """Система динамического фона космического пространства (Эффект Параллакса).""" 
    def __init__(self, canvas, count=80): 
        self.canvas = canvas 
        self.stars = [] 
        for _ in range(count): 
            x, y = random.randint(0, 400), random.randint(0, 500) 
            size = random.choice([1, 1, 1, 2]) 
            brightness = random.choice(["#FFFFFF", "#CCCCCC", "#AAAAAA", "#888888"]) 
            speed = random.uniform(0.3, 1.2) 
            sid = canvas.create_oval(x, y, x + size, y + size, fill=brightness, outline="") 
            self.stars.append({"id": sid, "x": x, "y": y, "speed": speed, "size": size}) 
 
    def update(self): 
        for s in self.stars: 
            s["y"] += s["speed"] 
            if s["y"] > 500: 
                s["y"] = 0 
                s["x"] = random.randint(0, 400) 
            self.canvas.coords(s["id"], s["x"], s["y"], s["x"] + s["size"], s["y"] + s["size"]) 
