import numpy as np
import cv2
from optparse import OptionParser
import os
import sys

def energyRGB(image):
    return energyGray(image[:, :, 0]).astype(np.float64) + energyGray(image[:, :, 1]).astype(np.float64) + energyGray(image[:, :, 2]).astype(np.float64)

def energyGray(image):
    return abs(cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize = 3)) + abs(cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize = 3))

def find_minimum_energy(energyMap):
    matrix = energyMap.copy()
    matrix = matrix.astype(np.float64)
    width  = energyMap.shape[1]
    height = energyMap.shape[0]
    for y in xrange(1, height):
        for x in xrange(0, width):
            if (x != 0 and x + 1 != width):
                matrix[y, x] = energyMap[y, x] + min(matrix[y - 1, x - 1], matrix[y - 1, x], matrix[y - 1, x + 1])
            elif (x == 0):
                # first pixel
                matrix[y, x] = energyMap[y, x] + min(matrix[y - 1, x], matrix[y - 1, x + 1])
            else:
                # last pixel
                matrix[y, x] = energyMap[y, x] + min(matrix[y - 1, x], matrix[y - 1, x - 1])
    return matrix

def find_horizontal_seam(matrix):
    width  = matrix.shape[1]
    height = matrix.shape[0]
    min_last_column = min_num_index(matrix[:, width - 1])
    path   = [min_last_column]
    index  = 0
    for x in range(width - 1, 0, -1):
        y = path[index]
        if (y != 0 and y + 1 != height):
            next_min_index = min_num_index(matrix[y - 1 : y + 2, x - 1])
            path.append(y + next_min_index - 1)
        elif (y == 0):
            # first pixel
            next_min_index = min_num_index(matrix[y : y + 2, x - 1])
            path.append(y  + next_min_index)
        else:
            # last pixel
            next_min_index = min_num_index(matrix[y - 1 : y + 1, x - 1])
            path.append(y + next_min_index - 1)
        index += 1
    return path

def find_vertical_seam(matrix):
    width  = matrix.shape[1]
    height = matrix.shape[0]
    min_last_row = min_num_index(matrix[height - 1, :])
    path   = [min_last_row]
    index  = 0
    for y in range(height - 1, 0, -1):
        x = path[index]
        if (x != 0 and x + 1 != width):
            next_min_index = min_num_index(matrix[y - 1, x - 1 : x + 2])
            path.append(x + next_min_index - 1)
        elif (x == 0):
            # first pixel
            next_min_index = min_num_index(matrix[y - 1, x : x + 2])
            path.append(x + next_min_index)
        else:
            # last pixel
            next_min_index = min_num_index(matrix[y - 1, x - 1 : x + 1])
            path.append(x + next_min_index - 1)

        index += 1
    return path

def remove_horizontal_seam(path, color_image):
    output = cv2.resize(color_image, (color_image.shape[1], color_image.shape[0] - 1), interpolation = cv2.INTER_LINEAR)
    current_x = color_image.shape[1] - 1
    for y in range(color_image.shape[1]):
        remove_y = path[y]
        output[: remove_y, current_x] = color_image[: remove_y, current_x]
        output[remove_y :, current_x] = color_image[remove_y + 1 :, current_x]
        current_x = current_x - 1
    return output

def remove_vertical_seam(path, color_image):
    output = cv2.resize(color_image, (color_image.shape[1] - 1, color_image.shape[0]), interpolation = cv2.INTER_LINEAR)
    current_y = color_image.shape[0] - 1
    for x in range(color_image.shape[0]):
        remove_x = path[x]
        output[current_y, 0 : remove_x] = color_image[current_y, 0 : remove_x]
        output[current_y, remove_x :] = color_image[current_y, remove_x + 1 :]
        current_y = current_y - 1
    return output

def add_horizontal_seam(path, color_image):
    output = cv2.resize(color_image, (color_image.shape[1], color_image.shape[0] + 1), interpolation = cv2.INTER_LINEAR)
    current_x = color_image.shape[1] - 1
    for y in range(color_image.shape[1]):
        add_y = path[y]
        output[0 : add_y, current_x] = color_image[0 : add_y, current_x]
        output[add_y, current_x] = [255, 255, 255]
        output[add_y + 1:, current_x] = color_image[add_y :, current_x]
        current_x = current_x - 1
    return output

def add_vertical_seam(path, color_image):
    output = cv2.resize(color_image, (color_image.shape[1] + 1, color_image.shape[0]), interpolation = cv2.INTER_LINEAR)
    current_y = color_image.shape[0] - 1
    for x in range(color_image.shape[0]):
        add_x = path[x]
        output[current_y, 0 : add_x] = color_image[current_y, 0 : add_x]
        output[current_y, add_x] = [255, 255, 255]
        output[current_y, add_x + 1 :] = color_image[current_y, add_x :]
        current_y = current_y - 1
    return output

def insert_avg(output):
    for x in range(output.shape[0]):
        for y in range(output.shape[1] - 1):
            if np.any(output[x, y] == [255, 255, 255]):
                output[x, y] = output[x, y + 1] / 2 + output[x, y - 1] / 2
    return output

def min_num_index(nums):
    index = list(nums).index(min(nums))
    return index

def resize(img, new_width, new_height):
    remove_width  = img.shape[1] - new_width
    remove_height = img.shape[0] - new_height
    add_width     = new_width - img.shape[1]
    add_height    = new_height - img.shape[0]

    print "Oringal Width: " + str(img.shape[1]) + " Original Height: " + str(img.shape[0])
    print "New Width: "+ str(new_width) + " New height: " + str(new_height)

    output = img.copy()
    for i in range(remove_width):
        energy = energyRGB(output)
        cost = find_minimum_energy(energy)
        path = find_vertical_seam(cost)
        output = remove_vertical_seam(path, output)

    for i in range(remove_height):
        energy = energyRGB(output)
        cost = find_minimum_energy(energy)
        path = find_horizontal_seam(cost)
        output = remove_horizontal_seam(path, output)

    for i in range(add_width):
        energy = energyRGB(output)
        cost = find_minimum_energy(energy)
        path = find_vertical_seam(cost)
        output = add_vertical_seam(path, output)

    if (add_width > 0):
        output = insert_avg(output)

    return output

def main():
    usage = "usage: %prog -i [input image] -r [width] [height] -o [output name] \n"
    parser = OptionParser(usage=usage)
    parser.add_option("-i", "--image", dest="input_image")
    parser.add_option("-r", "--resolution", dest="resolution", nargs=2)
    parser.add_option("-o", "--output", dest="output")
    (options, args) = parser.parse_args()

    if not options.input_image or not options.resolution or not options.output:
        print "Incorrect Options!"
        sys.exit(2)

    input_image = options.input_image
    resolution = (int(options.resolution[0]), int(options.resolution[1]))
    output = options.output

    image = cv2.imread(input_image)
    new_image = resize(image, resolution[0], resolution[1])
    cv2.imwrite(output, new_image)
    print "Completed " + output

if __name__ == "__main__":
    main()
