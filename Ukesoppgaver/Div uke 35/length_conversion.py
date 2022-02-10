meters = int(input("Length in meters? "))
# Inch, feet, yards, british mile
cm = meters * 100
inch = cm / 2.54
feet = inch / 12
yard = feet / 3
british_mile = yard / 1760

print(f"{meters} meters is {inch:g} inches, {feet:g} feet, "
      f"{yard:g} yards, and {british_mile:g} miles")
