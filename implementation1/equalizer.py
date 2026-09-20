import numpy as np
from scipy.signal import lfilter
from filters import lpf, bpf


def equalizer(x, gainLow, gainMid, gainHigh, M):

    fs = 44100  # sampling frequency

    WcLow = 2 * np.pi * 300 / fs
    hLow = lpf(WcLow, M)

    WlMid = 2 * np.pi * 300 / fs
    WhMid = 2 * np.pi * 3000 / fs
    W0Mid = (WhMid + WlMid) / 2 # mid band center frequency
    WcMid = (WhMid - WlMid) / 2
    hMid = bpf(WcMid, W0Mid, M)

    WlHigh = 2 * np.pi * 3000 / fs
    WhHigh = 2 * np.pi * 20000 / fs
    W0High = (WhHigh + WlHigh) / 2  # high band center frequency
    WcHigh = (WhHigh - WlHigh) / 2
    hHigh = bpf(WcHigh, W0High, M)

    xLow = lfilter(hLow, 1, x)
    xMid = lfilter(hMid, 1, x)
    xHigh = lfilter(hHigh, 1, x)

    y = gainLow * xLow + gainMid * xMid + gainHigh * xHigh

    return y


