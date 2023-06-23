import numpy as np
import cv2

photo = cv2.imread("noise.jpg",0)
photo = cv2.resize(photo,(1200,800))




#global methods Can't be classified
def g_mean(x):
    a = np.log(x)
    return np.exp(np.mean(a))


def h_mean(x):
    sum = 0
    for i in x :
        sum += 1/i
    return np.mean(sum)
#---------------------------------------------



class img_restore(object):



    def __init__(self,photo,M,N) -> None:
        
        self.photo = photo
        self.M = M
        self.N = N
        return None

    def median(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        new[0,:] = photo[0,:]
        new[M-1,:] = photo[M-1,:]
        new[:,0] = photo[:,0]
        new[:,N-1] = photo[:,N-1]

        for i in range(1,M-1):
            for j in range(1,N-1):

                kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                                [photo[i-1,j],photo[i,j],photo[i+1,j]],
                                [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
                new[i,j] = np.median(kernel)
        
        return new





    def mean(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        new[0,:] = photo[0,:]
        new[M-1,:] = photo[M-1,:]
        new[:,0] = photo[:,0]
        new[:,N-1] = photo[:,N-1]

        for i in range(1,M-1):
            for j in range(1,N-1):

                kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                                [photo[i-1,j],photo[i,j],photo[i+1,j]],
                                [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
                new[i,j] = np.mean(kernel)
        
        return new




    def geo_mean(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        new[0,:] = photo[0,:]
        new[M-1,:] = photo[M-1,:]
        new[:,0] = photo[:,0]
        new[:,N-1] = photo[:,N-1]

        for i in range(1,M-1):
            for j in range(1,N-1):

                kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                                [photo[i-1,j],photo[i,j],photo[i+1,j]],
                                [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
                new[i,j] = g_mean(kernel)
        
        return new


    #not working
    def har_mean(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        new[0,:] = photo[0,:]
        new[M-1,:] = photo[M-1,:]
        new[:,0] = photo[:,0]
        new[:,N-1] = photo[:,N-1]

        for i in range(1,M-1):
            for j in range(1,N-1):

                kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                                [photo[i-1,j],photo[i,j],photo[i+1,j]],
                                [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
                new[i,j] = h_mean(kernel)
        
        return new



    def contra_har_mean(self,Q):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        new[0,:] = photo[0,:]
        new[M-1,:] = photo[M-1,:]
        new[:,0] = photo[:,0]
        new[:,N-1] = photo[:,N-1]

        for i in range(1,M-1):
            for j in range(1,N-1):

                kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                                [photo[i-1,j],photo[i,j],photo[i+1,j]],
                                [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
                new[i,j] = (np.mean(kernel)**(Q+1))/(np.mean(kernel)**Q)
        
        return new



    def min(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        new[0,:] = photo[0,:]
        new[M-1,:] = photo[M-1,:]
        new[:,0] = photo[:,0]
        new[:,N-1] = photo[:,N-1]

        for i in range(1,M-1):
            for j in range(1,N-1):

                kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                                [photo[i-1,j],photo[i,j],photo[i+1,j]],
                                [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
                new[i,j] = np.min(kernel)
        
        return new



    def max(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float32)
        new[0,:] = photo[0,:]
        new[M-1,:] = photo[M-1,:]
        new[:,0] = photo[:,0]
        new[:,N-1] = photo[:,N-1]

        for i in range(1,M-1):
            for j in range(1,N-1):

                kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                                [photo[i-1,j],photo[i,j],photo[i+1,j]],
                                [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
                new[i,j] = np.max(kernel)
        
        return new


    
    def mid_point(self):

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M,N),dtype=np.float64)
        new[0,:] = photo[0,:]
        new[M-1,:] = photo[M-1,:]
        new[:,0] = photo[:,0]
        new[:,N-1] = photo[:,N-1]

        for i in range(1,M-1):
            for j in range(1,N-1):

                kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                                [photo[i-1,j],photo[i,j],photo[i+1,j]],
                                [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
                new[i,j] = (np.max(kernel) + np.min(kernel))//2
        
        return new


new = img_restore(photo,800,1200).har_mean()

cv2.imwrite("new.jpg",new)
disp = cv2.imread("new.jpg")
cv2.imshow('frame',disp)
cv2.waitKey(0)
cv2.destroyAllWindows()