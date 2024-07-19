#Simple function with positional arguments
def greet (x,y):
    print(f"Hi! My name is {x} {y}!")
    print ("Welcome aboard!")

greet("Donald", "Trump")
greet("Klaus", "Iohannis")

#Function that returns values (reusable).
def get_greeting(name):
    return (f"Hello {name}!")
message = get_greeting("Cici")
print(message)

#Function with optional arguments
def increment (number, by=1):
    return number+by
print (increment(2))
print(increment(2,5))

#xargs --> returns a Tuple
def multiply (*numbers):
    for x in numbers:
        print (x)

multiply(2,3,4)
##
def total (*numbers):
    total=0
    for x in numbers:
        total = total + x
    return total

print(total(2,3,4,5,6,7,8))

#xxargs --> return a dictonary
def save_user (**args):
    return args

print(save_user(id=1, name="Gigi Becali", age=54, wealth="1 Billion $"))

#FizzBuzz
def fizzbuzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizzbuzz(60))