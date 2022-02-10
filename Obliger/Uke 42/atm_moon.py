
d = {}

with open('atm_moon.txt') as file:
    file.readline()
    for line in file:
        words = line.split(';')
        for element in words:
            d_ = element.split('-')
            name = d_[0].upper().strip()
            value = int(''.join(letter for letter in d_[1] if letter.isdigit()).strip())

            d[name] = value

print(d)

"""
Terminal> atm_moon.py
{'HELIUM 4': 40000, 'NEON 20': 40000, 'HYDROGEN': 35000, 'ARGON 40': 30000, 'NEON 22': 5000, 'ARGON 36': 2000, 'METHANE': 1000, 'AMMONIA': 1000, 'CARBON DIOXIDE': 1000}
"""