from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from scipy.io import loadmat
from scipy.signal import freqz
from demodulation import limiter, differentiator, conjugate_delay
from filters import de_emphasis


fs = 256000

data_folder = Path(__file__).parent / "data"
files = sorted(data_folder.glob("*.mat"))

for i, filename in enumerate(files):

    x = loadmat(filename)["data"].ravel() # loads the complex baseband signal into a 1D array

    x_limited = limiter(x)

    dx, delay, h = differentiator(x_limited, fs)

    y = conjugate_delay(x_limited, dx, delay)

    y_deemph, b, a = de_emphasis(y, fs)

    if i == 0:

        f, H = freqz(b, a, worN=2048, fs=fs)

        plt.figure()
        plt.plot(f / 1000, 20 * np.log10(np.abs(H) + 1e-12))
        plt.xlabel("Frequency (kHz)")
        plt.ylabel("Magnitude (dB)")
        plt.title("De-emphasis Filter Magnitude Response")
        plt.grid()

        plt.figure()
        plt.plot(f / 1000, np.angle(H))
        plt.xlabel("Frequency (kHz)")
        plt.ylabel("Phase (radians)")
        plt.title("De-emphasis Filter Phase Response")
        plt.grid()

plt.show()