import tkinter as tk

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Survival - Скелет")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=400, height=500, bg="#05050F")
        self.canvas.pack()

        self.canvas.create_text(
            200,
            250,
            text="Окно создано. Ожидание модулей...",
            fill="white",
            font=("Courier", 12)
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
