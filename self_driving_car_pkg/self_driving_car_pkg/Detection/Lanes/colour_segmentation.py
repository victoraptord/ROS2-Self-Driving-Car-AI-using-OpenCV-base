import numpy as np
import cv2 as cv
import tensorflow as tf

def clr_segment(hls,lower_range, uper_range):
    mask_in_range = cv.inRange(hls, lower_range, upper_range)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
    mask_dilated = cv.morphologyEx(mask_in_range, cv.MORPH_DILATE, kernel)
    return mask_dilated

