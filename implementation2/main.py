from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from scipy.io import loadmat, wavfile
from scipy.signal import freqz
from demodulation import limiter, differentiator, conjugate_delay
from filters import de_emphasis, mono_lowpass

"""
LLM Disclosure:
I used ChatGPT for debugging Python errors, understanding NumPy's .ravel() function, loading .mat files and exporting .wav files, assistance w/ generating DTFT plots.
"""

fs = 256000

data_folder = Path(__file__).parent / "data"
files = sorted(data_folder.glob("*.mat"))

for i, filename in enumerate(files):

    x = loadmat(filename)["data"].ravel() # loads the complex baseband signal into a 1D array

    x_limited = limiter(x)

    dx, delay, h = differentiator(x_limited, fs)

    y = conjugate_delay(x_limited, dx, delay)

    y_deemph, b, a = de_emphasis(y, fs)

    y_filtered, h_lp = mono_lowpass(y_deemph, fs)

    audio = y_filtered[::4] # downsample by 4
    fs_out = fs // 4

    peak = np.max(np.abs(audio))  # normalizing audio to prevent clipping

    if peak > 0:
        audio = 0.95 * audio / peak

    output_path = Path(__file__).parent / (filename.stem + ".wav")
    wavfile.write(output_path, fs_out, audio.astype(np.float32))

    print("Saved:", output_path.name)
    print("Output sample rate:", fs_out)

plt.show()