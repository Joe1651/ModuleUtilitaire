import math
from abc import abstractmethod, ABC
from utilpy.Console.console_utils import *


class Forme(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError("Une forme c'est abstrait, on ne peut pas en construire.")

    def aire(self):
        pass

    def périmètre(self):
        pass


class Rectangle(Forme, ABC):
    # CONSTRUCTEUR
    def __init__(self, longueur: float, largeur: float):
        if longueur <= 0 or largeur <= 0:
            raise ValueError("Les dimensions du rectangles doivent être supérieure à 0.")
        self.__longueur = longueur
        self.__largeur = largeur

    # PROPRIÉTÉS
    @property
    def diagonale(self):
        return (self.__longueur ** 2 + self.__largeur ** 2) ** 0.5

    # MÉTHODES
    @property
    def aire(self):
        return self.__largeur * self.__longueur

    def périmètre(self):
        return 2 * self.__largeur + 2 * self.__longueur

    def obtenir_description(self):
        return (f"Rectangle de {self.__largeur} de largeur et de {self.__longueur} de longueur, pour une aire de "
                f"{self.aire}.")

    # OVERRIDES
    def __str__(self):
        return self.obtenir_description()


class Cercle(Forme, ABC):
    def __init__(self, rayon=1):
        self.__rayon = rayon

    def aire(self):
        return math.pi * self.__rayon ** 2

    def périmètre(self):
        return 2 * math.pi * self.__rayon

    def __str__(self):
        return (f"Ceci est un rayon de {self.__rayon}m de rayon, avec une aire de {self.aire()}m2 et un périmètre de "
                f"{self.périmètre()}m")


if __name__ == '__main__':
    colored_print("Ne pas exécuter ce fichier", "red", attributs=["bold"])
