def fill_list(n):
    list = []
    i=0
    while i < n:
        list.append(i)
        i+=1
    return list

def loops(list):
    
    for i in list:
        print(list[i]**2)

if __name__ == '__main__':
    n = int(input())
    loops(fill_list(n))
