def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    test = input("""
What would you like to math?
1 Plus
2 Minus
3 Multiply
4 Divide

Input number to choose: """)

    if test == "1":
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        print(add(first, second))

    if test == "2":
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        print(subtract(first, second))

    if test == "3":
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        print(multiply(first, second))

    if test == "4":
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        print(divide(first, second))

    keep = input('Type "close" to stop doing math, if you want to continue press Enter')
    if keep == "close":
        break
