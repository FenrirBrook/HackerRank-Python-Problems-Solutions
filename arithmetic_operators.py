def sum(a,b):
    return a + b

def difference(a,b):
    return a - b

def product(a,b):
    return a * b

def divicion(a,b):
    return a / b

if __name__ == '__main__':
    a = int(input("num 1: "))
    b = int(input("num 2: "))
    sw = int(input("presiones:\n1: suma\n2: resta\n3: multiplication\n4: divicion"))

    if sw == 1:
        print(sum(a,b))
    elif sw == 2:
        print(difference(a,b))
    elif sw == 3:
        print(product(a,b))
    elif sw == 4:
        print(divicion(a,b))
    else:
        print("error")
