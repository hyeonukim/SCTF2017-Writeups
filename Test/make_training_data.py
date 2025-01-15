import os
import cv2
import utils

# create training_data folder and inside create 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 folders where
# other numbers are saved as they are in folder and 10 = '+', 11 = '-', 12 = '*'

image = cv2.imread('TEST\\1.png')
# extract the characters 
chars = utils.extract_chars(image)

for char in chars:
    # show the image
    cv2.imshow('Image', char[1])
    input = cv2.waitKey(0)
    # resize the image to 20 x 20
    resized = cv2.resize(char[1], (20,20))

    # label the image from 0 to 9 by inputing number 0 to 9 and save them
    if input >= 48 and input <= 57:
        name = str(input - 48)
        file_count = len(next(os.walk('./training_data/' + name + '/'))[2])
        cv2.imwrite('./training_data/' + str(input - 48) + '/' + str(file_count + 1) + '.png', resized)
    # label operation characters 'a' = +, 'b' = -, 'c' = * and save them
    elif input == ord('a') or input == ord('b') or input == ord('c'):
        name = str(input - ord('a') + 10)
        file_count = len(next(os.walk('./training_data/' + name + '/'))[2])
        cv2.imwrite('./training_data/' + name + '/' + str(file_count + 1) + '.png', resized)