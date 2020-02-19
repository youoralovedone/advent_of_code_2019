# computer = [3,8,1001,8,10,8,105,1,0,0,21,38,47,64,85,106,187,268,349,430,99999,3,9,1002,9,4,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,101,3,9,9,102,5,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,3,9,101,2,9,9,102,4,9,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
amp = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

current_output = 0 # ewwwww not encapsulated EWWWW

def compute(computer, input_1, input_2): # actually have output output

    global current_output

    first_input = True

    current_index = 0
    while(current_index < len(computer) ):
        if(computer[current_index] == 1):
            computer[computer[current_index + 3]] = computer[computer[current_index + 1]] + computer[computer[current_index + 2]]
            current_index += 4
        elif(computer[current_index] == 2):
            computer[computer[current_index + 3]] = computer[computer[current_index + 1]] * computer[computer[current_index + 2]]
            current_index += 4
        elif (computer[current_index] == 3):

                computer[computer[current_index + 1]] = int(input_1) if first_input else int(input_2)
                print("input:", int(input_1) if first_input else int(input_2))
                if(first_input):
                    first_input = False

                current_index += 2

        elif (computer[current_index] == 4):
                print("output: ", computer[computer[current_index + 1]])
                current_output = computer[computer[current_index + 1]]
                current_index += 2
        elif (computer[current_index] == 99):
            break
        elif(computer[current_index] == 5):
            if(computer[computer[current_index + 1]] != 0):
                current_index = computer[computer[current_index + 2]]
            else:
                current_index += 3
        elif(computer[current_index] == 6):
            if(computer[computer[current_index + 1]] == 0):
                current_index = computer[computer[current_index + 2]]
            else:
                current_index += 3
        elif(computer[current_index] == 7):
            if(computer[computer[current_index + 1]] < computer[computer[current_index + 2]]):
                computer[computer[current_index + 3]] = 1
                current_index += 4
            else:
                computer[computer[current_index + 3]] = 0
                current_index += 4
        elif(computer[current_index] == 8):
            if (computer[computer[current_index + 1]] == computer[computer[current_index + 2]]):
                computer[computer[current_index + 3]] = 1
                current_index += 4
            else:
                computer[computer[current_index + 3]] = 0
                current_index += 4
        else:
            opcode = str(computer[current_index])
            if(len(opcode) < 4): opcode = "0" + opcode
            op = int(opcode[len(opcode) - 1])

            parameter_1_value = 0
            parameter_2_value = 0

            if(op != 4 and op != 3):
                parameter_1_value = computer[current_index + 1] if opcode[1] == '1' else computer[computer[current_index + 1]]
                parameter_2_value = computer[current_index + 2] if opcode[0] == '1' else computer[computer[current_index + 2]]
            else:
                parameter_1_value = computer[current_index + 1] if opcode[1] == '1' else computer[computer[current_index + 1]]

            output_index = computer[current_index + 3]
            if(op == 1):
                computer[output_index] = parameter_1_value + parameter_2_value
                current_index += 4
            elif(op == 2):
                computer[output_index] = parameter_1_value * parameter_2_value
                current_index += 4
            elif(op == 3):

                computer[computer[current_index + 1]] = int(input_1) if first_input else int(input_2)
                print("input:", int(input_1) if first_input else int(input_2))
                if(first_input):
                    first_input = False

                current_index += 2

            elif(op == 4):
                print("output:", parameter_1_value)
                current_output = parameter_1_value
                current_index += 2

            elif (op == 5):
                if (parameter_1_value != 0):
                    current_index = parameter_2_value
                else:
                    current_index += 3
            elif (op == 6):
                if (parameter_1_value == 0):
                    current_index = parameter_2_value
                else:
                    current_index += 3

            elif (op == 7):
                if (parameter_1_value < parameter_2_value):
                    computer[computer[current_index + 3]] = 1
                    current_index += 4
                else:
                    computer[computer[current_index + 3]] = 0
                    current_index += 4
            elif (op == 8):
                if (parameter_1_value == parameter_2_value):
                    computer[computer[current_index + 3]] = 1
                    current_index += 4
                else:
                    computer[computer[current_index + 3]] = 0
                    current_index += 4

def amp_computer(amp):
    global current_output

    current_input = int(input("first input: "))
    print()

    current_phase_setting = 4
    for i in range(0, 5):
        current_amp = amp

        compute(current_amp, current_phase_setting, current_input)
        current_input = current_output

        current_phase_setting -= 1 # just for test, real would need to iterate

# 4,3,2,1,0
amp_computer(amp)