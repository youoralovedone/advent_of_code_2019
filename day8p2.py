from textwrap import wrap
layers = wrap(open("day8_input").readline(), 150)
# each layer contains 100 lines
# 100 layers
# each layer is 6, 25 rows

# 25 wide, 6 tall

for layer in layers:
    for row in wrap(layer, 25):
        print(row)
    print()

# for layer_index in range(len(layers)-1, 0, -1):
#     for pixel_index in range(len(layers[layer_index])-1, 0, -1):
#         test_pixel = layers[layer_index+1][pixel_index]
#         pixel = layer_index[layer_index][pixel_index]
#
#         if(test_pixel == 1 or test_pixel == 0):
#             pixel = test_pixel

def print_final_image():
    for pixel_index in range(0,len(final_image)):
        if(pixel_index % 25 == 0):
            print()
        print(final_image[pixel_index], end="")

final_image = wrap(layers[len(layers) - 1], 1)

for layer in layers:
    for pixel in layer:
        fi_pixel_index = 0

        # print(pixel, end="") # WAYYYY too many pixels in this layer

        for pixel_final_image in final_image:
            if(pixel == "1" or pixel == "0"):
                final_image[fi_pixel_index] = pixel # what the fuck
                fi_pixel_index += 1
print_final_image()
