computer_test = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
computer_real = [] # keep blank until done testing for cleanliness

# ABCDE
#  1002
#
# DE - two-digit opcode,      02 == opcode 2
#  C - mode of 1st parameter,  0 == position mode
#  B - mode of 2nd parameter,  1 == immediate mode
#  A - mode of 3rd parameter,  0 == position mode,
#                                   omitted due to being a leading zero
# value of A will always be 0

# commands:
#   1, p1, p2, p3 - add p1 + p2 --> output to p3
#   2, p1, p2, p3 - multiply p1 * p2 --> output p3
#   3, p1 - get user input --> output p1
#   4, p1 - output p1
#   5, p1 - jump to p1
#   99 - break
#   7, p1, p2, p3 - p1 < p2 --> output to p3
#   8, p1, p2, p3 - p1 == p2 --> output to p3

# TODO: fix jumps, everything else is literally working fine fucking fuck FUCK

def compute(computer):
    current_mem_location = 0
    one_arg_commands = ["04", "03"]
    while (current_mem_location < len(computer)-2):

        # print(computer)

        raw_command = str(computer[current_mem_location])
        command = ""
        if(len(raw_command) == 1):
            # converts opcodes in format 1, 2, 3, 4 to position mode format 0001, 0002 ...
            command = "000" + raw_command
        else:
            command = raw_command

        opcode = command[2:] # op code last two digits
        # modes of parameters IMPORTANT: mode 1 is second parameter's mode
        modes = command[:2] # first 3

        first_parameter_value = None
        second_parameter_value = None

        # add support for relative mode for day 9
        # sets parameter values based on mode

        if(modes[1] == "1"):
            first_parameter_value = computer[current_mem_location + 1]
        elif(modes[1] == "0"):
            first_parameter_value = computer[computer[current_mem_location + 1]]

        if(modes[0] == "1" and not(opcode in one_arg_commands)):
            second_parameter_value = computer[current_mem_location + 2]
        elif(modes[0] == "0" and not(opcode in one_arg_commands)):
            second_parameter_value = computer[computer[current_mem_location + 2]]

        # opcode conditional tree
        if(opcode == "01"):
            computer[current_mem_location + 3] = first_parameter_value + second_parameter_value
            current_mem_location += 4
        elif(opcode == "02"):
            computer[current_mem_location + 3] = first_parameter_value * second_parameter_value
            current_mem_location += 4
        elif(opcode == "03"):
            # unnecessary, but when I remove it, everything breaks
            if (modes[1] == "0"):
                first_parameter_value = computer[current_mem_location + 1]
            elif (modes[1] == "1"):
                first_parameter_value = computer[computer[current_mem_location + 1]]

            computer[first_parameter_value] = int(input("in: "))
            current_mem_location += 2

        elif(opcode == "04"):
            print("out:", first_parameter_value)
            current_mem_location += 2
        elif(opcode == "05"):
            if(first_parameter_value != 0):
                current_mem_location = second_parameter_value
            else:
                current_mem_location += 3
        elif(opcode == "06"):
            if (first_parameter_value == 0):
                current_mem_location = second_parameter_value
            else:
                current_mem_location += 3
        elif(opcode == "07"):
            if(first_parameter_value < second_parameter_value):
                computer[computer[current_mem_location + 3]] = 1
                current_mem_location += 4
            else:
                computer[computer[current_mem_location + 3]] = 0
                current_mem_location += 4
        elif(opcode == "08"):
            if(first_parameter_value == second_parameter_value):
                computer[computer[current_mem_location + 3]] = 1
                current_mem_location += 4
            else:
                computer[computer[current_mem_location + 3]] = 0
                current_mem_location += 4

        elif(raw_command == "99"):
            break


compute(computer_test)