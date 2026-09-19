import numpy as np
from filters import lpf
from rate_conversion import upsample
from utilities import plot_dtft


"""
Wc = np.pi / 4
M = 10    # M = 10 differs from the expected behavior of an ideal lpf with a smoother cutoff; increasing M results in being closer to an ideal lpf

h = lpf(Wc, M)

plot_dtft(h)
"""