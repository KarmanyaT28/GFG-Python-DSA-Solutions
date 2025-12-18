# Subtraction using a while loop

def subtract(a,b):
    if a>b:
        diff = a-b
    else:
        diff = b-a

    print(diff)


a = 15
b = 7
print(subtract(a,b))