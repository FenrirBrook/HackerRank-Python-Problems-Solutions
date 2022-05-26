# Sample Input

# 3
# 1 0
# 2 $
# 3 1
# Sample Output

# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3

def run(a, b):
    try:
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

if __name__ == '__main__':
    for _ in range(int(input())):
        a = int(input())
        b = int(input())
    run(a, b)



















# def run(arr):
#     for i in arr:
#         try:
#             print(int(i[0])//int(i[1]))
#         except ZeroDivisionError as e:
#             print("Error Code:",e)
#         except ValueError as e:
#              print("Error Code:",e)

# if __name__ == '__main__':
#     arr = []
#     for _ in range(int(input())):
#         arr.append(list(input().split()))
#     run(arr)