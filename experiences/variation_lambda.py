import numpy as np
import matplotlib.pyplot as plt

import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from simulateur import simulate


N = 5
K = 10
tau = 1
T = 1000

lambdas = np.linspace(0.02, 2, 30)

debits = []

for lambd in lambdas:
    result = simulate(N, K, lambd, tau, T, seed=42)
    debits.append(result.final_throughput)

plt.figure()
plt.plot(lambdas, debits, marker="o")
plt.xlabel("lambda")
plt.ylabel("d(N, K, lambda, tau)")
plt.title("Débit en fonction de lambda")
plt.grid()
plt.show()