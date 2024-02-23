from rectangles import Rectangle
from points import Point
import unittest


class TestRectangle(unittest.TestCase):

    # pomijajac testy z poprzednich zadan

    def test_top(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.top, 4)

    def test_bottom(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.bottom, 2)

    def test_left(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.left, 1)

    def test_right(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.right, 3)

    def test_width(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 2)

    def test_height(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.height, 2)

    def test_from_points(self):
        points = [Point(1, 2), Point(3, 4)]
        rect = Rectangle.from_points(points)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")


if __name__ == "__main__":
    unittest.main()
