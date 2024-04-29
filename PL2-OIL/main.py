from geometry import Point, Edge, Line, EdgeSlopeLine
import matplotlib.pyplot as plt

n = int(input())
edges = []
horizontal_lines = []
hline_dict = {}

for i in range(n):
    x1, x2, y = map(int, input().split())

    if y not in hline_dict:
        hline_dict[y] = set([(x1, x2)])
    else:
        tmp = hline_dict[y].copy()
        for x1_, x2_ in tmp:
            if x1_ < x1 < x2 < x2_:
                continue
            elif x1 < x1_ < x2_ < x2:
                hline_dict[y].remove((x1_, x2_))
        hline_dict[y].add((x1, x2))

    if x1 == x2:
        continue

    A = Point(x1, y)
    B = Point(x2, y)

    if x1 > x2:
        A, B = B, A

    line_A_B = Line(A, B)  # Horizontal Segment

    edgeA = Edge(A, line_A_B)
    edgeB = Edge(B, line_A_B)

    edges.append(edgeA)
    edges.append(edgeB)

    horizontal_lines.append(line_A_B)

# Case distinction
if len(horizontal_lines) == 0:
    print(0)
    exit()

if len(horizontal_lines) == 1:
    print(horizontal_lines[0].x_length())
    exit()

if all(horizontal_lines[0].A.y == hline.A.y for hline in horizontal_lines):
    print(max(hline.x_length() for hline in horizontal_lines))
    exit()

edge_map = {}

for fixed_edge in edges:
    edge_slope_lines = []
    for hline in horizontal_lines:

        if fixed_edge.line == hline:
            continue

        if hline.A.y == fixed_edge.point.y:
            continue

        tmp_points_hline = [hline.A, hline.B]
        for point in tmp_points_hline:
            invert_slope = None

            if fixed_edge.point.y != point.y:
                tmp_line = Line(fixed_edge.point, point)
                invert_slope = tmp_line.inverse_slop()
            else:
                invert_slope = float("inf")

            edge_slope_line = EdgeSlopeLine(
                fixed_edge, invert_slope, hline, point, True
            )  # Entry point not important

            edge_slope_lines.append(edge_slope_line)
    edge_map[fixed_edge] = edge_slope_lines

# Sort the edge_slope_lines by slope for each edge
for fe in edge_map:
    edge_map[fe].sort(key=lambda esl: esl.slope)
    tmp = set()
    for esl in edge_map[fe]:
        if esl not in tmp:
            esl.set_entry_point(True)
            tmp.add(esl)
        else:
            esl.set_entry_point(False)
    edge_map[fe].sort(key=lambda esl: (esl.slope, not esl.is_entry_point))

def draw():
    # Creating a color map
    cmap = plt.get_cmap("Blues")

    i = 0
    # Plotting the horizontal lines
    for fixed_edge in edge_map:
        edge_slope_lines = edge_map[fixed_edge]
        for esl in edge_slope_lines:
            # Draw horizontal lines in red
            x = [esl.horizontal_line.A.x, esl.horizontal_line.B.x]
            y = [esl.horizontal_line.A.y, esl.horizontal_line.B.y]
            plt.plot(x, y, color="red")

            # Calculate color intensity (ranges from 0.3 to 1)
            color_intensity = 0.3 + 0.7 * i / len(edge_slope_lines)
            color = cmap(color_intensity)

            # Draw the edge in blue dotted line
            x = [esl.edge.point.x, esl.horizontal_line.A.x]
            y = [esl.edge.point.y, esl.horizontal_line.A.y]
            plt.plot(x, y, color=color, linestyle="dotted")

            i += 1

    plt.show()


# draw()

max_length = 0

for fixed_edge in edge_map:
    edge_slope_lines = edge_map[fixed_edge]
    length = fixed_edge.line.x_length()

    for i in range(len(edge_slope_lines)):
        esl = edge_slope_lines[i]
        if esl.is_entry_point:
            length += esl.horizontal_line.x_length()
        else:
            length -= esl.horizontal_line.x_length()
        max_length = max(max_length, length)

print(max_length)
