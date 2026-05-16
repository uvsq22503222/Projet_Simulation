import os
import matplotlib.pyplot as plt

from simulateur import simulate


os.makedirs("resultats", exist_ok=True)

N = 5
K = 10
lambd = 1
tau = 1
T = 1000

result = simulate(N, K, lambd, tau, T, seed=42)

print("Résultats de la simulation")
print("--------------------------")
print("Succès :", result.successes)
print("Arrivées :", result.arrivals)
print("Pertes :", result.losses)
print("Collisions :", result.collisions)
print("Débit final :", result.final_throughput)

plt.figure()
plt.plot(result.times, result.throughput)
plt.xlabel("Temps")
plt.ylabel("n(t)/t")
plt.title("Débit du système")
plt.grid()
plt.savefig("resultats/debit_systeme.png", dpi=300)
plt.close()

plt.figure()
plt.plot(result.times, result.mean_clients)
plt.xlabel("Temps")
plt.ylabel("Nombre moyen de clients")
plt.title("Clients moyens")
plt.grid()
plt.savefig("resultats/clients_moyens.png", dpi=300)
plt.close()

plt.figure()
plt.plot(result.times, result.loss_rate)
plt.xlabel("Temps")
plt.ylabel("Taux de pertes")
plt.title("Pertes")
plt.grid()
plt.savefig("resultats/pertes.png", dpi=300)
plt.close()

plt.figure()
plt.plot(result.times, result.collision_rate)
plt.xlabel("Temps")
plt.ylabel("Collisions / temps")
plt.title("Taux de collisions")
plt.grid()
plt.savefig("resultats/collisions.png", dpi=300)
plt.close()