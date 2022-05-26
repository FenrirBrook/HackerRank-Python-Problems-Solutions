# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
# def count_substring(string, sub_string):
#     count = 0
#     pos = 0
#     for i in range(0, len(string)):
#         if sub_string in string:
#             count += 1
#             if len(sub_string) == 1:
#                 pos = string.find(sub_string) + 1
#             else:
#                 pos = string.find(sub_string) + len(sub_string) - 1
#             string = string[pos:len(string)]
#         else: break
#     return count
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        count += string.count(sub_string,i,i+len(sub_string))
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)