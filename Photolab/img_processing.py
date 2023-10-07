import cv2
import numpy as np


class img_processing(object):

    def __init__(self,photo,M,N) -> None:
        self.photo = photo
        self.M = M
        self.N = N

    def flatten(self) -> np.array:

        count = 0
        flattened = np.zeros((self.M*self.N))
        for i in range(self.M):
            for j in range(self.N) :
                flattened[count] = self.photo[i,j]
                count+=1
        
        return flattened
        



img = cv2.imread(r'D:\Programs\Projects\Photolab\shark.jpg',0)
img = cv2.resize(img,(300,250))
imp_pr = img_processing(img,250,300)
print(imp_pr.flatten())