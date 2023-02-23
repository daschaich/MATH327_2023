#!/usr/bin/python3
# ------------------------------------------------------------------
import numpy as np
import matplotlib           # Hack for office machine
matplotlib.use('TkAgg')     # Hack for office machine
import matplotlib.pyplot as plt

# Temperature vs. energy for micro-canonical spin system
x = np.arange(-1, 1, 0.001)
T = -1.0 / x
plt.plot(x, T, 'k--')
plt.plot(x, T, 'b.')
plt.plot(x, 0*x, 'k--')
plt.xlabel('$E~/~NH$')
plt.ylabel('$\\frac{T}{H}$', rotation=0, fontsize=16, labelpad=10)
plt.ylim([-10, 10])
#plt.savefig('230220supplement_fig.pdf', bbox_inches='tight')
plt.show()
# ------------------------------------------------------------------
