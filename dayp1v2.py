total_orbits = 0

def get_direct_children(parent, depth):
    global total_orbits
    input_file = open("day6_input.txt")
    # need to keep track of depth
    already_iterated = False
    for line in input_file:

        line = line.strip()
        current_parent = line.split(")")[0]
        current_child = line.split(")")[1]

        # reset file so itll keep iterating
        if(parent == current_parent): # doesnt get G?
            # print(current_parent,": ", current_child)
            if(not(already_iterated)):
                depth += 1 # increments depth twice once for G and C FIX THIS
            print(current_child, ":", depth)
            get_direct_children(current_child, depth)
            total_orbits += depth

            already_iterated = True

get_direct_children("COM", 0)
print(total_orbits)