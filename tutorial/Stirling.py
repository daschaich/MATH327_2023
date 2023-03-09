#!/usr/bin/python3
# ------------------------------------------------------------------
# See how well x^N e^(-x) is approximated by a gaussian
# Normalize by maximum N^N e^(-N)
# Will overflow float precision when N-x too large
import numpy as np
import matplotlib.pyplot as plt

N = 100.0                       # Could read in as input
x = np.arange(0, 2*N, 0.001)
integrand = np.power(x / N, N) * np.exp(N - x)
gauss = np.exp(-(x - N)**2 / (2.0 * N))         # Norm cancels out
plt.plot(x, integrand, 'k-', label="$x^N e^{-x}$")
plt.plot(x, gauss, 'b--', label="Gaussian")
plt.xlabel('$x$')
plt.yticks([], [])
plt.legend(loc='upper right')
#plt.savefig('figs/Stirling.pdf', bbox_inches='tight')
plt.show()

# Check various approximations to log(N!)
import numpy as np
from scipy import special

N = 160
#N = np.power(10, 10)
print("N = %d" % N)

direct = np.log(special.factorial(N))
approx = N * np.log(N) - N
rel = 100.0 * np.abs(1 - approx/direct)
print("Nlog(N) - N = %.12g (%.2g percent off)" % (approx, rel))

approx += 0.5 * np.log(2.0 * np.pi * N)
rel = 100.0 * np.abs(1 - approx/direct)
print("Include log(N): %.12g (%.2g percent off)" % (approx, rel))

A = approx + np.log(1.0 + 1.0 / (12.0 * N))
rel = 100.0 * np.abs(1 - A/direct)
print("Include 1/N: %.12g (%.2g percent off)" % (A, rel))

B = approx + np.log(1.0 + 1.0 / (12.0 * N) + 1.0 / (288.0 * N * N))
rel = 100.0 * np.abs(1 - B/direct)
print("Include 1/N^2: %.12g (%.2g percent off)" % (B, rel))

print("Direct log(N!) = %.12g" % direct)
print("N! = %.4g" % special.factorial(N))
# ------------------------------------------------------------------
