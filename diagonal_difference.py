# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:
# The left-to-right diagonal = 1 +5+9=15. The right to left diagonal = 3+5+9=17. Their absolute difference is .2


def diagonalDifference(arr):
    count = 0 
    amount = 0
    amount2 = 0

    for i in arr:
        amount += i[count]
        count += 1
    for i in arr:
        amount2 += i[count-1]
        count -= 1

    return abs(amount - amount2)
    
if __name__ == '__main__':

    arr = [[1,2,3],[2,2,3],[3,3,3]]

    print(diagonalDifference(arr))
    

     