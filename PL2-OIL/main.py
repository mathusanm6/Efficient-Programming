#########################################
##
##  SOLUTION FOR OIL WELLS PROBLEM
##  BY: YANIS LACENNE (MAINLY) AND GABIN DUDILLIEU
##  AND MATHUSAN SELVAKUMAR
##
#########################################

from enum import IntEnum
from fractions import Fraction


class Orientation(IntEnum):
    IN = 0
    OUT = 1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.line = None

    def __str__(self):
        return f"({self.x}, {self.y})"

    def is_right(self):
        return self.line.B == self

    def is_left(self):
        return self.line.A == self

    def is_below(self, other):
        return self.y < other.y

    def is_above(self, other):
        return self.y > other.y


class Line:
    def __init__(self, A: "Point", B: "Point"):
        self.A = A
        self.B = B
        self.abs_length = self.compute_abs_length()

    def __str__(self):
        return f"{self.A} -> {self.B}"

    def compute_abs_length(self):
        return self.B.x - self.A.x

    def slope(self) -> Fraction:
        diff_ord = self.B.y - self.A.y
        diff_abs = self.B.x - self.A.x
        return Fraction(numerator=-diff_abs, denominator=diff_ord)


def in_or_out(fixe, other):
    if other.is_above(fixe):
        if other.is_right():
            return Orientation.IN
        else:
            return Orientation.OUT
    else:
        if other.is_left():
            return Orientation.IN
        else:
            return Orientation.OUT


# Read input
n = int(input())
points = []
for i in range(n):
    x1, x2, y = map(int, input().split())

    if x1 == x2:
        continue

    A = Point(x1, y)
    B = Point(x2, y)

    if x1 > x2:
        A, B = B, A

    points.append(A)
    points.append(B)
    line = Line(A, B)
    A.line = line
    B.line = line

# Case distinction
if len(points) == 0:
    print(0)
    exit()

if len(points) == 2:
    print(points[0].line.abs_length)
    exit()

max_value = 0
for point_fixe in points:

    slopes = []
    for other in points:
        if other == point_fixe or other.y == point_fixe.y:
            continue
        line = Line(point_fixe, other)
        slopes.append((other, line.slope(), in_or_out(point_fixe, other)))

    slopes.sort(key=lambda x: (x[1], x[2]))

    pf_max_value = point_fixe.line.abs_length
    value = pf_max_value
    for p in slopes:
        other, _, orientation = p

        if orientation == Orientation.OUT:
            value -= other.line.abs_length
        elif orientation == Orientation.IN:
            value += other.line.abs_length
            pf_max_value = max(value, pf_max_value)

    max_value = max(max_value, pf_max_value)

print(max_value)
