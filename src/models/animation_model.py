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
        self.paused = False

    def update(self):
        """Обновляет положение точки, если анимация не остановлена."""
        if not self.paused:
            self.angle += self.speed
            self.angle %= 2 * math.pi

    def get_position(self):
        """Возвращает текущие координаты точки."""
        x = self.center_x + self.radius * math.cos(self.angle)
        y = self.center_y + self.radius * math.sin(self.angle)

        return x, y

    def change_speed(self, delta):
        """Изменяет скорость, сохраняя направление движения."""
        direction = 1 if self.speed > 0 else -1

        new_speed = abs(self.speed) + delta

        # Ограничиваем скорость допустимыми значениями
        new_speed = max(0.01, min(0.20, new_speed))

        self.speed = direction * round(new_speed, 2)

    def reverse_direction(self):
        """Меняет направление движения точки."""
        self.speed = -self.speed

    def toggle_pause(self):
        """Приостанавливает или возобновляет анимацию."""
        self.paused = not self.paused
