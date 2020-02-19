# top down map, visualize?
# recursively go through each array and factorial number of elements
# only check bottom nodes, permutation based on distance to com
raw_input = open("day6_input.txt")
raw_input_test = open("day6_input.txt")

# for line in raw_input:
#     parent = line.split(")")[0]
#     children  = []
#     for line_test in raw_input_test:
#         parent_current = line_test.split(")")[0]
#         child_current = line_test.split(")")[1]
#
#         print(parent)
#         print(parent_current)
#
#         if (parent == parent_current):
#             children.append(child_current)
#     print(children)

# TOP DOWN TRAVERSAL
# new tree data type?
# start with root branch

# children of branches can be leaves or branches

# subsets? how to check
# ONLY 1 PARENT

class node():
    # wat dos self mean lol
    def __init__(self, name, parent):
        self.parent = parent
        self.children = []
        self.name = name
    def set_parent(self, parent):
        self.parent = parent
    def add_child(self, child_name):
        # for child in new_children: self.children.append(child)
        self.children.append(node(child_name, self))
        return self.children.find
    # def print_node(self):
    #     # print("parent: ", self.parent)
    #     if(self.parent != None):
    #         print(self.parent.get_name)
    #     else:
    #         print(self.parent)
    #     print("\t", self.name)
    #     if(len(self.children) > 0):
    #         for child in self.children:
    #             print("\t",child.print_node())
    # def get_name(self):
    #     return self.name
UCOM = node("COM", None)
UCOM.add_child("B")