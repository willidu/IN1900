f = 0
while f <= 100:
    C = (f - 32) * (5 / 9)
    C_approx = (f - 30) / 2
    print(f"F: {f}, C: {C:.1f}, C approx: {C_approx:.1f}")
    f += 10
