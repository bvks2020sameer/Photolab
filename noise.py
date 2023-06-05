import numpy as np
import cv2

photo = cv2.imread('car.jpg')
photo = cv2.resize(photo,(1200,800))

class spatial_noise(object) :

    def __init__(self,photo) -> None:
          self.photo = photo
          return None
    

    def salt(self,cycles:int):

        photo = self.photo    
        new = np.copy(photo)
        for count in range(cycles):
                i = np.random.randint(0,800)
                j = np.random.randint(0,1200)
                
                new[i,j] = [255,255,255]
        return new   


    def pepper(self,cycles:int):

        
        photo = self.photo       
        new = np.copy(photo)
        for count in range(cycles):
                i = np.random.randint(0,800)
                j = np.random.randint(0,1200)
                
                new[i,j] = [0,0,0]
        return new  

    def salt_pepper(self,cycles:int):

        
        photo = self.photo       
        new = np.copy(photo)
        for count in range(cycles):
                i = np.random.randint(0,800)
                j = np.random.randint(0,1200)
                key = np.random.randint(0,2)
                if key == 0 : 
                    new[i,j] = [0,0,0]
                else :
                    new[i,j] = [255,255,255]
                    
        return new  


class probabilistic_noise (object):
     
    def __init__(self,photo) -> None:
          self.photo = photo
          return None
    
    def gaussian(self,std_dev):
            
            photo = self.photo
            mean = np.mean(photo)
            noise = np.zeros((800,1200), np.uint8)
            cv2.randn(noise, mean, std_dev)
            noisy_img = cv2.add(photo, noise)

            return noisy_img
         



New = spatial_noise.salt_pepper(photo,100000)

cv2.imwrite("noise.jpg",New)
new = cv2.imread("noise.jpg")
cv2.imshow("frame",new)

cv2.waitKey(0)