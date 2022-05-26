def int_division(a,b):
    return a//b

def float_division(a,b):
    return a/b

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int_division(a,b))
    print(float_division(a,b))
