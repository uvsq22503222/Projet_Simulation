import numpy as np
import matplotlib.pyplot as plt

from simulateur import simulate

# Paramètres fixes
K = 10
lambd = 1
tau = 1
T = 1000

# Valeurs de N testées
Ns = range(1, 31)

debits = []

# Simulation pour chaque N
for N in Ns:

    result = simulate(
        N=N,
        K=K,
        lambd=lambd,
        tau=tau,
        T=T,
        seed=42
    )

    debits.append(result.final_throughput)

    print(f"N = {N}, débit = {result.final_throughput:.4f}")

# Graphe
plt.figure()

plt.plot(Ns, debits, marker="o")

plt.xlabel("N")
plt.ylabel("d(N, K, lambda, tau)")

plt.title("Débit en fonction de N")

plt.grid()

plt.show()