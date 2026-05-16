import os
import matplotlib.pyplot as plt

from simulateur import simulate


os.makedirs("resultats", exist_ok=True)

N = 10
K = 10
lambd = 1
tau = 1
T = 1000

# Avec exponential backoff
result_exp = simulate(
    N=N,
    K=K,
    lambd=lambd,
    tau=tau,
    T=T,
    seed=42,
    exponential_backoff=True
)

# Sans exponential backoff
result_simple = simulate(
    N=N,
    K=K,
    lambd=lambd,
    tau=tau,
    T=T,
    seed=42,
    exponential_backoff=False
)

print("=== Avec Exponential Backoff ===")
print("Débit :", result_exp.final_throughput)
print("Collisions :", result_exp.collisions)
print("Pertes :", result_exp.losses)

print()

print("=== Sans Exponential Backoff ===")
print("Débit :", result_simple.final_throughput)
print("Collisions :", result_simple.collisions)
print("Pertes :", result_simple.losses)

# Comparaison débit
plt.figure()

plt.plot(
    result_exp.times,
    result_exp.throughput,
    label="Exponential Backoff"
)

plt.plot(
    result_simple.times,
    result_simple.throughput,
    label="Backoff constant"
)

plt.xlabel("Temps")
plt.ylabel("Débit")
plt.title("Comparaison des débits")

plt.legend()
plt.grid()

plt.savefig("resultats/comparaison_debit.png", dpi=300)

plt.close()

# Comparaison collisions
plt.figure()

plt.plot(
    result_exp.times,
    result_exp.collision_rate,
    label="Exponential Backoff"
)

plt.plot(
    result_simple.times,
    result_simple.collision_rate,
    label="Backoff constant"
)

plt.xlabel("Temps")
plt.ylabel("Collisions / temps")
plt.title("Comparaison des collisions")

plt.legend()
plt.grid()

plt.savefig("resultats/comparaison_collisions.png", dpi=300)

plt.close()