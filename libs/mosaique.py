from PIL import Image
from math import sqrt, isclose
from libs.tiles import tiles_generator


def distance(a, b):
    """Calcule la distance euclidienne de points A et B en
    dimension quelconque.

    Entrées:
        A : tuple de float
        B : tuple de float

    Sortie :
        float

    >>> isclose(distance((0, 0), (1, 1)), sqrt(2))
    True
    """

    return sqrt(sum((a - b) ** 2 for a, b in zip(a, b)))


def mosaique(path, power):
    """
    Fonction Mosaique qui transforme une image en un mosaique de l'image composée d'elle meme en différentes couleurs,
    avec une précision prise en paramètre

    :param path: Prend en parametre le chemin vers l'image à transformer
    :param power: Défini la précision de la mosaique
    :return: Image image modifiée
    """
    # ouverture de l'image choisie en paramètre
    image = Image.open(path)
    largeur, hauteur = image.size

    # on crée la matrice de pixels de l'image, vide
    matrice = []

    # ajoute tous les pixels de l'image dans la liste matrice
    for y in range(hauteur):
        ligne_pixels = []
        for x in range(largeur):
            pixel = image.getpixel((x, y))
            ligne_pixels.append(pixel)
        matrice.append(ligne_pixels)

    # défini la taille d'un carreau de la mosaique en fonction du parametre donné
    taille_tile = largeur // power

    # genere les variantes colorées de l'image
    variantes = tiles_generator(path)
    for v in variantes:
        v[0] = v[0].resize(((hauteur // power), (hauteur // power)))

    # on crée la liste des carreaux, vide
    tiles = []

    # Division de l'image en tuiles
    for i in range(hauteur // taille_tile):
        ligne = []
        for j in range(power):
            tile = [matrice[y][x] for x in range(j * taille_tile, (j + 1) * taille_tile) for y in
                    range(i * taille_tile, (i + 1) * taille_tile)]
            ligne.append(tile)
        tiles.append(ligne)

    for i in range(hauteur // taille_tile):
        for j in range(power):
            # Calcul de la couleur moyenne de la tuile
            rouges = [r for (r, _, _) in tiles[i][j]]
            rouge = sum(rouges) // len(rouges)
            verts = [g for (_, g, _) in tiles[i][j]]
            vert = sum(verts) // len(verts)
            bleus = [b for (_, _, b) in tiles[i][j]]
            bleu = sum(bleus) // len(bleus)

            couleur_proche = variantes[0]
            for variante in variantes:
                if distance((rouge, vert, bleu), variante[1]) < distance((rouge, vert, bleu), couleur_proche[1]):
                    couleur_proche = variante

            variante_img = couleur_proche[0]

            # Récupérer les coordonnées de la tuile dans l'image principale
            x_debut = j * taille_tile
            y_debut = i * taille_tile
            x_fin = (j + 1) * taille_tile
            y_fin = (i + 1) * taille_tile

            # Redimensionner la variante à la taille de la tuile
            variante_img = variante_img.resize((x_fin - x_debut, y_fin - y_debut))

            # Coller la variante sur l'image principale aux coordonnées de la tuile
            image.paste(variante_img, (x_debut, y_debut, x_fin, y_fin))

    return image.crop((0, 0, largeur - (largeur % (taille_tile * power)), hauteur - (hauteur % taille_tile)))


if __name__ == '__main__':

    mosaique("../imgs/bois.jpg", 250).save("../rendu/resultat_bois.jpg")
    mosaique("../imgs/hedy.jpg", 250).save("../rendu/resultat_hedy.jpg")
    mosaique("../imgs/pont.jpg", 250).save("../rendu/resultat_pont.jpg")
    mosaique("../imgs/angers.jpg", 250).save("../rendu/resultat_angers.jpg")
    mosaique("../imgs/vitraille.jpg", 250).save("../rendu/resultat_vitraille.jpg")
