import cv2
import utils

image = cv2.imread('TEST\\1.png', cv2.IMREAD_COLOR)
blue = utils.get_chars(image.copy(), utils.BLUE)
green = utils.get_chars(image.copy(), utils.GREEN)
red = utils.get_chars(image.copy(), utils.RED)

cv2.imshow('Image Gray(BLUE)', blue)
cv2.waitKey(0)
cv2.imshow('Image Gray(GREEN)', green)
cv2.waitKey(0)
cv2.imshow('Image Gray(RED)', red)
cv2.waitKey(0)