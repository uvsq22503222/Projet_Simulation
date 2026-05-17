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

K = 10
tau = 1
T = 1000
R = 10  # répétitions pour lisser le bruit

Ns = range(1, 31)
lambdas = [1.0, 0.2]
styles = [
    {"color": "steelblue", "marker": "o", "label": "λ = 1.0"},
    {"color": "tomato",    "marker": "s", "label": "λ = 0.2"},
]

plt.figure(figsize=(9, 5))

for lambd, style in zip(lambdas, styles):
    debits = []
    for N in Ns:
        runs = [
            simulate(N=N, K=K, lambd=lambd, tau=tau, T=T, seed=1000 * N + r).final_throughput
            for r in range(R)
        ]
        debits.append(np.mean(runs))
        print(f"λ={lambd}, N={N:2d}, débit moyen={debits[-1]:.4f}")

    plt.plot(list(Ns), debits, marker=style["marker"],
             color=style["color"], label=style["label"])

    N_opt = list(Ns)[int(np.argmax(debits))]
    d_opt = max(debits)
    plt.axvline(N_opt, color=style["color"], linestyle="--", alpha=0.5,
                label=f"N optimal (λ={lambd}) = {N_opt}")
    print(f"  → N optimal pour λ={lambd} : N={N_opt}, débit={d_opt:.4f}\n")

plt.xlabel("N")
plt.ylabel("d(N, K, λ, τ)")
plt.title("Débit en fonction de N — comparaison λ=1.0 vs λ=0.2\n(K=10, τ=1.0, T=1000, moyenne sur 10 runs)")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "resultats", "fig_comparaison_lambda.png"),
    dpi=300
)
plt.show()
