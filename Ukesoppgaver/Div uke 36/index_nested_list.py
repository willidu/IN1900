q = [["a", "b", "c"], ["d", "e", "f"], ["g", "h"]]
print(q[0][0])
print(q[1])
print(q[-1][-1])
print(q[1][0])
print(f"q[-1][-2] = {q[-1][-2]} because it is the last element in the list q, and picks the second to last element in the list q[-1]")

for i in q:
    for j in range(len(i)):
        print(i[j])
"""
In the for loop, i is the elements in list q
j is the variable used to index through the lists within q
"""