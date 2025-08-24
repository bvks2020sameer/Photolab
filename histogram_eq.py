import cv2
import numpy as np


class histo_eq(object):

    def __init__(self,photo,M,N):
        self.photo = photo
        self.M = M
        self.N = N
        return None
    
    # Pixel Frequency Counter

    def __pix_freq(self,photo) -> dict:
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

        pix_freq_dist = self.__pix_freq(photo)
        
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
    
    # Pixel frequency redistributer for CLAHE

    def __pix_freq_redritibuter(self,pix_freq_dist:dict,threshold:int,reiteration:int = 0) -> dict:
        if max(list(pix_freq_dist.values())) > threshold:
            pix_sum = 0

            for i in pix_freq_dist:
                if pix_freq_dist[i] > threshold :
                    pix_sum += pix_freq_dist[i] - threshold
                    pix_freq_dist[i] = threshold

            step_cnt = 0

            for i in pix_freq_dist:
                if pix_freq_dist[i] < threshold :
                    step_cnt += 1

            if step_cnt != 0 :
                pix_avg = pix_sum//step_cnt

                for i in pix_freq_dist:
                    if pix_freq_dist[i] < threshold :
                        pix_freq_dist[i] += pix_avg
                
                if max(list(pix_freq_dist.values())) <= threshold:
                    return pix_freq_dist
                else:
                    reiteration += 1
                    if reiteration <5:
                        return self.__pix_freq_redritibuter(pix_freq_dist,threshold,reiteration)
                    else:
                        return pix_freq_dist
            else :
                return pix_freq_dist
        
        else :
            return pix_freq_dist


    # CLAHE Method for Histogram equalization 

    def CLAHE_eq(self, kernel_size: int, threshold: int = None) -> np.array:
        photo = self.photo
        M, N = self.M, self.N
        new = np.zeros((M, N), dtype=np.uint8)

        if threshold is None:
            pix_freq_tot = self.__pix_freq(photo)
            avg_freq = np.ceil(np.mean(list(pix_freq_tot.values())))
            threshold = avg_freq * 2
    

        block_maps = {}

        
        for i in range(M // kernel_size ):
            for j in range(N // kernel_size ):
                row_start, row_end = i * kernel_size, min((i + 1) * kernel_size, M)
                col_start, col_end = j * kernel_size, min((j + 1) * kernel_size, N)
                kernel = photo[row_start:row_end, col_start:col_end]

                pix_freq_dist = self.__pix_freq(kernel)
                pix_freq_dist = self.__pix_freq_redritibuter(pix_freq_dist, threshold)

                sorted_keys = sorted(pix_freq_dist.keys())
                cdf = {}
                cumulative = 0
                for k in sorted_keys:
                    cumulative += pix_freq_dist[k]
                    cdf[k] = cumulative

                min_cdf = min(v for v in cdf.values() if v > 0)
                total = kernel.size
                remapped = {}
                for k in sorted_keys:
                    remapped[k] = np.uint8(
                        np.ceil((cdf[k] - min_cdf) / (total - min_cdf + 0.1) * 255)
                    )

                block_maps[(i, j)] = remapped

        
        for i in range(M):
            for j in range(N):
                bi, bj = i // kernel_size, j // kernel_size
                di, dj = (i % kernel_size) / kernel_size, (j % kernel_size) / kernel_size

                intensity = photo[i, j]

                
                maps = []
                for ii in [bi, bi + 1]:
                    for jj in [bj, bj + 1]:
                        if (ii, jj) in block_maps:
                            maps.append(block_maps[(ii, jj)].get(intensity, intensity))
                        else:
                            maps.append(intensity)

                
                top = (1 - dj) * maps[0] + dj * maps[1]
                bottom = (1 - dj) * maps[2] + dj * maps[3]
                value = (1 - di) * top + di * bottom

                new[i, j] = np.uint8(value)

        return new
    

    # Bi-Histogram Equalization method

    def bi_hist_eq(self,mean_median_flag:str) -> np.array:
        
        photo = self.photo
        M = self.M
        N = self.N
        pix_freq_dist = self.__pix_freq(photo)
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

    
    