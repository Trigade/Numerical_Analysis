import numpy as np

def polyval(coeffs, x_vals):
    y_vals = np.zeros_like(x_vals, dtype=float)
    for i, c in enumerate(coeffs):
        y_vals += c * x_vals**(len(coeffs) - i - 1)
    return y_vals