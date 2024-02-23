from points import Point
from rectangles import Rectangle
import unittest


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p1_1 = Point(1, 2)
        self.p2 = Point(0, 5)
        self.p3 = Point(-2, -3)

    def test_init(self):
        self.assertEqual(self.p1.x, 1)
        self.assertEqual(self.p1.y, 2)
        self.assertEqual(self.p3.x, -2)
        self.assertEqual(self.p3.y, -3)

    def test_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")
        self.assertEqual(str(self.p3), "(-2, -3)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(1, 2)")
        self.assertEqual(repr(self.p3), "Point(-2, -3)")

    def test_eq_and_ne(self):
        self.assertEqual(self.p1, self.p1_1)
        self.assertNotEqual(self.p1, self.p2)

    def test_add(self):
        result_1 = self.p1 + self.p2
        result_2 = self.p1 + self.p3

        self.assertEqual(result_1, Point(1, 7))
        self.assertEqual(result_2, Point(-1, -1))

    def test_sub(self):
        result_1 = self.p1 - self.p2
        result_2 = self.p1 - self.p3

        self.assertEqual(result_1, Point(1, -3))
        self.assertEqual(result_2, Point(3, 5))

    def test_mul(self):
        result_1 = self.p1 * self.p2
        result_2 = self.p1 * self.p3

        self.assertEqual(result_1, 10)
        self.assertEqual(result_2, -8)

    def test_cross(self):
        result_1 = self.p1.cross(self.p2)
        result_2 = self.p1.cross(self.p3)

        self.assertEqual(result_1, 5)
        self.assertEqual(result_2, 1)

    def test_length(self):
        self.assertEqual(self.p1.length(), 5 ** (1 / 2))
        self.assertEqual(self.p2.length(), 5)

    def test_hash(self):
        self.assertEqual(self.p1.__hash__(), self.p1_1.__hash__())
        self.assertNotEqual(self.p1.__hash__(), self.p3.__hash__())


# ===============================================

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(1, 2, 3, 4)
        self.r2 = Rectangle(1, 2, 3, 4)
        self.r3 = Rectangle(-5, -6, 0, -8)
        self.r4 = Rectangle(13, -12, 15, 8)

    def test_init(self):
        self.assertEqual(self.r1.pt1, Point(1, 2))
        self.assertEqual(self.r1.pt2, Point(3, 4))
        self.assertEqual(self.r3.pt1, Point(-5, -6))
        self.assertEqual(self.r3.pt2, Point(0, -8))

    def test_str(self):
        self.assertEqual(str(self.r1), "[(1, 2), (3, 4)]")
        self.assertEqual(str(self.r3), "[(-5, -6), (0, -8)]")

    def test_repr(self):
        self.assertEqual(repr(self.r1), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(self.r3), "Rectangle(-5, -6, 0, -8)")

    def test_eq_and_ne(self):
        self.assertEqual(self.r1, self.r2)
        self.assertNotEqual(self.r1, self.r3)

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(2, 3))
        self.assertEqual(self.r3.center(), Point(-2.5, -7))

    def test_area(self):
        self.assertEqual(self.r1.area(), 4)
        self.assertEqual(self.r3.area(), 14.5)

    def test_move(self):
        self.r1.move(2,3)
        self.assertEqual(self.r1.pt1, Point(3, 5))
        self.assertEqual(self.r1.pt2, Point(5, 7))


if __name__ == '__main__':
    unittest.main()
