import numpy as np
from scipy.signal import lfilter


def upsample(x, L):

    y = np.zeros(len(x) * L)
    y[::L] = x  # every L-th element

    return y


def downsample(x, D):

    y = x[::D]  # every D-th element

    return y


def filterSignal(x,h):

    y = lfilter(h, 1, x)

    return y