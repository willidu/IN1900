class BankAccountP:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):    # NEW - read balance value
        return self._balance

    def transfer(self, acc1, acc2, amount):
        acc1.withdraw(amount)
        acc2.deposit(amount)

    def print_info(self):
        first = self._first_name; last = self._last_name
        number = self._number; bal = self._balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)

a1 = BankAccountP('John', 'Olsson', '19371554951', 20000)
a2 = BankAccountP('Liz', 'Olsson',  '19371564761', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
# print("a1's balance:", a1.get_balance())
# a1.print_info()

print(a1.get_balance())
print(a2.get_balance())
a1.transfer(a1, a2, 500)
# Hvordan kan jeg få bort 'a1.' fra funksjonskallet i linje 38?
print(a1.get_balance())
print(a2.get_balance())

def test_transfer():
    a1 = BankAccountP('John', 'Cena', '123', 0)
    a1.deposit(100)
    a1.withdraw(50)
    bal = a1.get_balance()
    if bal != 50:
        raise AssertionError

    a2 = BankAccountP('Tom', 'Lindstrøm', '321', 1000)
    a2.transfer(a2, a1, 500)
    if a2.get_balance() != 500:
        raise AssertionError

test_transfer()

"""
Terminal> python BankAccountP.py
testfunksjon printer ingenting:)
"""