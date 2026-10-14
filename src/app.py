import tkinter as tk

from src.models.animation_model import AnimationModel
from src.renderers.renderer import CircleRenderer


class App:
    """Графическое приложение для анимации точки."""

    def __init__(self):
        """Создаёт главное окно и компоненты приложения."""

        self.root = tk.Tk()

        self.root.title("Лабораторная работа №1")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        # Создаём область рисования
        self.canvas = tk.Canvas(
            self.root,
            width=600,
            height=600,
            bg="white",
            highlightthickness=0
        )

        self.canvas.pack(fill="both", expand=True)

        # Создаём математическую модель
        self.model = AnimationModel()

        # Создаём объект для отрисовки
        self.renderer = CircleRenderer(self.canvas)

        # Рисуем окружность и точку
        self.renderer.draw()

    def animate(self):
        """Обновляет положение точки и запускает следующий кадр."""

        # Обновляем положение точки
        self.model.update()

        # Получаем новые координаты
        x, y = self.model.get_position()

        # Перемещаем точку
        self.renderer.move_point(x, y)

        # Запускаем следующий кадр через 16 миллисекунд
        self.root.after(16, self.animate)

    def run(self):
        """Запускает приложение и анимацию."""

        self.animate()
        self.root.mainloop()
