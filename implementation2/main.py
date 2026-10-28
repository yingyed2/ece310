from pathlib import Path
import numpy as np
from scipy.io import loadmat
from demodulation import limiter

fs = 256000

data_folder = Path(__file__).parent / "data"
files = sorted(data_folder.glob("*.mat"))

for filename in files:

    x = loadmat(filename)["data"].ravel() # loads the complex baseband signal into a 1D array

    x_limited = limiter(x)

    print(filename.name)
    print("Samples:", len(x))
    print("Duration:", len(x) / fs, "seconds")  # N/fs
    print("Mean magnitude after limiter:", np.mean(np.abs(x_limited)))
    print()
