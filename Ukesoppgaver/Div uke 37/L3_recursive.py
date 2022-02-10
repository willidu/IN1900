
def L(x, n):
    s = sum(
        (1 / i) * (x / (1 + x)) ** i for i in range(1, n + 1))
    return s


def L3(x, epsilon=1.0E-6):
    x = float(x)
    i = 1
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i


def L3_ci(x, epsilon=1.0e-6):
    x = float(x)
    i = 1
    ci = (1.0 / i) * (x / (1.0 + x)) ** i
    s = ci
    while abs(ci) > epsilon:
        i += 1      # oppdaterer i
        a = (i * x - x) / (i + i * x)
        ci *= a     # oppdaterer term med ny i
        s += ci     # legger til term i sum

    return s, i


def test_L3_ci():
    x = 5
    expected = L3(x)[0]
    calculated = L3_ci(x)[0]
    tol = 1e-10
    success = abs(expected - calculated) < tol
    msg = f"L3_ci failed. Expected = {expected:.3e} with i {L3(x)[1]}. Calculated = {calculated:.3e} with i {L3(x)[1]}"
    assert success, msg


"""
Terminal> pytest L3_recursive.py
============================= test session starts =============================
collecting ... collected 1 item

L3_recursive.py::test_L3_ci PASSED                                       [100%]

======================== 1 passed, 1 warning in 0.01s =========================

Process finished with exit code 0
"""