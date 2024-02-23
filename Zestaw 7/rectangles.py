from points import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):

        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid values")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        middle_x = (self.pt1.x + self.pt2.x) / 2
        middle_y = (self.pt1.y + self.pt2.y) / 2
        if middle_y % 1 == 0:
            middle_y = int(middle_y)
        if middle_x % 1 == 0:
            middle_x = int(middle_x)

        return Point(middle_x, middle_y)

    def area(self):
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

    def intersection(self, other):
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)

        if x1 >= x2 or y1 >= y2:
            raise ValueError("Rectangles do not intersect")

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        center = self.center()
        return (
            Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),
            Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),
            Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),
            Rectangle(center.x, center.y, self.pt2.x, self.pt2.y),
        )
