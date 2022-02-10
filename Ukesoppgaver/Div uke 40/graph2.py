from graph1 import plot_line

n = 10  # number of points
n_lines = 4  # number of vertical lines
points = []
for i in range(n_lines):
    for j in range(n):
        points.append((i, j))
# print(points)

def complete_graph(points):
    import matplotlib.pyplot as plt
    # print(type(points), points)
    for i in range(len(points)):
        for j in range(len(points)):
            if points[i][0] != points[j][0]:  # removes lines between points on same vertial line
                plot_line(points[i], points[j])
            else:
                pass
    plt.show()
    return

complete_graph(points)
