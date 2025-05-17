import numpy as np
import matplotlib.pyplot as plt
from functions.search_sorted import searchsorted

x = np.arange(0, 10, 1)
y = np.cos(x)

x_i = np.linspace(x[0], x[-1], 500)
y_i = np.zeros_like(x_i)

for j in range(len(x) - 1):
    left_bound = x[j] - 0.5
    right_bound = x[j + 1] + 0.5

    start_idx = searchsorted(x_i, left_bound, side='left')
    end_idx = searchsorted(x_i, right_bound, side='right')

    y_i[start_idx:end_idx] = y[j]

plt.figure(figsize=(8, 4))
plt.plot(x, y, 'o', color='red', label='Orijinal Noktalar')
plt.plot(x_i, y_i, label='Atanmış Değerler')
plt.grid(True)
plt.legend()
plt.show()
