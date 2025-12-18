# Addition using while loop

def add(a,b):
    result = a
    while b > 0:
        result += 1
        print(result)
        b -= 1


def add1 (a,b):
    sum = a+b
    return sum



a = 10
b = 7

print(add(a,b))
print(add1(a,b))