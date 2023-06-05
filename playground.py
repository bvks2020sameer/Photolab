import numpy as np
from matplotlib import pyplot as plt


def gauss(Range) :
    gx = 2*np.pi*np.random.rand(Range)
    gy = np.cos(gx)*np.random.rand(Range)
    plt.plot(gy)
    plt.show()
    return None

gauss(100)