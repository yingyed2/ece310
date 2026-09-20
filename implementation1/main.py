import numpy as np
from filters import lpf, bpf
from rate_conversion import rateConverter
from utilities import plot_dtft

"""
Wc = np.pi / 160
M = 100    # M = 10 differs from the expected behavior of an ideal lpf with a smoother cutoff; increasing M results in being closer to an ideal lpf

h = 147 * lpf(Wc, M)

plot_dtft(h)
"""