from freq_filter import freq_filter as F
import cv2
import numpy as np

photo = cv2.imread("car.jpg",0)
photo = cv2.resize(photo,(1200,800))




def double_thresholding(photo,th1:int,th2:int):
    
    new = np.zeros((800,1200),dtype= np.float32)

    for i in range(0,800):
        for j in range(0,1200):
            if photo[i,j] >= th1 and photo[i,j] <= th2 :
                new[i,j] = photo[i,j]
            else :
                new[i,j] =0

    return new





def sobelx(photo):

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




def sobely(photo):

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






B = F(photo)
#new = B.ideal_low_pass(80)
#new = double_thresholding(photo,100,255)
#new = B.ideal_high_pass(90)
new = sobely(photo)
print(np.shape(new))
cv2.imwrite("edge.jpg",new)
disp = cv2.imread("edge.jpg")
cv2.imshow("frame",disp)
cv2.waitKey(0)

