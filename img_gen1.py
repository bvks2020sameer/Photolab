#pip library import

import cv2
import numpy as np
from random import randint as rd
from edge import edge



from freq_filter import freq_filter



photo = cv2.imread("""D:\Programs\Photolab\car.jpg""",0)
photo = cv2.resize(photo,(1200,800))

cuttoff = 50

B = freq_filter(photo)
new1 = B.gauss_low_pass(100,5)
e = edge(new1)
new = e.sobel_avg()



color = [6,255,72]
New = []
for i in new :
    row = []
    for j in i :
            if j != 0:
                wt = j/255*10
                key = [int(color[0]*wt),int(color[1]*wt),int(color[2]*wt)]
            else:
                key = [0,0,0]

            row.append(key)

    New.append(row)


        
New = np.array(New)
        

cv2.imwrite("new.jpg",New)
disp = cv2.imread("new.jpg")
cv2.imshow('frame',disp)
cv2.waitKey(0)
cv2.destroyAllWindows()

