import math
import unittest

from src.models.animation_model import AnimationModel


class TestAnimationModel(unittest.TestCase):
    """Тестирование математической модели анимации."""

    def setUp(self):
        """Создаёт модель перед каждым тестом."""
        self.model = AnimationModel()

    def test_initial_position(self):
        """Проверяет начальное положение точки."""
        x, y = self.model.get_position()

        self.assertAlmostEqual(x, 500)
        self.assertAlmostEqual(y, 300)

    def test_circle_radius(self):
        """Проверяет расстояние точки от центра окружности."""
        self.model.angle = 1.5

        x, y = self.model.get_position()

        distance = math.sqrt(
            (x - 300) ** 2 + (y - 300) ** 2
        )

        self.assertAlmostEqual(distance, 200)

    def test_angle_update(self):
        """Проверяет изменение угла при движении."""
        initial_angle = self.model.angle

        self.model.update()

        self.assertGreater(self.model.angle, initial_angle)

    def test_pause(self):
        """Проверяет остановку анимации."""
        self.model.toggle_pause()

        initial_angle = self.model.angle

        self.model.update()

        self.assertEqual(self.model.angle, initial_angle)

    def test_reverse_direction(self):
        """Проверяет изменение направления движения."""
        initial_speed = self.model.speed

        self.model.reverse_direction()

        self.assertEqual(self.model.speed, -initial_speed)

    def test_speed_limits(self):
        """Проверяет ограничения скорости движения."""
        self.model.change_speed(10)

        self.assertAlmostEqual(abs(self.model.speed), 0.20)

        self.model.change_speed(-10)

        self.assertAlmostEqual(abs(self.model.speed), 0.01)


if __name__ == "__main__":
    unittest.main()
