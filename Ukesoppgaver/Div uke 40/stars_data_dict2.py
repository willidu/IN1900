
with open('stars.txt', 'r') as file:
    stars = {}
    file.readline()
    for line in file:
        if len(line) > 2:
            lines = line.split(',')
            # print(lines)
            headers = ['name', 'distance', 'apparent brightness', 'luminosity']

            name = lines[0]
            for n in name:  # Formats name: Is ascii character, whitespace, letter or digit.
                name = ''.join(char for char in name if char.isascii() and
                               (char == ' ' or char.isalpha() or char.isdigit()))

            distance = float(lines[1])
            apparent_brightness = float(lines[2])

            luminosity = lines[-2]
            luminosity = float(luminosity[:-1])  # removes ')'

            stars[name] = {'distance': distance, 'apparent brightness': apparent_brightness,
                           'luminosity': luminosity}
        else:
            pass


for key in stars:
    print(f"Name: {key}")
    print(f"Distance: {stars[key]['distance']}")
    print(f"Apparent brightness: {stars[key]['apparent brightness']}")
    print(f"Luminosity: {stars[key]['luminosity']}")
    print()
