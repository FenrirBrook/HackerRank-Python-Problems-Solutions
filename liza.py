def run(exp, iters,ls):
    if exp == "insert":
        ls.insert(iters[0], iters[1])
    elif exp == "remove":
        ls.remove(iters[0])
    elif exp == "append":
        ls.append(iters[0])
    elif exp == "sort":
        ls.sort(iters[0])
    elif exp == "pop":
        ls.pop()
    elif exp == "reverse":
        ls.reverse()
    elif exp == "print":
        print(ls)

if __name__ == '__main__':
    ls = []
    N = int(input())
    for _ in range(N):
        exp, *line = input().split()
        iters = list(map(int, line))
        run(exp, iters,ls)
