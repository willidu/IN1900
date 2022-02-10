
def eval_function(expression, x_value):
    x = float(x_value)
    g = eval(expression)
    print(g, type(g))

eval_function('x**2', 2)

def eval_func_two_var(expression, k, x):
    x = float(x)
    k = float(k)
    g = eval(expression)
    print(expression, g, type(g))

eval_func_two_var('k*x**2', 2, 2)

def eval_func_2_var(expression, var_val1, var_val2):
    x = var_val1
    y = var_val2
    formula = expression
    code = f"""
    def f(x):
        return {formula}
    """
    exec(code)
    print(code)
    x = float(x)
    y = f(x)
    return y

print(eval_func_2_var('k*x**2', 2, 2))

