import numpy as np
from scipy.signal import remez, lfilter


def limiter(x):
    return x / np.maximum(np.abs(x), 1e-12)     # normalize magnitude, and preventing division by zero


def differentiator(x, fs):

    M = 30  # filter order
    num_taps = M + 1    # no. of coefficients
    cutoff = 100000  # passband edge (Hz)

    h = remez(num_taps, [0, cutoff], [1], type="differentiator", fs=fs) # remez(# of fir coefficients, frequency band applied, desired gain, ..., fs)

    h = h * 2 * np.pi * fs  # scaled to the ct differentiator

    dx = lfilter(h, 1, x)   # apply filter (no feedback)

    delay = M // 2

    return dx, delay, h

"""

"""