from textwrap import wrap

def print_layer(layer):
    for pixel_index in range(0, len(layer)):
        if(pixel_index % 4 == 0 ):#and pixel_index != 0):
            print()
        print(layer[pixel_index], end="")

# start from bottom layer then iterate through every layer, keep a current image array that is the current image and update that
# initialize current image with bottom layer or with 2s (list comprehension)
current_image = [2 for i in range(0, 16)]
layers = wrap(open("day8p2_test_input").readline(), 2)

for layer_index in range(len(layers)-1, 0, -1):
    # iter backwards through layers
    current_layer = layers[layer_index]

    print_layer(current_layer)

    for pixel_index in range(0, len(current_layer)):
        current_pixel = current_layer[pixel_index]
        if(current_pixel == "0" or current_pixel == "1"):
            current_image[pixel_index] = current_pixel


print("\n")
for pixel_index in range(0,len(current_image)):
    if(pixel_index % 4 == 0 and pixel_index != 0):
        print()
    print(current_image[pixel_index], end="")
    # print("X" if current_image[pixel_index] == "0" else " ", end="")
