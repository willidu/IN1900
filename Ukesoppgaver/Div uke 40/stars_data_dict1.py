
with open('stars.txt', 'r') as file:
    d = {}
    file.readline()
    for line in file:
        if len(line) > 2:
            lines = line.split(',')

            name = lines[0]
            name = name[4:-3]  # Removes the weird characters from name string

            luminosity = lines[-2]
            luminosity = float(luminosity[:-1])  # removes ')'

            d[name] = luminosity
        else:
            pass

print(d)
