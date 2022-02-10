import numpy as np


def extract_data(filename):
    t = []
    with open(filename) as file:
        file.readline()
        for line in file:
            lines = line.split()
            for i in range(len(lines)):
                t.append(float(lines[i]))
    return t


def analyze_data(filename):
    t = extract_data(filename)
    t_mean = np.mean(t)
    t_max = np.max(t)
    t_min = np.min(t)
    print("Data from", filename)
    print(f"Mean temperature = {t_mean:.1f} Celsius \nMax temperature = {t_max} \nMin temperature = {t_min}")


analyze_data('temp_oct_1945.txt')
analyze_data('temp_oct_2014.txt')

"""
Terminal> python temp_read_write.py
Data from temp_oct_1945.txt
Mean temperature = 6.5 Celsius 
Max temperature = 11.6 
Min temperature = 2.1
Data from temp_oct_2014.txt
Mean temperature = 8.9 Celsius 
Max temperature = 13.6 
Min temperature = 2.3
"""

oct_1945 = extract_data('temp_oct_1945.txt')
oct_2014 = extract_data('temp_oct_2014.txt')


def write_formatting(filename, list1, list2):
    with open(filename, "w") as outfile:
        for i in range(len(list1)):
            outfile.write(f"{list1[i]:4}, {list2[i]:4} \n")


write_formatting('temp_formatted.txt', oct_1945, oct_2014)

"""
Data from temp_formatted.txt
 7.2,  9.8 
 8.1, 11.6 
 8.9, 11.5 
11.6, 13.3 
 7.7, 12.6 
 8.7, 10.3 
 6.9,  7.5 
 5.4,  9.3 
 8.8, 10.3 
 8.9, 10.3 
 3.7,  8.4 
 3.3,  8.8 
 5.2,  5.0 
 9.6,  5.8 
10.8,  6.8 
 5.0,  2.3 
 5.4,  3.5 
 9.5,  7.9 
 5.3, 11.8 
 5.8, 10.7 
 2.3,  9.0 
 4.1,  5.8 
 6.6,  6.8 
 8.2, 11.7 
 6.1, 10.6 
 8.9, 11.7 
 6.6, 13.1 
 4.1, 13.6 
 2.8,  8.0 
 2.1,  3.5 
 4.1,  3.2 
"""