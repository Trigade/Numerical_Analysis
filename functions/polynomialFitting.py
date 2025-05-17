import numpy as np

def polyfit(x,y,degree):
    n = len(x)
    assert n == len(y)
    assert degree < n

    X = np.vander(x, degree + 1)

    XT = X.T
    A = XT @ X
    b = XT @ y

    coeffs = np.linalg.solve(A, b)
    return coeffs