class Mammal:
    def __init__(self):
        return

    def info(self):
        return 'I have hair on my body'

    def identity_mammal(self):
        print('I am a mammal')

class Primate(Mammal):
    def __init__(self):
        super(Mammal, self)
    
    def info(self):
        return (Mammal.info(self)) + f'\n' + 'I have a large brain'

    def identity_primate(self):
        print('I am a primate')

class Human(Primate):
    def __init__(self):
        super(Primate, self)
    
    def info(self):
        return Primate.info(self) + f'\n' + 'I have feelings'

    def identity_human(self):
        print('I am a human')

class Ape(Primate):
    def __init__(self):
        super(Primate, self)
    
    def info(self):
        return Primate.info(self) + f'\n' + 'I like bananas'

    def identity_ape(self):
        print('I am an ape')

John = Human()
Julius = Ape()

for e in (John, Julius):
    print(e.info())
    e.identity_mammal()
    e.identity_primate()
    # e.identity_human()
    # e.identity_ape()

    print(isinstance(e, Mammal))
    print(isinstance(e, Primate))
    print(isinstance(e, Human))
    print(isinstance(e, Ape))


"""
Terminal> python inheritance.py
 AttributeError
'Human' object has no attribute 'identity_ape'

AttributeError
'Ape' object has no attribute 'identity_human'

som gir mening da Ape og Human er separate klasser og metoden identity_ape hører kun til i Ape.

I have hair on my body
I have a large brain
I have feelings
I am a mammal
I am a primate
True
True
True
False (isinstance(John, Ape))
I have hair on my body
I have a large brain
I like bananas
I am a mammal
I am a primate
True
True
False (isinstance(Julius, Human))
True
"""