# The provided code stub will read in a dictionary containing 
# key/value pairs of name:[marks] for a list of students. Print the average of the marks 
# array for the student 
# name provided, showing 2 places after the decimal.
# Example
# alpha = [20, 30, 40]
# beta = [30, 50, 70]
# query_name = beta
# The query_name is 'beta'. beta's average score is . 30+50+70/3= 50.00


def run(student_marks, query_name):
    if query_name in student_marks:
        arr_marks = student_marks[query_name]
        count=0
        for i in arr_marks:
            count +=i
        print("{:.2f}".format(count/3))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    run(student_marks, query_name)
