import numpy as np

class edge(object):

    def __init__(self,photo,M,N):
        self.photo = photo
        self.M = M
        self.N = N
        return None

    def double_thresholding(self,th1:int,th2:int):
        photo = self.photo
        
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype= np.float32)

        for i in range(0,M):
            for j in range(0,N):
                if photo[i,j] >= th2:
                    new[i,j] = 255
                elif photo[i,j] >= th1 and photo[i,j] <= th2 :
                    new[i,j] = 127
                else :
                    new[i,j] =0

        return new





    def sobelx(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        temp = np.zeros((M+2,N+2),dtype=np.float32)


        temp[0,:] = 0
        temp[:, 0] = 0
        temp[M+1,:] = 0
        temp[:, N+1] = 0
        temp[1:M+1,1:N+1] = photo

        op = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                        
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

        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        temp = np.zeros((M+2,N+2),dtype=np.float32)


        temp[0,:] = 0
        temp[:, 0] = 0
        temp[M+1,:] = 0
        temp[:, N+1] = 0
        temp[1:M+1,1:N+1] = photo       
       

        op = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                
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
        M = self.M
        N = self.N
        mag = np.zeros((M,N),dtype=np.float32)
        e = edge(photo,M,N)
        gx = e.sobelx()
        gy = e.sobely()

        for i in range(M):
            for j in range(N):
                mag[i,j] = np.sqrt(gx[i,j]**2 + gy[i,j]**2)

        return mag    



    def gradientation(self):
        
        photo = self.photo
        M = self.M
        N = self.N

        
        mag = np.zeros((M,N),dtype=np.float32)
        ang = np.zeros((M,N),dtype=np.float32)
        filtered = np.zeros((M,N),dtype=np.float32)
        e = edge(photo)

        gx = e.sobelx()
        gy = e.sobely()

        for i in range(M):
            for j in range(N):
                mag[i,j] = np.sqrt(gx[i,j]**2 + gy[i,j]**2)
                ang[i,j] = np.arctan2(gy[i,j],gx[i,j])

        for i in range(1,M-1):
            for j in range(1,N-1):
                
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


    def prewits_horizontal(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        temp = np.zeros((M+2,N+2),dtype=np.float32)


        temp[0,:] = 0
        temp[:, 0] = 0
        temp[M+1,:] = 0
        temp[:, N+1] = 0
        temp[1:M+1,1:N+1] = photo

        op = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                        
                kernel = np.array([[temp[i-1,j-1],temp[i,j-1],temp[i+1,j-1]],
                            [temp[i-1,j],temp[i,j],temp[i+1,j]],
                            [temp[i-1,j+1],temp[i,j+1],temp[i+1,j+1]]])
                
                sum = 0

                for x_key in range(3):
                    for y_key in range(3) :
                        sum += op[x_key,y_key]*kernel[x_key,y_key]

                new[i-1,j-1] = sum
                        
        return  new

    def prewits_vertical(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        temp = np.zeros((M+2,N+2),dtype=np.float32)


        temp[0,:] = 0
        temp[:, 0] = 0
        temp[M+1,:] = 0
        temp[:, N+1] = 0
        temp[1:M+1,1:N+1] = photo

        op = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                        
                kernel = np.array([[temp[i-1,j-1],temp[i,j-1],temp[i+1,j-1]],
                            [temp[i-1,j],temp[i,j],temp[i+1,j]],
                            [temp[i-1,j+1],temp[i,j+1],temp[i+1,j+1]]])
                
                sum = 0

                for x_key in range(3):
                    for y_key in range(3) :
                        sum += op[x_key,y_key]*kernel[x_key,y_key]

                new[i-1,j-1] = sum
                        
        return  new


    def roberts45(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        temp = np.zeros((M+2,N+2),dtype=np.float32)


        temp[0,:] = 0
        temp[:, 0] = 0
        temp[M+1,:] = 0
        temp[:, N+1] = 0
        temp[1:M+1,1:N+1] = photo

        op = np.array([[-1,0,],[0,1]])
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                        
                kernel = np.array([[temp[i-1,j-1],temp[i,j-1],temp[i+1,j-1]],
                            [temp[i-1,j],temp[i,j],temp[i+1,j]],
                            [temp[i-1,j+1],temp[i,j+1],temp[i+1,j+1]]])
                
                sum = 0

                for x_key in range(2):
                    for y_key in range(2) :
                        sum += op[x_key,y_key]*kernel[x_key,y_key]

                new[i-1,j-1] = sum
                        
        return  new


    def roberts135(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        temp = np.zeros((M+2,N+2),dtype=np.float32)


        temp[0,:] = 0
        temp[:, 0] = 0
        temp[M+1,:] = 0
        temp[:, N+1] = 0
        temp[1:M+1,1:N+1] = photo

        op = np.array([[1,0,],[0,-1]])
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                        
                kernel = np.array([[temp[i-1,j-1],temp[i,j-1],temp[i+1,j-1]],
                            [temp[i-1,j],temp[i,j],temp[i+1,j]],
                            [temp[i-1,j+1],temp[i,j+1],temp[i+1,j+1]]])
                
                sum = 0

                for x_key in range(2):
                    for y_key in range(2) :
                        sum += op[x_key,y_key]*kernel[x_key,y_key]

                new[i-1,j-1] = sum
                        
        return  new
    


