import math
import unittest


class GeometryCalculator:
    # Вычисляет площадь круга по радиусу
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    # Вычисляет площадь треугольника по формуле Герона
    @staticmethod
    def triangle_area(a, b, c):
        # Полупериметр треугольника
        s = (a + b + c) / 2
        # Формула Герона для вычисления площади треугольника
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    # Проверяет треугольник на прямоугольность по теореме Пифагора
    @staticmethod
    def is_right_triangle(a, b, c):
        sides = [a, b, c]
        sides.sort()
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

    # Прямоугольник
    @staticmethod
    def rectangle_area(a, b):
        return a * b

    # Квадрат
    @staticmethod
    def square_area(a):
        return a ** 2


# Тестирование
class TestGeometryCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(GeometryCalculator.circle_area(5), 78.54, places=2)

    def test_triangle_area(self):
        self.assertAlmostEqual(GeometryCalculator.triangle_area(3, 4, 5), 6)

    def test_is_right_triangle(self):
        self.assertTrue(GeometryCalculator.is_right_triangle(3, 4, 5))
        self.assertFalse(GeometryCalculator.is_right_triangle(3, 4, 6))

    def test_rectangle_area(self):
        self.assertEqual(GeometryCalculator.rectangle_area(4, 5), 20)

    def test_square_area(self):
        self.assertEqual(GeometryCalculator.square_area(4), 16)


if __name__ == "__main__":
    unittest.main()
