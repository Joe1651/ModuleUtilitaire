from Console.console_utils import *


class Rectangle:
    # CONSTRUCTEUR
    def __init__(self, longueur: float, largeur: float):
        if longueur <= 0 or largeur <= 0:
            raise ValueError("Les dimensions du rectangles doivent être supérieure à 0.")
        self.__longueur = longueur
        self.__largeur = largeur

    # PROPRIÉTÉS
    @property
    def diagonale(self):
        return (self.__longueur ** 2 * self.__largeur ** 2) ** 0.5

    # MÉTHODES
    def calculer_aire(self):
        return self.__largeur * self.__longueur

    def calculer_périmètre(self):
        return 2 * self.__largeur + 2 * self.__longueur

    def obtenir_description(self):
        return f"Rectangle de {self.__largeur} de largeur et de {self.__longueur} de longueur."

    # OVERRIDES
    def __str__(self):
        return self.obtenir_description()


if __name__ == '__main__':
    colored_print("Ne pas exécuter ce fichier", "red", attributs=["bold"])
