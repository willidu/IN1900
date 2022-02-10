class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_name(self, str):
        self.name = str
        return self.name

    def set_age(self, val):
        self.age = val
        return self.age
    
    def set_gender(self, gender):
        self.gender = gender
        return self.gender

    def __str__(self):
        return f'{self.name}, {self.age}, {self.gender}'

f = Person('John', 55, 'Male')
print(f)

f.set_name('Not John')
f.set_gender('nonbinary')
print(f)
        
"""
Terminal> python class_people.py
John, 55, Male
Not John, 55, nonbinary
"""