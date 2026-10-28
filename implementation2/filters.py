from scipy.signal import lfilter


def de_emphasis(x, fs):

    tau = 75e-6  # de-emphasis time constant

    k = 2 * tau * fs    # substitution

    b = [1 / (1 + k), 1 / (1 + k)]
    a = [1, (1 - k) / (1 + k)]

    y = lfilter(b, a, x)

    return y, b, a