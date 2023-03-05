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
# ------------------------------------------------------------------
