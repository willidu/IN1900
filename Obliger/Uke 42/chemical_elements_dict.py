elements_10 = {1: '-', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5:'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: '-', 9: 'Fluorine', 10: 'Neon'}

elements_10[1] = 'Hydrogen'
elements_10[8] = 'Oxygen'

# print(elements_10)

"""
Terminal> chemical_elements_dict.py
{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon'}

Omskrevet 1 og 8 som oppgaven sa.
"""

elements_10_copy = elements_10.copy()
elements_10_copy.update({11: 'Sodium'})
print(elements_10)
print('\n')

elements_11 = elements_10
elements_11.update({11: 'Sodium'})
print(elements_10)

"""
Terminal> chemical_elements_dict.py
{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon'}


{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon', 11: 'Sodium'}

Observerer at første utskrift ikke inneholder 11: 'Sodium' men det gjør den siste printen. Det er fordi i første utskrift lager en kopi av elements_10 som vi gjør endringer på men printer likevel den originale element_10. I den siste utskriften endrer vi både elements_11 og elements_10 ved å oppdatere elements_11.
"""