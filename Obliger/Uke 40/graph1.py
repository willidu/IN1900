import math


def plot_line(p1, p2):
    import numpy as np
    import matplotlib.pyplot as plt
    n = 100
    line_x = np.linspace(p1[0], p2[0], n)
    line_y = np.linspace(p1[1], p2[1], n)
    plt.plot(line_x, line_y)
    plt.grid()
    return

points_list = [(0, 0), (1, 0), (0, 1), (1, 1)]

def complete_graph(points):
    import matplotlib.pyplot as plt
    print(type(points), points)
    for i in range(len(points)):
        for j in range(len(points)):
            if points[i] != points[j]:
                plot_line(points[i], points[j])
    plt.show()
    return

complete_graph(points_list)

"""
Terminal> python graph1.py
Ser at det plottes en firkant med streker mellom alle punkter.
"""

alpha = math.sqrt(2) / 2
points2 = [(1, 0), (alpha, alpha), (0, 1), (-1*alpha, alpha), (-1, 0),
           (-1*alpha, -1*alpha), (0, -1), (alpha, -1*alpha)]

complete_graph(points2)

"""
Terminal> python graph1.py
fancy pantsy plot
"""