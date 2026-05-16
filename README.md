# Projet de simulation — Medium Access Control

GE Shuning - GUO Xuxin


Ce projet simule un protocole MAC utilisant l’algorithme Exponential Backoff.

Le simulateur est développé en Python avec une approche de simulation à événements discrets.

---

# Structure du projet

```text
Projet_Simulation/
│
├── simulateur.py
├── main.py
├── experiences/
│   ├── variation_lambda.py
│   ├── variation_N.py
│   ├── optimal_N_ic95.py
│   └── comparaison_backoff.py
│
├── resultats/
│
├── README.md
└── .gitignore
```

---

# Description des fichiers

## `simulateur.py`

Contient le cœur du simulateur :

- gestion des événements ;
- files d’attente ;
- collisions ;
- Exponential Backoff ;
- calcul des statistiques.

---

## `main.py`

Lance une simulation simple et génère :

- le débit du système ;
- le nombre moyen de clients ;
- le taux de pertes ;
- le taux de collisions.

---

## `experiences/variation_lambda.py`

Étudie l’évolution du débit :

\[
d(N,K,\lambda,\tau)
\]

quand `lambda` varie.

---

## `experiences/variation_N.py`

Étudie l’évolution du débit quand le nombre de stations `N` varie.

---

## `experiences/optimal_N_ic95.py`

Détermine la valeur de `N` maximisant le débit avec un intervalle de confiance à 95 %.

---

## `experiences/comparaison_backoff.py`

Compare :

- l’Exponential Backoff ;
- un backoff constant.

Cette expérience montre l’effet du mécanisme de backoff sur :
- les collisions ;
- le débit du système.

---

# Installation

Installer les bibliothèques nécessaires :

```bash
pip install numpy matplotlib
```

---

# Lancement des simulations

## Simulation principale

```bash
python main.py
```

---

## Variation de lambda

```bash
python experiences/variation_lambda.py
```

---

## Variation de N

```bash
python experiences/variation_N.py
```

---

## Recherche du N optimal avec IC95

```bash
python experiences/optimal_N_ic95.py
```

---

## Comparaison des protocoles de backoff

```bash
python experiences/comparaison_backoff.py
```

---

# Résultats

Les figures sont sauvegardées automatiquement dans :

```text
resultats/
```

---

# Paramètres principaux

Les principaux paramètres du modèle sont :

- `N` : nombre de stations ;
- `K` : capacité des files d’attente ;
- `lambda` : intensité des arrivées ;
- `tau` : paramètre du backoff ;
- `T` : durée de simulation.

---

# Modèle simulé

Le système simulé suit les hypothèses du sujet :

- arrivées exponentielles ;
- durée de transmission fixe égale à 1 ;
- collisions si deux transmissions se recouvrent ;
- retransmission après attente aléatoire ;
- files d’attente bornées.

---

# Technologies utilisées

- Python 3
- NumPy
- Matplotlib
