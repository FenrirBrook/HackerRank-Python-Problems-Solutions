def printn(n):
    i=0
    cad=''
    while i<n:
        i+=1
        cad+= str(i)
    print(cad)

def validate(n):
    if n>0 and n<151:
        return True

if __name__ == '__main__':
    n = int(input())
    if validate(n)==True:
        printn(n)
