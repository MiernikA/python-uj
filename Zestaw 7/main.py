from rectangles import Rectangle
import unittest


class TestRectangle(unittest.TestCase):

    def test_creation(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

    def test_invalid_creation(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 1, 2)

    def test_equality(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect1, rect2)

    def test_inequality(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 6, 7, 8)
        self.assertNotEqual(rect1, rect2)

    def test_center(self):
        rect = Rectangle(1, 2, 3, 4)
        center = rect.center()
        self.assertEqual(center.x, 2)
        self.assertEqual(center.y, 3)

    def test_area(self):
        rect = Rectangle(1, 2, 4, 6)
        self.assertEqual(rect.area(), 12)

    def test_move(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.move(2, 3)
        self.assertEqual(str(rect), "[(3, 5), (5, 7)]")

    def test_intersection(self):
        rect1 = Rectangle(1, 2, 4, 5)
        rect2 = Rectangle(3, 4, 6, 7)
        intersection = rect1.intersection(rect2)
        self.assertEqual(str(intersection), "[(3, 4), (4, 5)]")

    def test_invalid_intersection(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(4, 5, 6, 7)
        with self.assertRaises(ValueError):
            rect1.intersection(rect2)

    def test_cover(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(3, 4, 6, 7)
        cover_rect = rect1.cover(rect2)
        self.assertEqual(str(cover_rect), "[(1, 2), (6, 7)]")

    def test_make4(self):
        rect = Rectangle(1, 2, 5, 6)
        rects = rect.make4()
        self.assertEqual(str(rects[0]), "[(1, 2), (3, 4)]")
        self.assertEqual(str(rects[1]), "[(3, 2), (5, 4)]")
        self.assertEqual(str(rects[2]), "[(1, 4), (3, 6)]")
        self.assertEqual(str(rects[3]), "[(3, 4), (5, 6)]")


if __name__ == "__main__":
    unittest.main()
