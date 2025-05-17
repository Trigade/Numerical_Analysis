import numpy as np
import matplotlib.pyplot as plt

def linterp(x_interp,x,y):
    y_interp = np.zeros_like(x_interp)

    for j in range(len(x_interp)):
        xi = x_interp[j]
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                y_interp[j] = y[i] + (xi - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                break
    return y_interp