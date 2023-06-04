import numpy as np

class edge(object):

    def __init__(self,photo):
        self.photo = photo
        return None

    def double_thresholding(self,th1:int,th2:int):
        photo = self.photo
        
        new = np.zeros((800,1200),dtype= np.float32)

        for i in range(0,800):
            for j in range(0,1200):
                if photo[i,j] >= th2:
                    new[i,j] = 255
                elif photo[i,j] >= th1 and photo[i,j] <= th2 :
                    new[i,j] = 127
                else :
                    new[i,j] =0

        return new





    def sobelx(self):

        photo = self.photo

        new = np.zeros((800,1200),dtype=np.float32)
        temp = np.zeros((802,1202),dtype=np.float32)


        temp[0,:] = 0
        temp[:, 0] = 0
        temp[801,:] = 0
        temp[:, 1201] = 0
        temp[1:801,1:1201] = photo

        op = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        
        for i in range(1,801):
            for j in range(1,1201):
                        
                kernel = np.array([[temp[i-1,j-1],temp[i,j-1],temp[i+1,j-1]],
                            [temp[i-1,j],temp[i,j],temp[i+1,j]],
                            [temp[i-1,j+1],temp[i,j+1],temp[i+1,j+1]]])
                
                sum = 0

                for x_key in range(3):
                    for y_key in range(3) :
                        sum += op[x_key,y_key]*kernel[x_key,y_key]

                new[i-1,j-1] = sum
            
            
            
        return  new




    def sobely(self):

        photo = self.photo

        new = np.zeros((800,1200),dtype=np.float32)
        temp = np.zeros((802,1202),dtype=np.float32)


        temp[0,:] = 0
        temp[:, 0] = 0
        temp[801,:] = 0
        temp[:, 1201] = 0
        temp[1:801,1:1201] = photo

        op = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
        
        for i in range(1,801):
            for j in range(1,1201):
                
                kernel = np.array([[temp[i-1,j-1],temp[i,j-1],temp[i+1,j-1]],
                            [temp[i-1,j],temp[i,j],temp[i+1,j]],
                            [temp[i-1,j+1],temp[i,j+1],temp[i+1,j+1]]])
                
                sum = 0

                for x_key in range(3):
                    for y_key in range(3) :
                        sum += op[x_key,y_key]*kernel[x_key,y_key]

                new[i-1,j-1] = sum
            
                
            
            
        return  new

    def sobel_avg(self):
        
        photo = self.photo
        mag = np.zeros((800,1200),dtype=np.float32)
        e = edge(photo)
        gx = e.sobelx()
        gy = e.sobely()

        for i in range(800):
            for j in range(1200):
                mag[i,j] = np.sqrt(gx[i,j]**2 + gy[i,j]**2)

        return mag    


    def gradientation(self):
        
        photo = self.photo
        mag = np.zeros((800,1200),dtype=np.float32)
        ang = np.zeros((800,1200),dtype=np.float32)
        filtered = np.zeros((800,1200),dtype=np.float32)
        e = edge(photo)

        gx = e.sobelx()
        gy = e.sobely()

        for i in range(800):
            for j in range(1200):
                mag[i,j] = np.sqrt(gx[i,j]**2 + gy[i,j]**2)
                ang[i,j] = np.arctan2(gy[i,j],gx[i,j])

        for i in range(1,799):
            for j in range(1,1199):
                
                if ang[i,j] < np.pi/8 :
                    n1 = mag[i-1,j]
                    n2 = mag[i+1,j]
                    if mag[i,j]>=n1 and mag[i,j]>=n2:
                        filtered[i,j] = mag[i,j]
                    else :
                        filtered[i,j] = 0
                

                elif ang[i,j] >= np.pi/8 and ang[i,j] < (np.pi/8 + np.pi/4):

                    n1 = mag[i-1,j-1]
                    n2 = mag[i+1,j+1]
                    if mag[i,j]>=n1 and mag[i,j]>=n2:
                        filtered[i,j] = mag[i,j]
                    else :
                        filtered[i,j] = 0


                elif ang[i,j] >= (np.pi/8+np.pi/4) and ang[i,j] < (np.pi/8 + np.pi/2):

                    n1 = mag[i,j-1]
                    n2 = mag[i,j+1]
                    if mag[i,j]>=n1 and mag[i,j]>=n2:
                        filtered[i,j] = mag[i,j]
                    else :
                        filtered[i,j] = 0

                
                elif ang[i,j] >= (np.pi/2+np.pi/8) and ang[i,j] < (np.pi/8 + 3*np.pi/4):

                    n1 = mag[i+1,j+1]
                    n2 = mag[i-1,j-1]
                    if mag[i,j]>=n1 and mag[i,j]>=n2:
                        filtered[i,j] = mag[i,j]
                    else :
                        filtered[i,j] = 0

                
                elif ang[i,j] >= (np.pi/8 + 3*np.pi/4) and ang[i,j] < (np.pi/8 + np.pi):

                    n1 = mag[i+1,j+1]
                    n2 = mag[i-1,j-1]
                    if mag[i,j]>=n1 and mag[i,j]>=n2:
                        filtered[i,j] = mag[i,j]
                    else :
                        filtered[i,j] = 0
                
        return filtered





