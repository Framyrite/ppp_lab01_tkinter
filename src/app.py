"""Модуль графического интерфейса и управления анимацией."""

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

        # Создаём объект отрисовки
        self.renderer = CircleRenderer(self.canvas)
        self.renderer.draw()

        # Подключаем управление с клавиатуры
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("<Right>", self.increase_speed)
        self.root.bind("<Left>", self.decrease_speed)
        self.root.bind("<r>", self.reverse_direction)

        self.update_title()

    def update_title(self):
        """Обновляет заголовок окна с информацией об анимации."""
        speed = abs(self.model.speed)

        if self.model.paused:
            status = "Пауза"
        else:
            status = "Движение"

        self.root.title(
            f"Лабораторная №1 | Скорость: {speed:.2f} | {status}"
        )

    def toggle_pause(self, event):
        """Останавливает или возобновляет анимацию."""
        self.model.toggle_pause()
        self.update_title()

    def increase_speed(self, event):
        """Увеличивает скорость движения."""
        self.model.change_speed(0.01)
        self.update_title()

    def decrease_speed(self, event):
        """Уменьшает скорость движения."""
        self.model.change_speed(-0.01)
        self.update_title()

    def reverse_direction(self, event):
        """Изменяет направление движения точки."""
        self.model.reverse_direction()
        self.update_title()

    def animate(self):
        """Обновляет положение точки и запускает следующий кадр."""
        self.model.update()

        x, y = self.model.get_position()

        self.renderer.move_point(x, y)

        self.root.after(16, self.animate)

    def run(self):
        """Запускает приложение."""
        self.animate()
        self.root.mainloop()
