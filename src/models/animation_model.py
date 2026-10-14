import math


class AnimationModel:
    """Математическая модель движения точки по окружности."""

    def __init__(self):
        """Инициализирует параметры движения."""
        self.center_x = 300
        self.center_y = 300
        self.radius = 200

        self.angle = 0
        self.speed = 0.03

    def update(self):
        """Обновляет угол положения точки."""
        self.angle += self.speed
        self.angle %= 2 * math.pi

    def get_position(self):
        """Возвращает текущие координаты точки."""
        x = self.center_x + self.radius * math.cos(self.angle)
        y = self.center_y + self.radius * math.sin(self.angle)

        return x, y
