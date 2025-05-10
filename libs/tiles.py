from PIL import Image
import random

# dictionnaire definnissants les differents filtre de couleur
couleurs = {}
# dictionnaire servant de base aux couleurs du dictionnaire couleurs
couleurs_base = {
    "rouge": (255, 0, 0),
    "vert": (0, 255, 0),
    "bleu": (0, 0, 255),
    "jaune": (255, 255, 0),
    "violet": (128, 0, 128),
    "orange": (255, 165, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "gris": (128, 128, 128),
    "noir": (0, 0, 0),
    "blanc": (255, 255, 255),
    "olive": (128, 128, 0),
    "teal": (0, 128, 128),
    "marron": (128, 0, 0),
    "vert_fonce": (0, 128, 0),
    "bleu_fonce": (0, 0, 128),
    "mauve": (128, 128, 255),
    "rose": (255, 128, 255),
    "turquoise": (128, 255, 255),
    "argent": (192, 192, 192),
    "rouge_fonce": (128, 0, 0),
    "vert_fonce": (0, 128, 0),
    "bleu_fonce": (0, 0, 128),
}


def generer_teintes_de_couleur(nombre_teintes, variation):
    """
    Genere nombre_teintes teintes des couleurs de base puis les stocke dans couleurs.

    Entrées:
        nombre_teintes  <- int : nombre de teinte différentes par couleurs de base
        variation       <- int : variation de R G B possible pour chaque teinte
    Sorties:

    Utilisations:
        generer_teintes_de_couleur(2, 20)
    """
    teintes = {}

    for couleur_base in couleurs_base:
        # cree n teinte différentes pour chaque couleur_base dans couleurs_base
        for n in range(nombre_teintes):
            teinte = tuple(min(max(intensite + random.randint(-variation, variation), 0), 255) for intensite in
                           couleurs_base[couleur_base])
            teintes[f"{couleur_base}_{n}"] = teinte

    for tint in teintes:
        # ajoute les teintes à couleurs 
        couleurs[tint] = teintes[tint]


def tiles_generator(image_path):
    """
    Créé un panel de couleur en fonction de l'image obtenu en entrée
    et renvoi une liste des différentes image teinte 

    Entrées:
        image_path  <- str   : emplacement de l'image original
    Sorties:
        <- list[Image] || None : liste de l'images modifié ou rien

    Utilisations:
        tiles_generator("../rendu/hedy.jpg") <- list[Image.Image]
    """
    tile = Image.open(image_path)
    # rend l'image en mode RGB, pour pouvoir séparer les canaux de couleurs(mode RGB de base)
    tile = tile.convert(mode="RGB")
    # sépare les 3 canaux de couleurs de l'image original (creer 1 image de rouge, vert et bleu)
    r, g, b = tile.split()

    generer_teintes_de_couleur(5, 15)  # genere une centaine de teintes

    tiles = []

    for color in couleurs:
        # cree une image teinté de la couleur color
        fltr = Image.merge("RGB", (
            r.point(lambda i: i * (couleurs[color][0] / 255)),
            g.point(lambda i: i * (couleurs[color][1] / 255)),
            b.point(lambda i: i * (couleurs[color][2] / 255))))
        tiles.append([fltr, couleurs[color]])

    return tiles
