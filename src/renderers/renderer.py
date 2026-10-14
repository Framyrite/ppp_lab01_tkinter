import tkinter as tk


class CircleRenderer:
    """Отвечает за отрисовку окружности и точки."""

    def __init__(self, canvas: tk.Canvas):
        """Инициализирует параметры отрисовки."""
        self.canvas = canvas

        self.center_x = 300
        self.center_y = 300
        self.radius = 200
        self.point_radius = 7

    def draw(self):
        """Рисует окружность и точку на ней."""

        x = self.center_x
        y = self.center_y
        r = self.radius

        # Рисуем окружность
        self.canvas.create_oval(
            x - r,
            y - r,
            x + r,
            y + r,
            outline="black",
            width=2
        )

        # Рисуем точку справа на окружности
        self.point = self.canvas.create_oval(
            x + r - self.point_radius,
            y - self.point_radius,
            x + r + self.point_radius,
            y + self.point_radius,
            fill="red",
            outline="red"
        )
    def move_point(self, x, y):
        """Перемещает точку в заданные координаты."""
        r = self.point_radius

        self.canvas.coords(
            self.point,
            x - r,
            y - r,
            x + r,
            y + r
        )
