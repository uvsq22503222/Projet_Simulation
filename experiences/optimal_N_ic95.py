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


def intervalle_confiance_95(valeurs):
    valeurs = np.array(valeurs)
    moyenne = np.mean(valeurs)
    ecart_type = np.std(valeurs, ddof=1)
    demi_largeur = 1.96 * ecart_type / np.sqrt(len(valeurs))
    return moyenne, moyenne - demi_largeur, moyenne + demi_largeur


K = 10
tau = 1
T = 1000
R = 30
Ns = range(1, 31)

resultats_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resultats")

for lambd in [1.0, 0.2]:

    print(f"\n=== λ = {lambd} ===")

    moyennes = []
    bornes_inf = []
    bornes_sup = []

    for N in Ns:
        debits_N = [
            simulate(N=N, K=K, lambd=lambd, tau=tau, T=T, seed=1000 * N + r).final_throughput
            for r in range(R)
        ]
        moyenne, borne_inf, borne_sup = intervalle_confiance_95(debits_N)
        moyennes.append(moyenne)
        bornes_inf.append(borne_inf)
        bornes_sup.append(borne_sup)
        print(f"N={N:2d} | moyenne={moyenne:.4f} | IC95=[{borne_inf:.4f}, {borne_sup:.4f}]")

    indice_max = int(np.argmax(moyennes))
    N_optimal = list(Ns)[indice_max]
    print(f"\nN optimal = {N_optimal}, débit moyen = {moyennes[indice_max]:.4f}, "
          f"IC95 = [{bornes_inf[indice_max]:.4f}, {bornes_sup[indice_max]:.4f}]")

    erreurs_inf = np.array(moyennes) - np.array(bornes_inf)
    erreurs_sup = np.array(bornes_sup) - np.array(moyennes)

    plt.figure(figsize=(9, 5))
    plt.errorbar(
        list(Ns), moyennes,
        yerr=[erreurs_inf, erreurs_sup],
        marker="o", capsize=4, color="steelblue"
    )
    plt.axvline(N_optimal, color="tomato", linestyle="--",
                label=f"N optimal = {N_optimal}")
    plt.xlabel("N")
    plt.ylabel("Débit moyen")
    plt.title(f"Débit moyen en fonction de N avec IC 95%\n(λ={lambd}, K={K}, τ={tau}, T={T}, R={R})")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    fname = os.path.join(resultats_dir, f"optimal_N_ic95_lambda{str(lambd).replace('.', '')}.png")
    plt.savefig(fname, dpi=300)
    plt.close()
    print(f"Figure sauvegardée : {fname}")
