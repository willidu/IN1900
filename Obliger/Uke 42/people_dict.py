
def read_person_data(filename):
    d = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split(',')
            d[words[0].strip()] = {'Age': int(words[1]), 'Gender': words[2].strip()}
    return d


def write_person_data(data_dict, filename):
    with open(filename, 'w') as file:
        for key in data_dict:
            file.write(f"{key}, {(data_dict[key]['Age'])}, {data_dict[key]['Gender']}\n")

write_person_data(read_person_data('names.txt'), 'names2.txt')

"""
Terminal> people_dict.py
skriver filen med samme format som fila vi leste inn fra.
"""