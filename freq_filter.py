import numpy as np

class freq_filter(object):

    def __init__(self,photo,M,N) -> None:
        self.photo = photo
        self.M = M
        self.N = N


    def ideal_low_pass(self, cuttoff: int):

        photo = self.photo
        M = self.M
        N = self.N
        freq_dom = np.fft.fft2(photo)
        freq_dom = np.fft.fftshift(freq_dom)

        H = np.zeros((M,N),dtype= np.float32 )
        for i in range(M):

            for j in range(N):
                D = np.sqrt((i-M/2)**2 + (j-N/2)**2)
                if D <= cuttoff:
                    H[i,j] = 1
                else:
                    H[i,j] = 0

        Gshift = H*freq_dom
        G = np.fft.ifftshift(Gshift)
        new = np.abs(np.fft.ifft2(G))

        return new





    def ideal_high_pass(self, cuttoff: int):

        photo = self.photo
        M = self.M
        N = self.N
        freq_dom = np.fft.fft2(photo)
        freq_dom = np.fft.fftshift(freq_dom)

        H = np.zeros((M,N),dtype= np.float32)
        for i in range(M):

            for j in range(N):
                D = np.sqrt((i-M/2)**2 + (j-N/2)**2)
                if D >= cuttoff:
                    H[i,j] = 1
                else:
                    H[i,j] = 0

        Gshift = H*freq_dom
        G = np.fft.ifftshift(Gshift)
        new = np.abs(np.fft.ifft2(G))

        return new





    def butter_low_pass(self,cuttoff: int,n:int) :

        photo = self.photo
        M = self.M
        N = self.N

        H = np.zeros((M,N),dtype= np.float32)
        for i in range(0, M):
            for j in range(0, N):
                if((np.sqrt((i-M/2)**2 + (j-N/2)**2)) != 0 ):
                    key = (np.sqrt((i-M/2)**2 + (j-N/2)**2))
                else :
                    key = 1;
                H[i,j] = 1/(1+(key/cuttoff)**n)

        FFT = np.fft.fft2(photo)
        FFT = np.fft.fftshift(FFT)

        Gshift = H * FFT
        G = np.fft.ifftshift(Gshift)
        new = np.abs(np.fft.ifft2(G))

        return  new




    def butter_high_pass(self,cuttoff: int,n:int) :

        photo = self.photo
        M = self.M
        N = self.N

        H = np.zeros((M,N),dtype= np.float32)
        for i in range(0, M):
            for j in range(0, N):
                if((np.sqrt((i-M/2)**2 + (j-N/2)**2)) != 0 ):
                    key = (np.sqrt((i-M/2)**2 + (j-N/2)**2))
                else :
                    key = 1;
                H[i,j] = 1/(1+(cuttoff/key)**n)

        FFT = np.fft.fft2(photo)
        FFT = np.fft.fftshift(FFT)

        Gshift = H * FFT
        G = np.fft.ifftshift(Gshift)
        new = np.abs(np.fft.ifft2(G))

        return  new



    def gauss_low_pass(self,cuttoff: int,sigma:int) :

        photo = self.photo
        M = self.M
        N = self.N

        H = np.zeros((M,N),dtype= np.float32)

        s = 2*sigma*sigma
        for i in range(0, M):
            for j in range(0, N):
                key = (np.sqrt((i-M/2)**2 + (j-N/2)**2))

                H[i,j] = np.exp((-key)/s)

        FFT = np.fft.fft2(photo)
        FFT = np.fft.fftshift(FFT)

        Gshift = H * FFT
        G = np.fft.ifftshift(Gshift)
        new = np.abs(np.fft.ifft2(G))

        return  new




    def gauss_high_pass(self,cuttoff: int,sigma:int) :

        photo = self.photo
        M = self.M
        N = self.N

        H = np.zeros((M,N),dtype= np.float32)

        s = 2*sigma*sigma
        for i in range(0, M):
            for j in range(0, N):
                key = (np.sqrt((i-M/2)**2 + (j-N/2)**2))

                H[i,j] = 1 - np.exp((-key)/s)

        FFT = np.fft.fft2(photo)
        FFT = np.fft.fftshift(FFT)

        Gshift = H * FFT
        G = np.fft.ifftshift(Gshift)
        new = np.abs(np.fft.ifft2(G))

        return  new


