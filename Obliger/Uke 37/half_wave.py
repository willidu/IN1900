import math
from math import sin, pi


def f(x):
    if sin(x) > 0:
        return sin(x)
    elif sin(x) <= 0:
        return 0


def test_f():
    """
    Tester om f(0) gir 0 og om f(pi/2) gir 1
    """
    x_1 = 0
    expected_1 = 0
    computed_1 = f(x_1)
    x_2 = math.pi / 2
    expected_2 = 1
    computed_2 = f(x_2)
    tol = 1e-10
    success = abs(expected_1 - computed_1) < tol and abs(expected_2 - computed_2) < tol
    msg = f"Test failed"
    assert success, msg


"""
Terminal> pytest half_wave.py
============================= test session starts =============================
collecting ... collected 1 item

half_wave.py::test_f PASSED                                              [100%]

======================== 1 passed, 1 warning in 0.00s =========================

Process finished with exit code 0
"""
