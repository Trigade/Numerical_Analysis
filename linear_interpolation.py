import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)
y = np.sin(x)

x_interp = np.linspace(x[0], x[-1], 500)
y_interp = np.zeros_like(x_interp)

for j in range(len(x_interp)):
    xi = x_interp[j]
    for i in range(len(x) - 1):
        if x[i] <= xi <= x[i + 1]:
            y_interp[j] = y[i] + (xi - x[i]) * (y[i + 1] - y[i]) / (x[i + 1] - x[i])
            break

plt.figure(figsize=(8, 4))
plt.plot(x, y, 'o', color='red', label='Veri Noktaları')
plt.plot(x_interp, y_interp,label='Doğrusal Enterpolasyon')
plt.title("Linear (Doğrusal) Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()