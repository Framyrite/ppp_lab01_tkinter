import tkinter as tk


class App:
    """Графическое приложение для анимации точки."""

    def __init__(self):
        """Создаёт главное окно и область рисования."""
        self.root = tk.Tk()

        self.root.title("Лабораторная работа №1")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=600,
            height=600,
            bg="white",
            highlightthickness=0
        )

        self.canvas.pack(fill="both", expand=True)

    def run(self):
        """Запускает главный цикл приложения."""
        self.root.mainloop()
