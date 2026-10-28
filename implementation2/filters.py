from scipy.signal import lfilter, remez, lfilter


def de_emphasis(x, fs):

    tau = 75e-6  # de-emphasis time constant

    k = 2 * tau * fs    # substitution

    b = [1 / (1 + k), 1 / (1 + k)]
    a = [1, (1 - k) / (1 + k)]

    y = lfilter(b, a, x)

    return y, b, a

"""tested with dtft plot"""


def mono_lowpass(x, fs):

    num_taps = 201  # constant group delay

    h = remez(num_taps, [0, 15000, 18000, fs / 2], [1, 0], weight=[1, 10], fs=fs)   # specifying passband with desired gain 1, and stopband with desired gain 0 w/ error weight of 10 for stopband

    y = lfilter(h, 1, x)

    return y, h