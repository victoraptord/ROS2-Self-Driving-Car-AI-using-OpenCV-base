import numpy as np
import cv2 as cv
import tensorflow as tf

#White Regions Range
hue_l = 0
lit_l = 225
sat_l = 0

#Yellow Regions Range
hue_l_y = 30
hue_h_y = 33
lit_l_y = 160
sat_l_y = 0

def maskextract():
    mask    = color_segment(hls,(hue_l ,lit_l, sat_l), (255,255,255))
    mask_y  = color_segment(hls,(hue_l_y, lit_l_y, sat_l_y), (hue_h_y, 255, 255))

    mask = mask != 0
    dst = src*(mask_[:,:,None].astype(src.dtype))

    mask_y = mask_y != 0
    dst_Y = src*(mask_y_[:,:,None].astype(src.dtype))

    cv.imshow('white_regions',dst)
    cv.imshow('yellow_regions', dst_Y)
def on_hue_low_change(val):
    global hue_l
    hue_l = val
    maskextract()
def on_lit_low_change(val):
    global lit_l
    lit_l = val
    maskextract()
def on_sat_low_change(val):
    global sat_l
    sat_l = val
    maskextract()
def on_hue_high_y_change(val):
    global hue_h_y
    hue_h_y = val
    maskextract()
def on_hue_low_y_change(val):
    global hue_l_y
    hue_l_y = val
    maskextract()
def on_lit_low_y_change(val):
    global lit_l_y
    lit_l_y = val
    maskextract()
def on_sat_low_y_change(val):
    global sat_l_y
    sat_l_y = val
    maskextract()

cv.namedWindow("white_regions")
cv.namedWindow("yellow_regions")

cv.createTrackbar("Hue_L", "white_regions",hue_l,255,on_hue_low_change)
cv.createTrackbar("Lit_L", "white_regions",lit_l,255,on_lit_low_change)
cv.createTrackbar("Sat_L", "white_regions",sat_l,255,on_sat_low_change)

cv.createTrackbar("Hue_L_Y", "yellow_regions",hue_l_y,255,on_hue_low_y_change)
cv.createTrackbar("Hue_H_Y", "yellow_regions",hue_h_y,255,on_hue_high_y_change)
cv.createTrackbar("Lit_L_Y", "yellow_regions",lit_l_y,255,on_lit_low_y_change)
cv.createTrackbar("Sat_L_Y", "yellow_regions",sat_l_y,255,on_sat_low_y_change)

def clr_segment(hls,lower_range, upper_range):
    mask_in_range = cv.inRange(hls, lower_range, upper_range)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
    mask_dilated = cv.morphologyEx(mask_in_range, cv.MORPH_DILATE, kernel)
    return mask_dilated

def segment_lanes(frame, min_area):
    hls = cv.cvtColor(frame, cv.COLOR_BGR2HLS)

    #Segmenting White Regions
    white_regions = clr_segment(hls, np.array([hue_l,lit_l,sat_l]), np.array([255,255,255]))
    yellow_regions = clr_segment(hls, np.array([hue_l_y, lit_l_y, sat_l_y]), np.array([hue_h_y, 255, 255]))

    cv.imshow("white_regions", white_regions)
    cv.imshow("yellow_regions", yellow_regions)

    cv.waitKey(1)