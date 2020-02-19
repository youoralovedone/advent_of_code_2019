import re
# ITS JUST ASKING FOR THE FIRST INTERSECTION
map = [[0 for x in range(2)]]
intersections = [[0 for x in range(2)]]

# get instructions
line_1_instructions = []
line_2_instructions = []
with open("day3p1_line_1", "r") as line_1_file:
    for line in line_1_file:
        line_1_instructions = line.split(",")
with open("day3p1_line_2", "r") as line_2_file:
    for line in line_2_file:
        line_2_instructions = line.split(",")

current_x = 0
current_y = 0
for index in range(0, len(line_1_instructions)):
    # parse instructions
    line_1_direction = line_1_instructions[index]
    line_1_distance = int(re.sub("[A-Za-z]", "",  line_1_instructions[index]))

    line_2_direction = line_2_instructions[index]
    line_2_distance = int(re.sub("[A-Za-z]", "",  line_2_instructions[index]))

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