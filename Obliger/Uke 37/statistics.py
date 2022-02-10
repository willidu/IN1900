import numpy as np
from math import sqrt


def mean(x_list):
    N = len(x_list)
    i = 0
    s = 0
    while i < N:
        s += x_list[i]
        i += 1
    if i == N:
        return 1 / N * s


def test_mean():
    x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.mean(x_test_values)
    computed = mean(x_test_values)
    tol = 1e-10
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg


def standard_deviation(x_list):
    x_mean = mean(x_list)
    N = len(x_list)
    i = 0
    s = 0
    while i < N:
        s += (x_list[i] - x_mean) ** 2
        i += 1
    if i == N:
        S_n = sqrt(1 / N * s)
        return S_n


def test_standard_deviation():
    x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.std(x_test_values)
    computed = standard_deviation(x_test_values)
    tol = 1e-10
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg


"""
Terminal> pytest statistics.py
============================= test session starts =============================
collecting ... collected 2 items

statistics.py::test_mean PASSED                                          [ 50%]
statistics.py::test_standard_deviation PASSED                            [100%]

======================== 2 passed, 1 warning in 0.01s =========================

Process finished with exit code 0
"""
