def run(n, arr):
    aux = list(set(arr))
    aux.sort()
    print(aux[len(aux)-2])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    run(n, arr)
    
