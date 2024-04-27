from fractions import Fraction


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, value: object) -> bool:
        return self.x == value.x and self.y == value.y

    def __hash__(self):
        return hash((self.x, self.y))


class Edge:
    def __init__(self, point, line):
        self.point = point
        self.line = line

    def __str__(self):
        return f"{self.point} in {self.line}"

    def __eq__(self, value: object) -> bool:
        return self.point == value.point and self.line == value.line

    def __hash__(self):
        return hash((self.point, self.line))


class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def __str__(self):
        return f"{self.A} -> {self.B}"

    def x_length(self):
        return abs(self.A.x - self.B.x)

    def inverse_slop(self):
        dy = self.B.y - self.A.y
        dx = self.B.x - self.A.x
        return Fraction(numerator=dx, denominator=dy)

    def __eq__(self, value: object) -> bool:
        return self.A == value.A and self.B == value.B

    def __hash__(self):
        return hash((self.A, self.B))


class EdgeSlopeLine:
    def __init__(self, edge, slope, horizontal_line, point, is_entry_point):
        self.edge = edge
        self.slope = slope
        self.horizontal_line = horizontal_line
        self.point = point
        self.is_entry_point = is_entry_point

    def __str__(self):
        entry_str = "Entry" if self.is_entry_point else "Exit"
        return f"{entry_str} : {self.edge.point} -> {self.point} with slope {self.slope}, \
        edge line : {self.edge.line}, horizontal line: {self.horizontal_line}"

    def __eq__(self, value: object) -> bool:
        return self.edge == value.edge and self.edge.line == value.edge.line

    def __hash__(self):
        return hash((self.edge, self.horizontal_line))

    def set_entry_point(self, is_entry_point):
        self.is_entry_point = is_entry_point
