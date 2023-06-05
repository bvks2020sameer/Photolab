import numpy as np
import cv2

photo = cv2.imread("Destroyed.jpg")
photo = cv2.resize(photo,(1200,800))




#global methods Can't be classified
def g_mean(x):
    a = np.log(x)
    return np.exp(np.mean(a))


def h_mean(x):
    sum = 0
    for i in x :
        sum += i/i
    return np.mean(sum)
#---------------------------------------------





def median(photo):
    new = np.zeros((800,1200),dtype=np.float32)
    new[0,:] = photo[0,:]
    new[799,:] = photo[799,:]
    new[:,0] = photo[:,0]
    new[:,1199] = photo[:,1199]

    for i in range(1,799):
        for j in range(1,1199):

            kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                            [photo[i-1,j],photo[i,j],photo[i+1,j]],
                            [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
            new[i,j] = np.median(kernel)
    
    return new





def mean(photo):
    new = np.zeros((800,1200),dtype=np.float32)
    new[0,:] = photo[0,:]
    new[799,:] = photo[799,:]
    new[:,0] = photo[:,0]
    new[:,1199] = photo[:,1199]

    for i in range(1,799):
        for j in range(1,1199):

            kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                            [photo[i-1,j],photo[i,j],photo[i+1,j]],
                            [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
            new[i,j] = np.mean(kernel)
    
    return new




def geo_mean(photo):
    new = np.zeros((800,1200),dtype=np.float32)
    new[0,:] = photo[0,:]
    new[799,:] = photo[799,:]
    new[:,0] = photo[:,0]
    new[:,1199] = photo[:,1199]

    for i in range(1,799):
        for j in range(1,1199):

            kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                            [photo[i-1,j],photo[i,j],photo[i+1,j]],
                            [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
            new[i,j] = g_mean(kernel)
    
    return new



def har_mean(photo):
    new = np.zeros((800,1200),dtype=np.float32)
    new[0,:] = photo[0,:]
    new[799,:] = photo[799,:]
    new[:,0] = photo[:,0]
    new[:,1199] = photo[:,1199]

    for i in range(1,799):
        for j in range(1,1199):

            kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                            [photo[i-1,j],photo[i,j],photo[i+1,j]],
                            [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
            new[i,j] = h_mean(kernel)
    
    return new



def contra_har_mean(photo,Q):
    new = np.zeros((800,1200),dtype=np.float32)
    new[0,:] = photo[0,:]
    new[799,:] = photo[799,:]
    new[:,0] = photo[:,0]
    new[:,1199] = photo[:,1199]

    for i in range(1,799):
        for j in range(1,1199):

            kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                            [photo[i-1,j],photo[i,j],photo[i+1,j]],
                            [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
            new[i,j] = (np.mean(kernel)**(Q+1))/(np.mean(kernel)**Q)
    
    return new



def min(photo,Q):
    new = np.zeros((800,1200),dtype=np.float32)
    new[0,:] = photo[0,:]
    new[799,:] = photo[799,:]
    new[:,0] = photo[:,0]
    new[:,1199] = photo[:,1199]

    for i in range(1,799):
        for j in range(1,1199):

            kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                            [photo[i-1,j],photo[i,j],photo[i+1,j]],
                            [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
            new[i,j] = np.min(kernel)
    
    return new



def max(photo,Q):
    new = np.zeros((800,1200),dtype=np.float32)
    new[0,:] = photo[0,:]
    new[799,:] = photo[799,:]
    new[:,0] = photo[:,0]
    new[:,1199] = photo[:,1199]

    for i in range(1,799):
        for j in range(1,1199):

            kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                            [photo[i-1,j],photo[i,j],photo[i+1,j]],
                            [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
            new[i,j] = np.max(kernel)
    
    return new



def mid_point(photo,Q):
    new = np.zeros((800,1200),dtype=np.float32)
    new[0,:] = photo[0,:]
    new[799,:] = photo[799,:]
    new[:,0] = photo[:,0]
    new[:,1199] = photo[:,1199]

    for i in range(1,799):
        for j in range(1,1199):

            kernel = np.array([[photo[i-1,j-1],photo[i,j-1],photo[i+1,j-1]],
                            [photo[i-1,j],photo[i,j],photo[i+1,j]],
                            [photo[i-1,j+1],photo[i,j+1],photo[i+1,j+1]]])
            new[i,j] = (np.max(kernel) + np.min(kernel))//2
    
    return new


new = median(photo)

cv2.imwrite("new.jpg",new)
disp = cv2.imread("new.jpg")
cv2.imshow('frame',disp)
cv2.waitKey(0)
cv2.destroyAllWindows()