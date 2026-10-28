import numpy as np

def limiter(x):
    return x / np.maximum(np.abs(x), 1e-12)     # normalize magnitude, and preventing division by zero