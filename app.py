# print("Hello, World!")

alfa = 20
beta = 30
print("Produsul a doua numere este: ", alfa * beta)
print("Lungimea cuvantului 'Hello, World!' este: ", len("Hello, World!"))
print("Prima litera a cuvantului 'Hello, World!' este: ", "Hello, World!"[0])
print("Primele 3 litere ale cuvantului 'Hello, World!' sunt: ", "Hello, World!"[0:3])
print("A 5-a litera din alfabet este: ", "abcdefghijklmnopqrstuvwxyz"[4])


def multiply(a, b):
    return a * b

print(multiply(20, 30))

class Cow:
    def __init__(self, name):
        self.name = name

    def say(self):
        return "Muuu!"

cow = Cow("Bella")
print(cow.name)
print(cow.say())

