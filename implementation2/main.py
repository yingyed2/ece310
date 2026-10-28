from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from scipy.io import loadmat
from scipy.signal import freqz
from demodulation import limiter, differentiator, conjugate_delay


fs = 256000

data_folder = Path(__file__).parent / "data"
files = sorted(data_folder.glob("*.mat"))

for i, filename in enumerate(files):

    x = loadmat(filename)["data"].ravel() # loads the complex baseband signal into a 1D array

    x_limited = limiter(x)
    dx, delay, h = differentiator(x_limited, fs)

    y = conjugate_delay(x_limited, dx, delay)

    print(filename.name)
    print("Output samples:", len(y))
    print("Output type:", y.dtype)
    print("First five steady-state samples:", y[100:105])
    print()

    if i == 0:

        f, H = freqz(h, worN=2048, fs=fs)

        plt.figure()
        plt.plot(f / 1000, np.abs(H), label="FIR differentiator")
        plt.plot(f / 1000, 2 * np.pi * f, "--", label="Ideal")
        plt.xlabel("Frequency (kHz)")
        plt.ylabel("Magnitude")
        plt.title("Differentiator Magnitude Response")
        plt.legend()
        plt.grid()

        omega = 2 * np.pi * f / fs
        H_corrected = H * np.exp(1j * omega * delay)

        plt.figure()
        plt.plot(f[1:] / 1000, np.angle(H_corrected[1:]))
        plt.xlabel("Frequency (kHz)")
        plt.ylabel("Phase (radians)")
        plt.title("Differentiator Phase (Delay Removed)")
        plt.xlim(0, 100)
        plt.grid()

    test_frequency = 1000

    t = np.arange(5000) / fs
    test_x = np.exp(1j * 2 * np.pi * test_frequency * t)

    test_dx, test_delay, _ = differentiator(test_x, fs)
    test_y = conjugate_delay(test_x, test_dx, test_delay)

    print("Expected:", 2 * np.pi * test_frequency)
    print("Measured:", np.mean(test_y[100:]))

plt.show()