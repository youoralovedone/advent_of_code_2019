import re

map = [[]]
instructions = []

with open("day3p1_line_1", "r") as line_1_file:
    for line in line_1_file:
        instructions = line.split(",")
print(instructions)

def add_point(x, y):
    # sets map[x,y] as a point unless its already occupied in which case it returns the manhattan distance to the intersection
    # fix this shit
    if(map[x, y] != 0): return 1 # <-- replace 1 with sum of the coordinates
    map[x, y] = 1
    return 0

def add_line(instruction, start_x, start_y):
    direction = instruction[0]
    # remove the alpha characters from instruction
    distance = re.sub("[A-Za-z]", "", instruction)
    distance = int(distance) # condense this to 1 line

    # get first character
    if(direction == "U"):
        for point in range(0, distance):
            add_point(start_x, start_y + point)
    elif(direction == "D"):
        for point in range(0, distance):
            add_point(start_x, start_y - point)
    elif (direction == "R"):
        for point in range(0, distance):
            add_point(start_x + point, start_y)
    elif (direction == "L"):
        for point in range(0, distance):
            add_point(start_x - point, start_y)

# read instructions from directions and copy each point onto map
current_x = 0
current_y = 0
for instruction in instructions:
    add_line(instruction, current_x, current_y)
print(map)