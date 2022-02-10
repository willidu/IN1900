k_e = 9.0e9  # Nm^2/C^2
e = 1.6e-19  # C
G = 6.7e-11  # N/kg^2/m^2
m_p = 1.7e-27  # kg
m_e = 9.1e-31  # kg
r = 5.3e-11  # m

Fc = k_e * ((e**2)/(r**2))
Fg = G * ((m_p * m_e)/(r**2))
ratio = Fc / Fg
print(f"Fc = {Fc:.2e} N \nFg = {Fg:.2e} N \nRatio Fc/Fe = {ratio:.2e}")