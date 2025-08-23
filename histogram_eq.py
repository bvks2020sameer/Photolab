import cv2
import numpy as np

# Correct way to read the image
img = cv2.imread(r"D:\Programs\Projects\Photolab\fish.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (1080, 720))


# cv2.imshow("Car Image", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

class histo_eq(object):

    def __init__(self,photo,M,N):
        self.photo = photo
        self.M = M
        self.N = N
        return None
    
    # Pixel Frequency Counter

    def __pix_freq(self) -> dict:
        
        photo = self.photo
        arr = photo.flatten()
        pix_freq_dist = dict()
        
        for i in arr:
            if i not in pix_freq_dist:
                pix_freq_dist[i] = 1
            else:
                pix_freq_dist[i] += 1

        pix_freq_dist = dict(sorted(pix_freq_dist.items()))
        return pix_freq_dist
    

    # Global Histogram equalization

    def global_hist_eq(self,photo : np.array =None , M:int = None, N:int = None ) -> np.array:
        
        if M is None:
            M = self.M
        
        if N is None:
            N =self.N

        if photo is None:
            photo = self.photo

        new = np.zeros((M,N),dtype=np.uint8)

        pix_freq_dist = self.__pix_freq()
        
        #Cummulative frequency and mapping

        cum_sum = 0
        cdf = dict()

        for k,v in pix_freq_dist.items():
            cum_sum += v
            cdf[k] = cum_sum

        
        min_cdf_freq = min(cdf.values())
        
        for i in cdf :
            cdf[i] = np.uint8(np.ceil((cdf[i] - min_cdf_freq)/(M*N - min_cdf_freq) * 255))
        
        pix_freq_dist = cdf

        for i in range(0,M):
            for j in range(0,N):
                new[i,j] = pix_freq_dist[photo[i,j]]

        return new
    
    # Local histogram equalization

    def local_hist_eq(self, kernel_size):

        if kernel_size < 100:
            raise ValueError("Kernel size too low")

        photo = self.photo
        M = self.M
        N = self.N

        new = np.zeros((M, N), dtype=np.uint8)

        # 🔹 store mappings per tile
        mappings = {}

        for m in range(0, M, kernel_size):
            for n in range(0, N, kernel_size):
                kernel = photo[m:min(m+kernel_size, M), n:min(n+kernel_size, N)]
                height, width = kernel.shape

                # your existing GHE call
                kernel_eq = self.global_hist_eq(kernel, height, width)

                # 🔹 build mapping for this tile
                mapping = {}
                for orig, eq in zip(kernel.flatten(), kernel_eq.flatten()):
                    mapping[orig] = eq

                mappings[(m//kernel_size, n//kernel_size)] = mapping

                # (don’t copy kernel back here — we’ll interpolate later)

        # 🔹 now interpolate for each pixel
        n_tiles_y = (M + kernel_size - 1) // kernel_size
        n_tiles_x = (N + kernel_size - 1) // kernel_size

        for i in range(M):
            for j in range(N):
                ty, tx = i // kernel_size, j // kernel_size
                dy = (i % kernel_size) / kernel_size
                dx = (j % kernel_size) / kernel_size

                ty1 = min(ty, n_tiles_y-1)
                tx1 = min(tx, n_tiles_x-1)
                ty2 = min(ty+1, n_tiles_y-1)
                tx2 = min(tx+1, n_tiles_x-1)

                val = photo[i, j]

                # get mapped values from 4 neighboring tiles
                q11 = mappings[(ty1, tx1)].get(val, val)
                q21 = mappings[(ty1, tx2)].get(val, val)
                q12 = mappings[(ty2, tx1)].get(val, val)
                q22 = mappings[(ty2, tx2)].get(val, val)

                # bilinear interpolation
                new_val = (
                    (1-dx)*(1-dy)*q11 +
                    dx*(1-dy)*q21 +
                    (1-dx)*dy*q12 +
                    dx*dy*q22
                )
                new[i, j] = round(new_val)

        return new
    

    def bi_hist_eq(self,mean_median_flag:str):
        
        photo = self.photo
        M = self.M
        N = self.N
        pix_freq_dist = self.__pix_freq()
        new = np.zeros((M,N),np.uint8)

        freqs = list(pix_freq_dist.keys())

        if mean_median_flag == 'mean':
            mid_val = np.mean(freqs)
        else:
            mid_val = np.median(freqs)

        low_half = dict()
        up_half = dict()

        for i in pix_freq_dist:
            if i <= mid_val:
                low_half[i] = pix_freq_dist[i]
            else:
                up_half[i] = pix_freq_dist[i]


        def remapper(pix_freq_dist:dict,low_up_flag:str):
            cum_sum = 0
            cdf = dict()

            for k,v in pix_freq_dist.items():
                cum_sum += v
                cdf[k] = cum_sum

            
            min_cdf_freq = min(cdf.values())
            
            for i in cdf :
                if low_up_flag == 'low':
                    cdf[i] = np.uint8(np.ceil((cdf[i] - min_cdf_freq)/(M*N - min_cdf_freq) * 127))
                else :
                    cdf[i] = np.uint8(128 + np.ceil((cdf[i] - min_cdf_freq)/(M*N - min_cdf_freq) * 127))
            return cdf
        
        
        low_half = remapper(low_half,'low')
        up_half = remapper(up_half,'up')

        pix_freq_dist = low_half | up_half
        pix_freq_dist = dict(sorted(pix_freq_dist.items()))

        for i in range(0,M):
            for j in range(0,N):
                new[i,j] = pix_freq_dist[photo[i,j]]

        return new

    
    
   


e = histo_eq(img,720,1080)

# img = e.global_hist_eq()
# print(img)

img = e.bi_hist_eq('mean')

cv2.imshow("Car Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()