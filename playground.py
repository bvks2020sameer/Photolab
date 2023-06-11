import numpy as np
import cv2
import math
from noise import probabilistic_noise as p

photo = cv2.imread("""D:\Programs\Photolab\car.jpg""",0)
photo = cv2.resize(photo,(1200,800))

def motion_process( motion_angle):
    PSF = np.zeros((800,1200),dtype=np.float32)
    center_position = (800 - 1) / 2
    print(center_position)

    slope_tan = math.tan(motion_angle * math.pi / 180)
    slope_cot = 1 / slope_tan
    if slope_tan <= 1:
        for i in range(15):
            offset = round(i * slope_tan)  # ((center_position-i)*slope_tan)
            PSF[int(center_position + offset), int(center_position - offset)] = 1
        return PSF / PSF.sum()  # Normalize the luminance of the point spread function
    else:
        for i in range(15):
            offset = round(i * slope_cot)
            PSF[int(center_position - offset), int(center_position + offset)] = 1
        return PSF / PSF.sum()

def make_blurred(input, PSF, eps):
    input_fft = np.fft.fft2(input)  # Take the Fourier transform of a two-dimensional array
    PSF_fft = np.fft.fft2(PSF) + eps
    blurred = np.fft.ifft2(input_fft * PSF_fft)
    blurred = np.abs(np.fft.fftshift(blurred))
    return blurred

def wiener(input, PSF, eps, K=0.01):  # Wiener filtering，K=0.01
    input_fft = np.fft.fft2(input)
    PSF_fft = np.fft.fft2(PSF) + eps
    PSF_fft_1 = np.conj(PSF_fft) / (np.abs(PSF_fft) ** 2 + K)
    result = np.fft.ifft2(input_fft * PSF_fft_1)
    result = np.abs(np.fft.fftshift(result))
    return result

psf = motion_process(20)
blur = make_blurred(photo,psf,p(photo).exponential(10))
New = wiener(blur,psf,p(photo).exponential(10))
cv2.imwrite("new.jpg",New)
disp = cv2.imread("new.jpg")
cv2.imshow('frame',disp)
cv2.waitKey(0)
cv2.destroyAllWindows()