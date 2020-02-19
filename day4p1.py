import re

# regex to check double digits ???
# parse into array of digits
# check if array[5] > array[4] ... > array[0]

def repeating_digits(string):
    # rewrite this
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

possible = 0
passwords_as_string = []
for password in range(197487, 673251):
    as_string = str(password)
    # slow as fuck
    ones, tens, hundreds, thousands, ten_thousands, hundred_thousands = int(as_string[0]), int(as_string[1]), int(as_string[2]), int(as_string[3]), int(as_string[4]), int(as_string[5])
    if(hundred_thousands >= ten_thousands >= thousands >= hundreds >= tens >= ones and repeating_digits(as_string)):
        possible += 1

print(possible)