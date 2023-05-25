#pip library import

import cv2
import numpy as np
from random import randint as rd
import subprocess

#
from basic_bw import basic_bw



photo = cv2.imread("""D:\Programs\Photolab\shark.jpg""",0)
photo = cv2.resize(photo,(1200,800))





#B = basic_bw(photo)
#new = B.edge_detect(1.5)
photo = cv2.medianBlur(photo,5)
new = cv2.Sobel(photo,cv2.CV_64F,1,1)
new = cv2.Sobel(new,cv2.CV_64F,1,1)



New = []
count = 0

for i in new :
    
        row = []
        
        if count % 150 == 0 :
                color = [rd(0,255),rd(0,255),rd(0,170)]
            

        for j in i :

        
            if j != 0:
                key = [color[0],color[1],color[2]]
            else:
                key = [30,10,0]

                
            row.append(key)
        
        New.append(row)
        count += 1
        

New = np.array(New)
        

cv2.imwrite("new.jpg",New)
disp = cv2.imread("new.jpg")
cv2.imshow('frame',disp)
cv2.waitKey(0)
cv2.destroyAllWindows()

