import numpy as np
import matplotlib.pyplot as plt

def diff(a, b):
    slp = []
    for i in range(len(a) - 1):
        slp.append((b[i + 1] - b[i]) / (a[i + 1] - a[i]))
    slp = np.array(slp)
    mid = (a[:-1] + a[1:]) / 2
    return slp, mid

x = np.linspace(-10, 10, 501)
y = np.sin(x) * np.cos(x) * np.exp(-x ** 2)

m, x_mid = diff(x, y)

m2, x_mid2 = diff(x_mid, m)

np_m = np.diff(y) / np.diff(x)
np_x_mid = (x[:-1] + x[1:]) / 2

np_m2 = np.diff(np_m) / np.diff(np_x_mid)
np_x_mid2 = (np_x_mid[:-1] + np_x_mid[1:]) / 2

plt.figure(figsize=(12, 6))
plt.plot(x, y, '-', color='#1f77b4', label='y = sin(x) * cos(x) * e^(-x^2)')
plt.plot(x_mid, m, '-', color='#ff7f0e', label="1st derivative (approx)")
plt.plot(x_mid2, m2, '-', color='#000000', label="2nd derivative (approx)")
plt.plot(np_x_mid, np_m, '--', color='#d62728', label="1st derivative (np.diff)")
plt.plot(np_x_mid2, np_m2, '--', color="#2ca02c", label="2nd derivative (np.diff)")
plt.grid(True)
plt.legend()
plt.title('Function and Derivatives Comparison (with np.diff)')
plt.show()
