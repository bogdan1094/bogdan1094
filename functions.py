#Simple function with positional arguments
def greet (x,y):
    print(f"Hi! My name is {x} {y}!")
    print ("Welcome aboard!")

greet("Donald", "Trump")
greet("Klaus", "Iohannis")

#Funtion that returns values (reusable).
def get_greeting(name):
    return (f"Hello {name}!")
message = get_greeting("Cici")
print(message)
#Function with optional arguments