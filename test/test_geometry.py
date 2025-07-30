import unittest
from src.geometry import Circle, Rectangle

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertEqual(circle.area(), math.pi * 25)

    def test_rectangle_area(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

if __name__ == '__main__':
    unittest.main()