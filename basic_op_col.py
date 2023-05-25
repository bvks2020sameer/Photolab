import cv2
import numpy as np
from time import *
from os import system as sys


photo = cv2.imread("D:\Programs\Photolab\shark.jpg",-1)
photo = cv2.resize(photo,(1200,800))



def invert (photo):
    new = []
    avg = np.average(photo)
    for i in photo :
        row = []
        for j in i :
           row.append(255-j)
        new.append(row)

    new = np.array(new)

    return new


def col_slice_mask (photo,offr1: 'int', offr2: 'int',offg1: 'int', offg2: 'int',offb1: 'int', offb2: 'int' ):
    new = []
    avg = np.average(photo)
    for i in photo :
        row = []
        for j in i :
            pix = []
            if j[0] >= offb1 and j[0] <= offb2 :
                pix.append(j[0])
            else :
                pix.append(0)
            if j[1] >= offg1 and j[1] <= offg2 :
                pix.append(j[1])
            else :
                pix.append(0)
            if j[2] >= offr1 and j[2] <= offr2 :
                pix.append(j[2])
            else :
                pix.append(0)

            row.append(pix)

        new.append(row)

    new = np.array(new)

    return new



def col_slice_bg (photo,offr1: 'int', offr2: 'int',offg1: 'int', offg2: 'int',offb1: 'int', offb2: 'int' ):
    new = []
    avg = np.average(photo)
    for i in photo :
        row = []
        for j in i :
            pix = []
            if j[0] >= offb1 and j[0] <= offb2 :
                pix.append(255)
            else :
                pix.append(j[0])
            if j[1] >= offg1 and j[1] <= offg2 :
                pix.append(255)
            else :
                pix.append(j[1])
            if j[2] >= offr1 and j[2] <= offr2 :
                pix.append(255)
            else :
                pix.append(j[2])

            row.append(pix)

        new.append(row)

    new = np.array(new)

    return new



def col_threshold (photo,offr:'int',offg:'int',offb:'int'):
    new = []
    avg = np.average(photo)
    for i in photo :
        row = []
        for j in i :
            pix = []
            if j[0] >= offb:
                pix.append(255)
            else :
                pix.append(0)
            if j[1] >= offg:
                pix.append(255)
            else :
                pix.append(0)
            if j[2] >= offr:
                pix.append(255)
            else :
                pix.append(0)
            row.append(pix)
        new.append(row)

    new = np.array(new)

    return new

def col_threshold_bg (photo,offr:'int',offg:'int',offb:'int'):
    new = []
    avg = np.average(photo)
    for i in photo :
        row = []
        for j in i :
            pix = []
            if j[0] >= offb:
                pix.append(255)
            else :
                pix.append(j[0])
            if j[1] >= offg:
                pix.append(255)
            else :
                pix.append(j[1])
            if j[2] >= offr:
                pix.append(255)
            else :
                pix.append(j[2])
            row.append(pix)
        new.append(row)

    new = np.array(new)

    return new

def col_threshold_mask (photo,offr:'int',offg:'int',offb:'int'):
    new = []
    avg = np.average(photo)
    for i in photo :
        row = []
        for j in i :
            pix = []
            if j[0] >= offb:
                pix.append(j[0])
            else :
                pix.append(0)
            if j[1] >= offg:
                pix.append(j[1])
            else :
                pix.append(0)
            if j[2] >= offr:
                pix.append(j[2])
            else :
                pix.append(0)
            row.append(pix)
        new.append(row)

    new = np.array(new)

    return new



new = col_slice_bg(photo,0,150,150,0,0,150)
print(np.shape(new))
cv2.imwrite("color.jpg",new)
disp = cv2.imread("color.jpg")
cv2.imshow('frame',disp)
cv2.waitKey(0)
cv2.destroyAllWindows