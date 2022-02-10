def triangle_area(vertices):
    A = 0.5 * (vertices[1][0] * vertices[2][1]
               - vertices[2][0] * vertices[1][1]
               - vertices[0][0] * vertices[2][1]
               + vertices[2][0] * vertices[0][1]
               + vertices[0][0] * vertices[1][1]
               + vertices[1][0] * vertices[0][1])
    return A


def test_triangle_area():
    """
    Verify the area of a triangle with vertices
    (0,0), (1,0), and (0,2).
    """
    v1 = [0, 0]
    v2 = [1, 0]
    v3 = [0, 2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg


"""
Terminal> pytest triangle_area.py
============================= test session starts =============================
collecting ... collected 1 item

triangle_area.py::test_triangle_area PASSED                              [100%]

======================== 1 passed, 1 warning in 0.02s =========================

Process finished with exit code 0
"""