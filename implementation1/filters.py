import numpy as np

def lpf(Wc, M):

    h = np.zeros(2 * M + 1)

    for n in range(-M, M + 1):
        if n == 0:
            h[n + M] = Wc / np.pi
        else:
            h[n + M] = (np.sin(Wc * n) / (np.pi * n))
            
    return h

