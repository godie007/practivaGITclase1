def saludar():
    print("Hola mundo")

# sum tow numbers when the first param is name and second param is age
def sumar(name, age):
    print("Hola " + name + " tu edad es " + str(age))

saludar()
# call function sumar with params name and age
sumar("Andres", 32)

# create a recursive function that allows to calculate a number of the fibonacci series giving as a parameter an index and return the value
def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)
# call the fibonacci function with a random argument
print(fibonacci(4))
