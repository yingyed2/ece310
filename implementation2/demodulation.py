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

"""tested with dtft plot"""


def conjugate_delay(x_limited, dx, delay):

    x_delayed = np.zeros_like(x_limited)
    x_delayed[delay:] = x_limited[:-delay]  # delays samples by 'delay' amount

    product = dx * np.conj(x_delayed)   # multiply the derivative with the conjugate of the delayed signal

    y = np.imag(product)

    return y
