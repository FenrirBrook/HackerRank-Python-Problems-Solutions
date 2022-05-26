def cal(n):
    if n%2 != 0:
        print("Weird")
    else:
        if n%2 == 0 and n>=2 and n<=5:
            print("Not Weird")
        else:
            if n%2 == 0 and n>=6 and n<=20:
                print("Weird")
            else:
                if n%2 == 0 and n>20:
                    print("Not Weird")

if __name__ == '__main__':
    n = int(input("ingrese un numero"))
    cal(n)
