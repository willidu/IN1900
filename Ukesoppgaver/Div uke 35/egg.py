from math import pi, log

p = 1.038  # g/cm^3
c = 3.7  # J/g/K
K = 5.4e-3  # W/cm/K
T_w = 100 + 273  # Kelvin
T_y = 70 + 273  # Kelvin

print("Large egg = 67 grams, \nFridge temperature = 4 Celsius, Room temperature = 20 Celsius")

mass = int(input("Mass in grams? "))
temp = int(input("Temperature in Celsius? "))


def time(temp, mass):
    t_seconds = ((mass ** (2 / 3)) * c * (p ** (1 / 3)) /
                 (K * pi ** 2 * ((4 * pi / 3) ** (2 / 3)))) * \
                (log(0.76 * (((temp + 273) - T_w) / (T_y - T_w))))
    t_minutes = t_seconds / 60
    return t_minutes


print(f"For an egg with mass {mass} grams and temperature {temp} Celsius, \n"
      f"the time to get soft boiled is {time(temp, mass):.2f} minutes")
