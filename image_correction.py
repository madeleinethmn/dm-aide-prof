
   
# Modules et fonctions importés
###############################
from PIL import Image
import numpy


#Exercice 1

# Donne le négatif d'une image

def negatif_image(image_tab):
    """ Fonction qui retourne le négatif d'une image
        Pour chaque pixel, on effectue le calcul 255 - pixel
    """
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            image_tab2[i,j] = -image_tab[i,j] + 255
    return image_tab2

# Jeu de tests   

image_origine = numpy.array([[5, 100], [13, 25], [12, 240]], dtype = numpy.uint8)
image_negative = numpy.array([[250, 155], [242, 230], [243, 15]], dtype = numpy.uint8)

assert numpy.array_equal(negatif_image(image_origine), image_negative)


# Fin jeu de tests


def negatif_image2(image_tab):
    """ Fonction qui retourne le négatif d'une image
        Pour chaque pixel, on effectue le calcul 255 - pixel
    """
    image_tab2 = numpy.array([[-elem + 255 for elem in liste]\
                                           for liste in image_tab],
                             dtype = numpy.uint8)
    return image_tab2
 
# Jeu de tests   
image_origine = numpy.array([[5, 100], [13, 25], [12, 240]], dtype = numpy.uint8)
image_negative = numpy.array([[250, 155], [242, 230], [243, 15]], dtype = numpy.uint8)

assert numpy.array_equal(negatif_image2(image_origine), image_negative)

# Fin jeu de tests


def lumiere(image_tab, x):
    """ Retourne une image éclaire de x ou assombri de x"""
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)                       
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            if image_tab[i, j] > 255 - x:
                nouveau_pixel = 255
            elif image_tab[i, j] < -x:
                nouveau_pixel = 0
            else:
                nouveau_pixel = image_tab[i,j] + x
            image_tab2[i,j] = nouveau_pixel
    return image_tab2


# Jeu de tests   

# test pour la question 2

image_origine = numpy.array([[5, 100], [13, 25], [12, 120]], dtype = numpy.uint8)
image_eclaire= numpy.array([[55, 150], [63, 75], [62, 170]], dtype = numpy.uint8)

assert numpy.array_equal(lumiere(image_origine, 50), image_eclaire)


# test pour la question 3
image_origine = numpy.array([[5, 240], [13, 25], [12, 120]], dtype = numpy.uint8)
image_eclaire = numpy.array([[55, 255], [63, 75], [62, 170]], dtype = numpy.uint8)
image_assombri = numpy.array([[0, 190], [0, 0], [0, 70]], dtype = numpy.uint8)
assert numpy.array_equal(lumiere(image_origine, 50), image_eclaire)
assert numpy.array_equal(lumiere(image_origine, -50), image_assombri)

# Fin jeu de tests



def eclairer(image_tab):
    """ Retourne une image éclairée à l'aide d'une fonction racine carrée"""
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            image_tab2[i, j] = numpy.sqrt(image_tab[i, j] * 255)
    return image_tab2

# Jeu de tests 
image_origine = numpy.array([[5, 100], [13, 25], [12, 120]], dtype = numpy.uint8)
image_eclaire= numpy.array([[35, 159], [57, 79], [55, 174]], dtype = numpy.uint8)


assert numpy.array_equal(eclairer(image_origine), image_eclaire)

# Fin jeu de tests


def assombrir(image_tab):
    """ Retourne une image assombrie à l'aide d'une fonction carrée"""
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            image_tab2[i, j] = (image_tab[i, j]) ** 2 / 255
    return image_tab2
    
# Jeu de tests
image_origine = numpy.array([[5, 100], [13, 25], [12, 120]], dtype = numpy.uint8)
image_assombri= numpy.array([[0, 39], [0, 2], [0, 56]], dtype = numpy.uint8)

assert numpy.array_equal(assombrir(image_origine), image_assombri)


def f(x):
    """ Retourne 128 + signe(x - 128) * sqrt(128 * abs(x - 128))"""
    return int(128 + numpy.sign(x - 128) * numpy.sqrt(128 * abs(x - 128)))


# Jeu de tests

assert f(5) == 2
assert f(128) == 128
assert f(250) == 252

# Fin jeu de tests


def jouer_sur_la_luminosite(image_tab):
    """ Retourne une image à qui on a associé f à chaque pixel"""
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            image_tab2[i, j] = f(image_tab[i, j])
    return image_tab2

# Jeu de tests
image_origine = numpy.array([[5, 100], [13, 25], [12, 120]], dtype = numpy.uint8)
image_finale= numpy.array([[2, 68], [6, 13], [6, 96]], dtype = numpy.uint8)
assert numpy.array_equal(jouer_sur_la_luminosite(image_origine), image_finale)

# Fin jeu de tests



# Exercice 2

def horizontale(image_tab):
    """ Retourne une image qui est symétrique par rapport
        à une droite horizontale de l'image d'origine
    """
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            image_tab2[i, j] = image_tab[-i - 1, j]
    return image_tab2


# Jeu de tests
image_origine = numpy.array([[5, 100], [12, 120]], dtype = numpy.uint8)
image_finale = numpy.array([[12, 120], [5, 100]], dtype = numpy.uint8)
assert numpy.array_equal(horizontale(image_origine), image_finale)

image_origine = numpy.array([[5, 100], [13, 25], [12, 120]], dtype = numpy.uint8)
image_finale = numpy.array([[12, 120], [13, 25], [5, 100]], dtype = numpy.uint8)
assert numpy.array_equal(horizontale(image_origine), image_finale)

# Fin jeu de tests


# Exercice 3 : Flouter une image


def floute_coin_haut_gauche(image_tab, image_tab2):
    """ Floute le coin haut gauche de image_tab
        le résultat est affecté à image_tab2
        Cette fonction ne retourne rien
    """
    somme = 0
    somme += image_tab[0, 0]
    somme += image_tab[1, 0]
    somme += image_tab[0, 1]
    somme += image_tab[1, 1]
    image_tab2[0, 0] = somme // 4

# Jeu de tests
image_origine = numpy.array([[5, 100, 25], [13, 25, 13], [12, 120, 18]],
                            dtype = numpy.uint8)
image_origine2 = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            dtype = numpy.uint8)
image_finale = numpy.array([[35, 0, 0], [0, 0, 0], [0, 0, 0]],
                            dtype = numpy.uint8)
floute_coin_haut_gauche(image_origine, image_origine2)
assert numpy.array_equal(image_origine2, image_finale)

# Fin jeu de tests

def floute_coin_haut_droit(image_tab, image_tab2):
    """ Floute le coin haut droit de image_tab
        le résultat est affecté à image_tab2
        Cette fonction ne retourne rien
    """
    somme = 0
    somme += image_tab[0, -1]
    somme += image_tab[0, -2]
    somme += image_tab[1, -2]
    somme += image_tab[1, -1]
    image_tab2[0, -1] = somme // 4



# Jeu de tests
image_origine = numpy.array([[5, 100, 25], [13, 25, 13], [12, 120, 18]],
                            dtype = numpy.uint8)
image_origine2 = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            dtype = numpy.uint8)
image_finale = numpy.array([[0, 0, 40], [0, 0, 0], [0, 0, 0]],
                            dtype = numpy.uint8)
floute_coin_haut_droit(image_origine, image_origine2)
assert numpy.array_equal(image_origine2, image_finale)

# Fin jeu de tests

def floute_coin_bas_gauche(image_tab, image_tab2):
    """ Floute le coin bas gauche de image_tab
        le résultat est affecté à image_tab2
        Cette fonction ne retourne rien
    """
    somme = 0
    somme += image_tab[-1, 0]
    somme += image_tab[-1, 1]
    somme += image_tab[-2, 0]
    somme += image_tab[-2, 1]
    image_tab2[-1, 0] = somme // 4



# Jeu de tests
image_origine = numpy.array([[5, 100, 25], [13, 25, 13], [12, 120, 18]],
                            dtype = numpy.uint8)
image_origine2 = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            dtype = numpy.uint8)
image_finale = numpy.array([[0, 0, 0], [0, 0, 0], [42, 0, 0]],
                            dtype = numpy.uint8)
floute_coin_bas_gauche(image_origine, image_origine2)
assert numpy.array_equal(image_origine2, image_finale)


# Fin jeu de tests


def floute_coin_bas_droit(image_tab, image_tab2):
    """ Floute le coin bas gauche de image_tab
        le résultat est affecté à image_tab2
        Cette fonction ne retourne rien
    """
    somme = 0
    somme += image_tab[-1, -1]
    somme += image_tab[-1, -2]
    somme += image_tab[-2, -1]
    somme += image_tab[-2, -2]
    image_tab2[-1, -1] = somme // 4



# Jeu de tests
image_origine = numpy.array([[5, 100, 25], [13, 25, 13], [12, 120, 18]],
                            dtype = numpy.uint8)
image_origine2 = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            dtype = numpy.uint8)
image_finale = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 44]],
                            dtype = numpy.uint8)
floute_coin_bas_droit(image_origine, image_origine2)
assert numpy.array_equal(image_origine2, image_finale)


# Fin jeu de tests

def floute_premiere_ligne(image_tab, image_tab2):
    """ Floute la première ligne de image_tab
        sans les coins.
        le résultat est affecté à image_tab2
        Cette fonction ne retourne rien
    """
    nb_colonnes = len(image_tab[0])
    for j in range(1, nb_colonnes - 1):
        somme = 0
        somme += image_tab[0, j - 1]
        somme += image_tab[0, j]
        somme += image_tab[0, j + 1]
        somme += image_tab[1, j - 1]
        somme += image_tab[1, j]
        somme += image_tab[1, j + 1]
        image_tab2[0, j] = somme // 6



# Jeu de tests
image_origine = numpy.array([[5, 100, 25, 13], [13, 25, 13, 25],
                             [12, 120, 18, 36]], dtype = numpy.uint8)
image_origine2 = numpy.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            dtype = numpy.uint8)
image_finale = numpy.array([[0, 30, 33, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            dtype = numpy.uint8)
floute_premiere_ligne(image_origine, image_origine2)
assert numpy.array_equal(image_origine2, image_finale)


# Fin jeu de tests

def floute_derniere_ligne(image_tab, image_tab2):
    """ Floute la dernière ligne de image_tab
        sans les coins.
        le résultat est affecté à image_tab2
        Cette fonction ne retourne rien
    """
    nb_colonnes = len(image_tab[0])
    for j in range(1, nb_colonnes - 1):
        somme = 0
        somme += image_tab[-1, j - 1]
        somme += image_tab[-1, j]
        somme += image_tab[-1, j + 1]
        somme += image_tab[-2, j - 1]
        somme += image_tab[-2, j]
        somme += image_tab[-2, j + 1]
        image_tab2[-1, j] = somme // 6



# Jeu de tests
image_origine = numpy.array([[5, 100, 25, 13], [13, 25, 13, 25],
                             [12, 120, 18, 36]], dtype = numpy.uint8)
image_origine2 = numpy.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                            dtype = numpy.uint8)
image_finale = numpy.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 33, 39, 0]],
                            dtype = numpy.uint8)
floute_derniere_ligne(image_origine, image_origine2)
assert numpy.array_equal(image_origine2, image_finale)


# Fin jeu de tests


def floute_premiere_colonne(image_tab, image_tab2):
    """ Floute la première colonne de image_tab
        sans les coins.
        le résultat est affecté à image_tab2
        Cette fonction ne retourne rien
    """
    nb_lignes = len(image_tab)
    for i in range(1, nb_lignes - 1):
        somme = 0
        somme += image_tab[i - 1, 0]
        somme += image_tab[i, 0]
        somme += image_tab[i + 1, 0]
        somme += image_tab[i - 1, 1]
        somme += image_tab[i, 1]
        somme += image_tab[i + 1, 1]
        image_tab2[i, 0] = somme // 6

# Jeu de tests
image_origine = numpy.array([[5, 100, 25], [13, 13, 25], [13, 25, 12],
                             [120, 18, 36]], dtype = numpy.uint8)
image_origine2 = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            dtype = numpy.uint8)
image_finale = numpy.array([[0, 0, 0], [28, 0, 0], [33, 0, 0], [0, 0, 0]],
                            dtype = numpy.uint8)
floute_premiere_colonne(image_origine, image_origine2)
assert numpy.array_equal(image_origine2, image_finale)


# Fin jeu de tests

def floute_derniere_colonne(image_tab, image_tab2):
    """ Floute la dernière colonne de image_tab
        sans les coins.
        le résultat est affecté à image_tab2
        Cette fonction ne retourne rien
    """
    nb_lignes = len(image_tab)
    for i in range(1, nb_lignes - 1):
        somme = 0
        somme += image_tab[i - 1, -1]
        somme += image_tab[i, -1]
        somme += image_tab[i + 1, -1]
        somme += image_tab[i - 1, -2]
        somme += image_tab[i, -2]
        somme += image_tab[i + 1, -2]
        image_tab2[i, -1] = somme // 6

# Jeu de tests
image_origine = numpy.array([[5, 100, 25], [13, 13, 25], [13, 25, 12],
                             [120, 18, 36]], dtype = numpy.uint8)
image_origine2 = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            dtype = numpy.uint8)
image_finale = numpy.array([[0, 0, 0], [0, 0, 33], [0, 0, 21], [0, 0, 0]],
                            dtype = numpy.uint8)
floute_derniere_colonne(image_origine, image_origine2)
assert numpy.array_equal(image_origine2, image_finale)


# Fin jeu de tests

def floute_centre_image(image_tab, image_tab2):
    """ Floute les pixels de image_tab
        sans le contour (1ère/dernière lignes/colonnes)
        le résultat est affecté à image_tab2
        Cette fonction ne retourne rien
    """
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    for i in range(1, nb_lignes - 1):
        for j in range(1, nb_colonnes - 1):
            somme = 0
            for i2 in range(3):
                for j2 in range(3):
                    somme += image_tab[i - 1 + i2, j - 1 + j2]
            image_tab2[i, j] = somme // 9




# Jeu de tests
image_origine = numpy.array([[5, 100, 25, 18], [13, 13, 25, 100],
                             [13, 100, 200, 200], [120, 18, 36, 150]],
                              dtype = numpy.uint8)
image_origine2 = numpy.array([[0, 0, 0, 0], [0, 0, 0, 0],
                              [0, 0, 0, 0], [0, 0, 0, 0]],
                               dtype = numpy.uint8)
image_finale = numpy.array([[0, 0, 0, 0], [0, 54, 86, 0],
                              [0, 59, 93, 0], [0, 0, 0, 0]],
                               dtype = numpy.uint8)
floute_centre_image(image_origine, image_origine2)
assert numpy.array_equal(image_origine2, image_finale)

# Fin jeu de tests


def floue(image_tab):
    """ Retourne une image floutée
        Précondition : L'image contient au moins 2 lignes et 2 colonnes
    """
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    if nb_lignes < 2 or nb_colonnes < 2: 
        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                image_tab2[i, j] = 255
        return image_tab2
    floute_coin_haut_gauche(image_tab, image_tab2)
    floute_coin_haut_droit(image_tab, image_tab2)
    floute_coin_bas_gauche(image_tab, image_tab2)
    floute_coin_bas_droit(image_tab, image_tab2)
    floute_derniere_ligne(image_tab, image_tab2)
    floute_premiere_ligne(image_tab, image_tab2)
    floute_derniere_colonne(image_tab, image_tab2)
    floute_premiere_colonne(image_tab, image_tab2)
    floute_centre_image(image_tab, image_tab2)
    return image_tab2



#Jeu de tests

# Premier test : On laisse un cadre noir autour de l'image
# La première ligne, première colonne, dernière ligne et dernière colonne
# ne sont pas traitées.
image_origine = numpy.array([[5, 100, 25], [13, 25, 13], [12, 120, 18]],
                            dtype = numpy.uint8)
assert floue(image_origine)[1, 1] == 36


# Second test : On teste le tout
image_origine = numpy.array([[5, 100, 25, 18], [13, 13, 25, 100],
                             [13, 100, 200, 200], [120, 18, 36, 150]],
                              dtype = numpy.uint8)
image_finale = numpy.array([[32, 30, 46, 42], [40, 54, 86, 94],
                            [46, 59, 93, 118], [62, 81, 117, 146]],
                              dtype = numpy.uint8)
assert numpy.array_equal(floue(image_origine), image_finale) 


# Fin jeu de tests

# Exercice 3 : Contour d'une image

def contour(image_tab):
    """ list[list[int]] -> list[list[int]]
        retourne un tableau dont chaque pixel qui n'est pas aux extrem
                 vaut 0 ou 255 en fonction des pixels autour.
                 Le résultat donne un contour.
                 Aux extrémités, on mettra les pixels à 255 (blanc)
    """
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    # Première et dernière colonnes
    for i in range(nb_lignes):
        image_tab2[i, 0] = 255
        image_tab2[i, -1] = 255
    #Première et dernière ligne
    for j in range(nb_colonnes):
        image_tab2[0, j] = 255
        image_tab2[-1, j] = 255
    # Centre de l'image
    for i in range(1, nb_lignes - 1):
        for j in range(1, nb_colonnes - 1):
            somme = 0
            for i2 in range(3):
                for j2 in range(3):
                    somme += image_tab[i - 1 + i2, j - 1 + j2]
            somme =  9 * image_tab[i, j] - somme
            if abs(somme) > 200:
                tmp = 0
            else :
                tmp = 255
            image_tab2[i, j] =  tmp 
    return image_tab2

# Jeux de tests

image_origine = numpy.array([[255]], dtype = numpy.uint8)
image_finale = numpy.array([[255]], dtype = numpy.uint8)
assert numpy.array_equal(contour(image_origine), image_finale)
image_origine = numpy.array([[25, 40, 70], [55, 200, 30], [13, 40, 60]],
                             dtype = numpy.uint8)
image_finale = numpy.array([[255, 255, 255], [255, 0, 255], [255, 255, 255]],
                             dtype = numpy.uint8)
assert numpy.array_equal(contour(image_origine), image_finale)
#Fin jeu de tests


# Exercice 4 : 

def clarte(image_tab):
    """ Retourne une image niveau de gris à partir de l'image couleur image_tab
        en utilisant clarte"""
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            somme = 0
            somme += max(image_tab[i][j])
            somme += min(image_tab[i][j])
            image_tab2[i, j] = somme // 2
    return image_tab2
# Jeux de tests

image_origine = numpy.array([[(150, 200, 100)]], dtype = numpy.uint8)
image_finale = numpy.array([[150]], dtype = numpy.uint8)
assert numpy.array_equal(clarte(image_origine), image_finale)
image_origine = numpy.array([[(25, 40, 70), (55, 200, 30), (13, 40, 60)],
                            [(200, 200, 200), (100, 150, 25), (200, 250, 220)]],
                             dtype = numpy.uint8)
image_finale = numpy.array([[47, 115, 36], [200, 87, 225]],
                             dtype = numpy.uint8)
assert numpy.array_equal(clarte(image_origine), image_finale)
#Fin jeu de tests

def luminosite(image_tab):
    """ Retourne une image niveau de gris à partir de l'image couleur image_tab
        en utilisant luminosité"""
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            somme = 0
            somme += 0.21 * image_tab[i][j][0]
            somme += 0.71 * image_tab[i][j][1]
            somme += 0.71 * image_tab[i][j][2]
            image_tab2[i][j] = somme
    return image_tab2
# Jeux de tests

image_origine = numpy.array([[(150, 200, 100)]], dtype = numpy.uint8)
image_finale = numpy.array([[244]], dtype = numpy.uint8)
assert numpy.array_equal(luminosite(image_origine), image_finale)
image_origine = numpy.array([[(25, 40, 70), (55, 200, 30), (13, 40, 60)],
                            [(200, 200, 200), (100, 150, 25), (200, 250, 220)]],
                             dtype = numpy.uint8)
image_finale = numpy.array([[83, 174, 73], [70, 145, 119]],
                             dtype = numpy.uint8)
assert numpy.array_equal(luminosite(image_origine), image_finale)
#Fin jeu de tests

def moyenne(image_tab):
    """ Retourne une image niveau de gris à partir de l'image couleur image_tab
        en utilisant la moyenne des pixels"""
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            somme = 0
            somme += image_tab[i][j][0]
            somme += image_tab[i][j][1]
            somme += image_tab[i][j][2]
            image_tab2[i][j] = somme // 3
    return image_tab2
# Jeux de tests

image_origine = numpy.array([[(150, 200, 100)]], dtype = numpy.uint8)
image_finale = numpy.array([[150]], dtype = numpy.uint8)
assert numpy.array_equal(moyenne(image_origine), image_finale)
image_origine = numpy.array([[(25, 40, 70), (55, 200, 30), (13, 40, 60)],
                            [(200, 200, 200), (100, 150, 25), (200, 250, 220)]],
                             dtype = numpy.uint8)
image_finale = numpy.array([[45, 95, 37], [200, 91, 223]],
                             dtype = numpy.uint8)
assert numpy.array_equal(moyenne(image_origine), image_finale)
#Fin jeu de tests

def noir_et_blanc(image_tab):
    """ Retourne une image noir et blanc à partir de l'image couleur image_tab
        en utilisant la moyenne des pixels"""
    nb_lignes = len(image_tab)
    nb_colonnes = len(image_tab[0])
    image_tab2 = numpy.zeros([nb_lignes, 
                              nb_colonnes],
                              dtype = numpy.uint8)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            somme = 0
            somme += 0.21 * image_tab[i][j][0]
            somme += 0.71 * image_tab[i][j][1]
            somme += 0.71 * image_tab[i][j][2]
            if somme > 127:
                image_tab2[i][j] = 255
            else:
                image_tab2[i][j] = 0
    return image_tab2
# Jeux de tests

image_origine = numpy.array([[(150, 200, 100)]], dtype = numpy.uint8)
image_finale = numpy.array([[255]], dtype = numpy.uint8)
assert numpy.array_equal(noir_et_blanc(image_origine), image_finale)
image_origine = numpy.array([[(25, 40, 70), (55, 200, 30), (13, 40, 60)],
                            [(200, 200, 200), (100, 150, 25), (200, 250, 220)]],
                             dtype = numpy.uint8)
image_finale = numpy.array([[0, 255, 0], [255, 255, 255]],
                             dtype = numpy.uint8)
assert numpy.array_equal(noir_et_blanc(image_origine), image_finale)
#Fin jeu de tests
        
# Code:
#######


nom = "hoche_niveau_de_gris.jpg"

# On transforme l'image en tableau
image = Image.open(nom)
image.show()

#On transforme l'image en tableau à deux dimensions.
image_tab = numpy.array(image)
# Appel de la fonction negatif_image qui permet de transformer une image
# en son négatif    
image_tab2=contour(image_tab)


## On crée une nouvelle image.
nouvelle_image = Image.fromarray(image_tab2)
nouvelle_image.show()
# On l'enregistre dans un nouveau fichier.
nouvelle_image.save("nouveau_"+nom)




