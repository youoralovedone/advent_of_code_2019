# computer = [2,4,4,5,99,0]
computer = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0]
current_index = 0
while(current_index < len(computer)):
    #print(computer[current_index])
    # print(current_index)
    if(computer[current_index] == 1):
        # computer[computer[current_index + 3]] = computer[computer[current_index + 1]] + computer[computer[current_index + 2]]
        computer[computer[current_index + 3]] = computer[computer[current_index + 1]] + computer[computer[current_index + 2]]
        # print(computer[computer[current_index + 1]] + computer[computer[current_index + 2]])

        current_index += 4
    elif(computer[current_index] == 2):
        # print("got here")
        # computer[computer[current_index + 3]] = computer[computer[current_index + 1]] * computer[computer[current_index + 2]]
        computer[computer[current_index + 3]] = (computer[computer[current_index + 1]])*(computer[computer[current_index + 2]])
        current_index += 4
    elif (computer[current_index] == 99):
        break
print(computer)