import numpy as np
import matplotlib.pyplot as plt
from functions.polynomailValue import polyval
from functions.polynomialFitting import polyfit

x = np.array([0, 1, 2, 3, 4])
y = np.sin(x)

degree = len(x) - 1

coeffs = polyfit(x, y, degree)
x_interp = np.linspace(x[0], x[-1], 500)
y_interp = polyval(coeffs, x_interp)

plt.plot(x, y, 'ro', label='Veri Noktaları')
plt.plot(x_interp, y_interp, 'b-', label='Polinomsal Interpolasyon')
plt.title('Polynomial Interpolation (my_polyfit & my_polyval)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()