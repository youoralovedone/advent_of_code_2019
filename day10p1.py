# res_x = len(open("day10_input").readline().strip())
res_y = sum(1 for line in open("day10_input"))
map = []
asteroids = []

for line in open("day10_input"):
    for node in line.strip():
        map.append(node)

def to_index(x, y):
    return x + res_y*y

# DRAW LINE TO AND ITERATE THROUGH OTHER ASTEROIDS TO SEE IF THEY LIE ON THE LINx E