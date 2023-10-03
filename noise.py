import numpy as np
import random
import cv2

class spatial_noise_color(object)  :

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
            noise = np.random.normal(loc=mean,scale=std_dev,size=(800,1200))
            return photo+noise
    

    
    def uniform(self,a,b):
            
            photo = self.photo
            mean = np.mean(photo)
            noise = np.zeros((800,1200),np.float32)

            for i in range(800):
                  for j in range(1200):
                        noise[i,j] = random.randrange(a,b+1)     
            
            return photo+noise
    
    
    
    def erlang(self,a,b):
            photo = self.photo
            noise = np.random.gamma(a,b,(800,1200))
            print(noise)
            return photo+noise


    def exponential(self,a):
            photo = self.photo
            noise = np.random.exponential(a,(800,1200))
            print(noise)
            return photo+noise

    def poisson(self):
            photo = self.photo
            noise = np.random.poisson(lam=np.mean(photo), size=(800,1200))
            print(noise)
            return photo + noise


