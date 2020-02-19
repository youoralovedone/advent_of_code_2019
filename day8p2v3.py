from textwrap import wrap

res_x = 25
res_y = 6

# split each layer into
# layer_length is res_x*res_y

# final_image = [2 for i in range(0, res_x*res_y)]
layers = wrap(open("day8_input").readline(), res_x*res_y)
final_image = wrap(layers[len(layers)-1],1)

# print(layers)

for layer_index in range(len(layers)-1, -1, -1):
    current_layer = layers[layer_index]
    # print(current_layer)

    for pixel_index in range(0, len(current_layer)-1):
        current_pixel = current_layer[pixel_index]
        if(current_pixel == "0" or current_pixel == "1"):
            # print("updated")
            final_image[pixel_index] = current_pixel

# print(final_image)

for pixel_index in range(0, len(final_image)):
    if(pixel_index%res_x == 0 and pixel_index != 0):
        print()
    current_pixel = final_image[pixel_index]
    print(" " if current_pixel == "0" else "X", end="")