import numpy as np
from filters import lpf
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


def rateConverter(x, M):

    L = 147
    D = 160

    h = 147 * lpf(np.pi / 160, M)

    xUpsampled = upsample(x, L)
    xFiltered = filterSignal(xUpsampled, h)
    y = downsample(xFiltered, D)

    return y