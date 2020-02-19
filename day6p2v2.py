total_orbits = 0

depth_switch = 0
depth_santa = 0
depth_you = 0

you_nodes = []
santa_nodes = []

# nodes = []

def get_direct_children(parent, depth):
    global total_orbits, depth_you, depth_santa
    input_file = open("day6_input.txt")
    # need to keep track of depth
    already_iterated = False

    # already_santa = False
    # already_you = False

    for line in input_file:

        line = line.strip()
        current_parent = line.split(")")[0]
        current_child = line.split(")")[1]

        # reset file so itll keep iterating
        if(parent == current_parent): # doesnt get G?
            # print(current_parent,": ", current_child)
            if(not already_iterated):
                depth += 1 # increments depth twice once for G and C FIX THIS

            # nodes.append([current_child, depth])
            # print(current_child, ":", depth)
            get_direct_children(current_child, depth)
            total_orbits += depth

            if(current_child == "YOU"):
                depth_you = depth
                current_you_node = current_parent
                while(current_you_node != "COM"):
                    current_you_node = get_parent(current_you_node)
                    depth -= 1
                    you_nodes.append([current_you_node, depth])

            if(current_child == "SAN"):
                depth_santa = depth
                current_santa_node = current_parent
                while(current_santa_node != "COM"):
                    current_santa_node = get_parent(current_santa_node)
                    depth -= 1
                    santa_nodes.append([current_santa_node, depth])

            # if(not is_santa):
            #     santa_nodes.append(current_parent)
            # if(not is_you):
            #     you_nodes.append(current_parent) # dont append nodes that you arent directly parented to


            already_iterated = True

def get_parent(child):
    input_file = open("day6_input.txt")
    for line in input_file:

        line = line.strip()
        current_parent = line.split(")")[0]
        current_child = line.split(")")[1]

        if(current_child == child):
            return current_parent

# iterate until current depth is < santa depth
# then iterate down until current depth = santa_depth


depth_switches = []
get_direct_children("COM", 0)
print("totsl orbits:",total_orbits)
print("depth santa:", depth_santa)
print("depth you:", depth_you)

for node in santa_nodes:
    for node_you in you_nodes:
        if(node == node_you):
            depth_switch = node_you[1]
            depth_switches.append(depth_switch)

largest_switch = 0
for switch in depth_switches:
    if switch > largest_switch:
        largest_switch = switch

print("steps: ", (130 - largest_switch) + (267 - largest_switch))