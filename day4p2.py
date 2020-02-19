test = [1,1,1,3,4,4]
def two_digits(input):
    # rewrite this
    for i in range(0, len(input)):
        # checks first 2 digits
        if(input[0] == input[1] and input[0] != input[2]):
            return True
        # checks last 2 digits
        elif(input[len(input) - 2] == input[len(input) - 1] and input[len(input) - 2] != input[len(input) - 3]):
            return True
        # checks digits between
        elif(i + 2 < len(input) and i != 0): # not elegant
            if(input[i] == input[i+1] and input[i] != input[i-1] and input[i] != input[i + 2]): # check index 2 ahead
                return True
    return False

possible = 0
passwords_as_string = []
for password in range(197487, 673251):
    as_string = str(password)
    # check if array[5] > array[4] ... > array[0]
    # slow as fuck
    ones, tens, hundreds, thousands, ten_thousands, hundred_thousands = int(as_string[0]), int(as_string[1]), int(as_string[2]), int(as_string[3]), int(as_string[4]), int(as_string[5])
    if(hundred_thousands >= ten_thousands >= thousands >= hundreds >= tens >= ones and two_digits(as_string)):
        possible += 1

print(possible)