# @author : Bhamidipati Venkatakrishnasameer
# @ param : Photo in numpy matrix format
# @return : Photo in matrix format


import cv2
import numpy as np


class basic_bw(object):

    def __init__(self, photo) -> None:
        self.photo = photo

    def gray_slice_mask(self, off1: 'int', off2: 'int'):

        photo = self.photo
        new = []
        avg = np.average(photo)
        for i in photo:
            row = []
            for j in i:
                if j >= off1 and j <= off2:
                    row.append(j)
                else:
                    row.append(0)
            new.append(row)

        new = np.array(new)

        return new

    def threshold_mask(self, off: 'int'):

        photo = self.photo
        new = []
        avg = np.average(photo)
        for i in photo:
            row = []
            for j in i:
                if j >= off:
                    row.append(j)
                else:
                    row.append(0)
            new.append(row)

        new = np.array(new)

        return new

    def gray_slice(self, off1: 'int', off2: 'int'):

        photo = self.photo
        new = []
        avg = np.average(photo)
        for i in photo:
            row = []
            for j in i:
                if j >= off1 and j <= off2:
                    row.append(255)
                else:
                    row.append(0)
            new.append(row)

        new = np.array(new)

        return new

    def threshold(self, off: 'int'):

        photo = self.photo
        new = []
        avg = np.average(photo)
        for i in photo:
            row = []
            for j in i:
                if j >= off:
                    row.append(255)
                else:
                    row.append(0)
            new.append(row)

        new = np.array(new)

        return new

    def gray_slice_bg(self, off1: 'int', off2: 'int'):

        photo = self.photo
        new = []
        avg = np.average(photo)
        for i in photo:
            row = []
            for j in i:
                if j >= off1 and j <= off2:
                    row.append(255)
                else:
                    row.append(j)
            new.append(row)

        new = np.array(new)

        return new

    def edge_detect(self, sigma: float) -> np.ndarray:

        photo = self.photo
        new = []
        blur = cv2.GaussianBlur(photo, [49, 49], sigma);
        gx = cv2.Sobel(photo, cv2.CV_64F, 1, 0)
        gy = cv2.Sobel(photo, cv2.CV_64F, 0, 1)
        mag, theta = cv2.cartToPolar(gx, gy)
        max_mag = np.max(mag)
        new = cv2.Canny(blur, max_mag * 0.04, max_mag * 0.09)
        return new

    def threshold_bg(self, off: 'int') -> np.ndarray:

        photo = self.photo
        new = []
        avg = np.average(photo)
        for i in photo:
            row = []
            for j in i:
                if j >= off:
                    row.append(255)
                else:
                    row.append(j)
            new.append(row)

        new = np.array(new)

        return new

    def invert(self):

        photo = self.photo
        new = []
        avg = np.average(photo)
        for i in photo:
            row = []
            for j in i:
                row.append(255 - j)
                new.append(row)

        new = np.array(new)

        return new

    def __del__(self):
        pass
