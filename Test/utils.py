import cv2
import numpy as np 
import re

BLUE = 0
GREEN = 1
RED = 2

# turn the characters that have our image into WHITE and others into BLACK
def get_chars(image, color):
    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3

    # turn the other colors into BLACK
    c = image[:, :, other_1] == 255
    image[c] = [0, 0, 0]
    c = image[:, :, other_2] == 255
    image[c] = [0, 0, 0]

    # if our color is less than AA in hexcode, turn into BLACK
    c = image[:, :, color] < 170
    image[c] = [0, 0, 0]

    # turn our color into WHITE
    c = image[:, :, color] != 0
    image[c] = [255, 255, 255]

    return image

# extract the characters from the image
def extract_chars(image):
    chars = []
    colors = [BLUE, GREEN, RED]

    for color in colors:
        image_from_one_color = get_chars(image.copy(), color)
        # change the image to gray to apply thresholding
        image_gray = cv2.cvtColor(image_from_one_color, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image_gray, 127, 255, 0)
        # find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours: 
            # if image size is bigger than 50, we should extract them
            area = cv2.contourArea(contour)
            if area > 50:
                x, y, width, height = cv2.boundingRect(contour)
                # getting roi using boundingRect
                roi = image_gray[y:y + height, x:x + width]
                chars.append((x, roi))
        
        # sort the array by x value so it reads from left to right
        chars = sorted(chars, key=lambda char: char[0])
    return chars
    
# make specific image into (20x20) size
def resize20(image):
    resized = cv2.resize(image, (20, 20))
    return resized.reshape(-1, 400).astype(np.float32)

# we must first remove the 0s that come before (ex: 0032)
def remove_first_0(string):
    temp = []
    # add the operation into temp
    for i in string:
        if i == '+' or i == '-' or i == '*':
            temp.append(i)
    
    # split the string into 2 numbers (ex: 003 + 74 -> [003, 74])
    split = re.split('\*|\+|-', string)
    i = 0
    temp_count = 0
    result = ''
    for a in split:
        # remove the 0s on left
        a = a.lstrip('0')
        # edge case if it's all '0'
        if a == '':
            a = '0'
        result += a
        # updating the result
        if i < len(split) - 1:
            result += temp[temp_count]
            temp_count = temp_count + 1
        i = i + 1
    return result