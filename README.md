# MOSAIC - Génération d'une mosaique à partir d'une image

Le projet MOSAIC est le projet final de NSI de mon année de Terminale.

---

## ⚙️ Fonctionnalités

- Le script prend en entrée une image et en génère une version mosaique à partir d'elle même et l'affiche
---

## 🧰 Technologies utilisées

- **Python**
- **PIL (Pillow)** pour dessiner des images de rendu
---

## 🛠️ Utilisation type
#### Comme indiqué dans le fichier main.py

```bash
mosaique("./imgs/hedy.jpg", 150).show()
```
La fonction mosaique prend deux paramètres: ***path*** et ***power***

Dans cet exemple l'image d'entrée est hedy.jpg qu'on transforme en une image de 150 tuiles carrées de mosaique de tailles largeur/150.
Les tuiles sont teintés à partir des couleurs originelles de l'image.


*Plus l'argument power est grand plus la mosaique est précise*

---
## 🖼️ Rendus
Des images pré-générées avec un power élevé qui demandent une certaine puissance de calcul sont disponibles dans le dossier ***./rendu*** à titre d'illustration.
