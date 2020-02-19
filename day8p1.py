from textwrap import wrap
raw_input = wrap(open("day8_input").readline(), 150)

# each layer contains 100 lines
# 100 layers
# each layer is 6, 25 rows

# 25 wide, 6 tall

layers = []
current_row = 0
for row in raw_input:
    # create a new list every 100 layers
    # if(index%25 == 0 and index != 0):
    #     layers.append([])
    #     current_row += 1
    # layers[current_row].append(row)
    layers.append(row)

# print(layers)
# print(len(layers))
# print(len(layers[0]), len(layers[1]), len(layers[2]), len(layers[3]), len(layers[4]), len(layers[5]))

def get_zeros(layer):
    amount_zeros = 0
    for pixel in layer:
        # print(pixel)
        if(pixel == '0'):
            amount_zeros += 1
    return amount_zeros
def get_ones(layer):
    amount_ones = 0
    for pixel in layer:
        if(pixel == '1'):
            amount_ones += 1
    return amount_ones
def get_twos(layer):
    amount_twos = 0
    for pixel in layer:
        if(pixel == '2'):
            amount_twos += 1
    return amount_twos

smallest_zeros = get_zeros(layers[0]) # lol
layer_with_least_zeros = layers[0]

for layer in layers:
    # print(get_zeros(layer))
    if( get_zeros(layer) < smallest_zeros):
        layer_with_least_zeros = layer
        smallest_zeros = get_zeros(layer)
print(get_ones(layer_with_least_zeros) * get_twos(layer_with_least_zeros))