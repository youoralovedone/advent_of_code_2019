import re

map = [[0 for x in range(2)]]
map_test = [[0 for x in range(2)]]

# get instructions
line_1_instructions = []
line_2_instructions = []
with open("day3p1_line_1", "r") as line_1_file:
    for line in line_1_file:
        line_1_instructions = line.split(",")
with open("day3p1_line_2", "r") as line_2_file:
    for line in line_2_file:
        line_2_instructions = line.split(",")

# print(line_1_instructions)
# print(line_2_instructions)

current_x = 0
current_y = 0
for instruction in line_1_instructions:
    # parse instructions
    direction = instruction[0]
    distance = int(re.sub("[A-Za-z]", "", instruction))

    # update map for line 1, no need to worry about collisions
    if(direction == "R"):
        for i in range(0, distance):
            current_x += 1
            map.append([current_x,current_y])
    elif(direction == "L"):
        for i in range(0, distance):
            current_x -= 1
            map.append([current_x,current_y])
    elif (direction == "U"):
        for i in range(0, distance):
            current_y += 1
            map.append([current_x,current_y])
    elif (direction == "D"):
        for i in range(0, distance):
            current_y -= 1
            map.append([current_x,current_y])
current_x = 0
current_y = 0
for instruction in line_2_instructions:
    # parse instructions
    direction = instruction[0]
    distance = int(re.sub("[A-Za-z]", "", instruction))

    # update map for line 1, no need to worry about collisions
    if(direction == "R"):
        for i in range(0, distance):
            current_x += 1
            map_test.append([current_x,current_y])
    elif(direction == "L"):
        for i in range(0, distance):
            current_x -= 1
            map_test.append([current_x,current_y])
    elif (direction == "U"):
        for i in range(0, distance):
            current_y += 1
            map_test.append([current_x,current_y])
    elif (direction == "D"):
        for i in range(0, distance):
            current_y -= 1
            map_test.append([current_x,current_y])

for cord in map:
    for cord_test in map_test:
        if(cord == cord_test):
            print(map.index(cord) + map_test.index(cord_test))

# print(map)
#print(map_test)