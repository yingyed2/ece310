import numpy as np
import soundfile as sf

from rate_conversion import rateConverter
from equalizer import equalizer

"""
LLM Disclosure:
I used ChatGPT for understanding the soundfile library for audio file input/output and for debugging Git/Python errors.
"""

inputFile = "funk.mp3"
outputFile = "output.wav"

x, fs = sf.read(inputFile)

if fs != 48000:
    raise ValueError("Input file must have a sampling frequency of 48000 Hz.")

if x.ndim == 2:
    x = np.mean(x, axis=1)  # convert to mono by averaging channels

x = rateConverter(x, M = 100)
y = equalizer(x, gainLow=1.0, gainMid=1.0, gainHigh=1.0, M=100)

sf.write(outputFile, y, 44100)

print(f"Processed audio saved to {outputFile}")