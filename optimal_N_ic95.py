import numpy as np
import matplotlib.pyplot as plt

from simulateur import simulate


def intervalle_confiance_95(valeurs):
    valeurs = np.array(valeurs)

    moyenne = np.mean(valeurs)
    ecart_type = np.std(valeurs, ddof=1)

    demi_largeur = 1.96 * ecart_type / np.sqrt(len(valeurs))

    borne_inf = moyenne - demi_largeur
    borne_sup = moyenne + demi_largeur

    return moyenne, borne_inf, borne_sup


K = 10
lambd = 1
tau = 1
T = 1000

R = 30  # nombre de répétitions

Ns = range(1, 31)

moyennes = []
bornes_inf = []
bornes_sup = []

for N in Ns:

    debits_N = []

    for r in range(R):

        result = simulate(
            N=N,
            K=K,
            lambd=lambd,
            tau=tau,
            T=T,
            seed=1000 * N + r
        )

        debits_N.append(result.final_throughput)

    moyenne, borne_inf, borne_sup = intervalle_confiance_95(debits_N)

    moyennes.append(moyenne)
    bornes_inf.append(borne_inf)
    bornes_sup.append(borne_sup)

    print(
        f"N={N:2d} | "
        f"moyenne={moyenne:.4f} | "
        f"IC95=[{borne_inf:.4f}, {borne_sup:.4f}]"
    )


# Détermination du meilleur N
indice_max = np.argmax(moyennes)
N_optimal = list(Ns)[indice_max]

print()
print("Résultat final")
print("--------------")
print(f"N optimal estimé = {N_optimal}")
print(f"Débit moyen max  = {moyennes[indice_max]:.4f}")
print(f"IC95             = [{bornes_inf[indice_max]:.4f}, {bornes_sup[indice_max]:.4f}]")


# Graphe avec barres d'erreur
erreurs_inf = np.array(moyennes) - np.array(bornes_inf)
erreurs_sup = np.array(bornes_sup) - np.array(moyennes)

plt.figure()

plt.errorbar(
    list(Ns),
    moyennes,
    yerr=[erreurs_inf, erreurs_sup],
    marker="o",
    capsize=4
)

plt.xlabel("N")
plt.ylabel("Débit moyen")
plt.title("Débit moyen en fonction de N avec IC 95 %")
plt.grid()

plt.show()