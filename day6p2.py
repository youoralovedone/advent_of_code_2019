# use pathfinding algo to find shortest path between santa node and you node
santa_depth = 0
you_depth = 0
total_orbits = 0
total_steps_to_santa = 0

def get_direct_children(parent, depth):
    global total_orbits, santa_depth, you_depth

    input_file = open("day6_input.txt")
    already_iterated = False

    for line in input_file:
        line = line.strip()
        current_parent = line.split(")")[0]
        current_child = line.split(")")[1]
        if(parent == current_parent): # doesnt get G?
            if(not(already_iterated)):
                depth += 1 # increments depth twice once for G and C FIX THIS


            get_direct_children(current_child, depth)
            total_orbits += depth

            if(current_child == "YOU"):
                you_depth = depth

            elif(current_child == "SAN"):
                santa_depth = depth

            already_iterated = True

            # while depth is > santa depth iterate backwards
            # when depth is < santa depth iterate forwards

            # FIND NODE IN COMMON

def get_direct_parent(child, depth):
    # global santa_depth, you_depth

    input_file = open("day6_input.txt")
    already_iterated = False

    for line in input_file:
        line = line.strip()
        current_parent = line.split(")")[0]
        current_child = line.split(")")[1]

        # print(current_parent, ":", depth)

        if(child == current_child): # doesnt get G?
            if(not(already_iterated)):
                depth -= 1 # increments depth twice once for G and C FIX THIS

            get_direct_parent(current_parent, depth)
            already_iterated = True

get_direct_children("COM", 0)
get_direct_parent("SAN", santa_depth)
print("santa:", santa_depth)
print("you:", you_depth)
# print(depth_santa - depth_you)
# need to get to depth santa