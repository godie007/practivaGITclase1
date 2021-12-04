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

# calculate median of a list of numbers
def median(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[int(len(list)/2)] + list[int(len(list)/2) - 1])/2
    else:
        return list[int(len(list)/2)]
# cal the median function with a random list of numbers random
print(median([1,2,3,4,5,6,7,8,9,10]))


print(fibonacci(4))
