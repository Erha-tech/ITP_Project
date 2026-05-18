import tkinter as tk
from data_manager import load_high_score, save_high_score
from game_entities import Player, Enemy, Stars

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Survival")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=400, height=500, bg="#05050F")
        self.canvas.pack()

        self.state = "START"
        self.high_score = load_high_score()
        self.score = 0
        self.player = None
        self.enemies = []
        self.stars = None
        self.enemy_speed = 4
        self.spawn_rate = 1200

        self.root.bind("<Left>", lambda e: self.handle_left())
        self.root.bind("<Right>", lambda e: self.handle_right())
        self.root.bind("<space>", lambda e: self.handle_space())

        self.draw_start_menu()

    def handle_left(self):
        if self.state == "PLAYING" and self.player:
            self.player.move_left()

    def handle_right(self):
        if self.state == "PLAYING" and self.player:
            self.player.move_right()

    def handle_space(self):
        if self.state in ["START", "GAME_OVER"]:
            self.start_game()

    def clear_canvas(self):
        self.canvas.delete("all")
        self.enemies.clear()
        if self.stars:
            self.stars = None

    def draw_start_menu(self):
        self.state = "START"
        self.clear_canvas()
        self.stars = Stars(self.canvas, 60)

        self.canvas.create_text(
            200, 130,
            text="✦ SPACE SURVIVAL ✦",
            fill="#66AAFF",
            font=("Courier", 18, "bold")
        )

        self.canvas.create_text(
            200, 175,
            text="Уклоняйся от астероидов!",
            fill="#8899BB",
            font=("Courier", 11)
        )

        self.canvas.create_text(
            200, 360,
            text="[ ПРОБЕЛ — СТАРТ ]",
            fill="#00FF88",
            font=("Courier", 13, "bold")
        )

        self.canvas.create_text(
            200, 410,
            text=f"Рекорд: {self.high_score}",
            fill="#FFD700",
            font=("Courier", 12)
        )

        self._menu_star_loop()

    def _menu_star_loop(self):
        if self.state == "START" and self.stars:
            self.stars.update()
            self.root.after(40, self._menu_star_loop)

    def start_game(self):
        self.state = "PLAYING"
        self.score = 0
        self.enemy_speed = 4
        self.spawn_rate = 1200

        self.clear_canvas()

        self.stars = Stars(self.canvas, 80)
        self.player = Player(self.canvas, 178, 410)

        self.score_text = self.canvas.create_text(
            10, 12,
            anchor="w",
            text="Score: 0",
            fill="#AACCFF",
            font=("Courier", 12, "bold")
        )

        self.spawn_enemy()
        self.game_loop()

    def game_over(self):
        self.state = "GAME_OVER"

        if self.score > self.high_score:
            self.high_score = self.score
            save_high_score(self.high_score)

        self.clear_canvas()

        self.stars = Stars(self.canvas, 60)

        self.canvas.create_text(
            200, 140,
            text="— GAME OVER —",
            fill="#FF4444",
            font=("Courier", 22, "bold")
        )

        self.canvas.create_text(
            200, 240,
            text=f"Счёт: {self.score}",
            fill="#FFFFFF",
            font=("Courier", 16)
        )

        self.canvas.create_text(
            200, 370,
            text="[ ПРОБЕЛ — ЗАНОВО ]",
            fill="#00FF88",
            font=("Courier", 13, "bold")
        )

        self._menu_star_loop()

    def spawn_enemy(self):
        if self.state == "PLAYING":
            enemy = Enemy(self.canvas, self.enemy_speed)
            self.enemies.append(enemy)

            self.score += 10

            self.canvas.itemconfig(
                self.score_text,
                text=f"Score: {self.score}"
            )

            if self.score % 150 == 0:
                self.enemy_speed = min(self.enemy_speed + 1, 14)
                self.spawn_rate = max(self.spawn_rate - 80, 400)

            self.root.after(self.spawn_rate, self.spawn_enemy)

    def check_collisions(self):
        if not self.player:
            return False

        px1 = self.player.x + 4
        py1 = self.player.y + 4
        px2 = self.player.x + self.player.width - 4
        py2 = self.player.y + self.player.height - 4

        for enemy in self.enemies:
            ex1, ey1 = enemy.x, enemy.y
            ex2 = ex1 + enemy.width
            ey2 = ey1 + enemy.height

            if px1 < ex2 and px2 > ex1 and py1 < ey2 and py2 > ey1:
                return True

        return False

    def game_loop(self):
        if self.state == "PLAYING":

            if self.stars:
                self.stars.update()

            if self.player:
                self.player.animate_flame()

            for enemy in self.enemies:
                enemy.update()

            self.enemies = [e for e in self.enemies if e.y < 520]

            if self.check_collisions():
                self.game_over()
            else:
                self.root.after(30, self.game_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
