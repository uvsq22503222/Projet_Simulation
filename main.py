import numpy as np
import matplotlib.pyplot as plt

from simulateur import simulate

N = 5
K = 10
lambd = 0.15
tau = 1
T = 1000

result = simulate(N, K, lambd, tau, T, seed=42)

plt.figure()
plt.plot(result.times, result.throughput)
plt.xlabel("Temps")
plt.ylabel("n(t)/t")
plt.title("Débit du système")
plt.grid()

plt.figure()
plt.plot(result.times, result.mean_clients)
plt.xlabel("Temps")
plt.ylabel("Nombre moyen de clients")
plt.title("Clients moyens")
plt.grid()

plt.figure()
plt.plot(result.times, result.loss_rate)
plt.xlabel("Temps")
plt.ylabel("Taux de pertes")
plt.title("Pertes")
plt.grid()

plt.show()