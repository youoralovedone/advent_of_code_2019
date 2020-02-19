import re
# ITS JUST ASKING FOR THE FIRST INTERSECTION
map_line_1 = []
map_line_2 = []
intersections = []

# get instructions
line_1_instructions = open('day3p1_line_1_test', 'r').readline().split(",")
line_2_instructions = open('day3p1_line_2_test', 'r').readline().split(",")

current_x_cord = 0
current_y_cord = 0
for instruction in line_1_instructions:
    direction = instruction[0]
    distance = int(re.sub("[A-Za-z]", "", instruction))

    for point in range(0, distance):
        if(direction == "U"):
            current_y_cord += 1
        elif(direction == "D"):
            current_y_cord -= 1
        elif(direction == "R"):
            current_x_cord += 1
        elif(direction == "L"):
            current_x_cord -= 1

        map_line_1.append([current_x_cord, current_y_cord])

current_x_cord = 0
current_y_cord = 0
for instruction in line_2_instructions:
    direction = instruction[0]
    distance = int(re.sub("[A-Za-z]", "", instruction))

    for point in range(0, distance):
        if (direction == "U"):
            current_y_cord += 1
        elif (direction == "D"):
            current_y_cord -= 1
        elif (direction == "R"):
            current_x_cord += 1
        elif (direction == "L"):
            current_x_cord -= 1

        map_line_2.append([current_x_cord, current_y_cord])
        if([current_x_cord, current_y_cord] in map_line_1):
            # print(current_x_cord, current_y_cord)
            print(map_line_1)
            print(map_line_2)
            print(map_line_2.index([current_x_cord, current_y_cord]) + map_line_1.index([current_x_cord, current_y_cord]))

# INDEX IS NUMBER OF STEPS
