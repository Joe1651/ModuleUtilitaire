# Module contenant les fonctions utilitaires qui
# interagissent avec la console (input, print)
import os

# Essayez de garder les fonctions en ordre alphabétique
# pour que ce soit plus simple pour vous et pour vous retrouver

# Au besoin, utilisez l'onglet "Structure" de PyCharm pour
# voir facilement la liste des fonctions

import termcolor  # Test salut

os.environ["FORCE_COLOR"] = "1"


def colored_print(message: str, color: str = None, surlignage: str = None, attributs: list = None):  # Salut
    print(termcolor.colored(message, color, on_color=surlignage, attrs=attributs))


def confirmer(question: str = "Voulez-vous confirmer (O/N) ?") -> bool:
    """
    Demande une confirmation O/N à l'utilisateur
    :param question: si vous fournissez la question, elle doit aussi afficher les choix
                     valides (O ou N) pour indiquer à l'utilisateur ce qui est valide
    :return: vrai si l'utilisateur a confirmé (O ou o)
    """
    réponse = lire_caractère_selon_ensemble(question, "OoNn")
    if réponse.upper() == "O":
        return True
    elif réponse.upper() == "N":
        return False


def lire_caractère(question: str) -> str:
    while True:
        saisie = input(question)
        if len(saisie) == 1 and saisie.isalpha():
            break
        colored_print("Veuillez saisir un seul caractère", "red", attributs=["bold"])

    return saisie


def lire_caractère_selon_ensemble(question: str, ensemble: str) -> str:
    """
    Comme lire_caractère, mais le caractère sera validé pour
    être certain qu'il est présent dans l'ensemble de caractères valides.
    """
    while True:
        saisie = input(question).upper()
        if len(saisie) == 1 and saisie.isalpha() and saisie in ensemble:
            break
        colored_print(f"Veuillez saisir un des caractères suivants: {ensemble}", "red", attributs=["bold"])

    return saisie


def lire_chaine(question: str) -> str:
    """
    :param question: la question à poser
    :return: valide et retourne une chaine non vide après avoir
             retiré les espaces initiaux et ceux de la fin (strip)
    """
    while True:
        chaine = input(question).strip()
        if len(chaine) > 0:
            break
        colored_print(f"Veuillez saisir une réponse non-vide.", "red", attributs=["bold"])

    return chaine


def lire_chaine_str(question: str) -> str:
    """
    :param question: la question à poser
    :return: valide et retourne une chaine non vide après avoir
             retiré les espaces initiaux et ceux de la fin (strip)
    """
    while True:
        chaine = input(question).strip()
        if len(chaine) > 0 and all([not c.isdigit() for c in chaine]):
            break
        colored_print(f"Veuillez saisir une réponse non-vide sans int ou float.", "red", attributs=["bold"])

    return chaine


def lire_chaine_taille_intervalle(question: str, taille_min: int, taille_max: int) -> str:
    """
    :param question: la question à poser
    :param taille_min: la taille minimum que doit avoir la chaine de retour
    :param taille_max: la taille maximum
    :return: une chaine avec longueur dans l'intervalle spécifié.
    """
    while True:
        chaine = input(question).strip()
        if taille_min <= len(chaine) <= taille_max:
            break
        colored_print(f"Veuillez saisir une réponse entre {taille_min} et {taille_max} caractères.", "red", attributs=["bold"])

    return chaine


def lire_entier(question: str) -> int:
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            break
        except ValueError:
            colored_print("Veuillez saisir un entier seulement.", "red", attributs=["bold"])
    return entier


def lire_entier_pair(question: str) -> int:
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            if entier % 2 == 0:
                break
        except ValueError:
            pass
        colored_print("Veuillez saisir un entier pair.", "red", attributs=["bold"])
    return entier


def lire_entier_positif(question: str) -> int:
    while True:
        # PMC lire_entier_positif(), tu devrais réutiliser lire_entier() et valider après
        saisie = input(question)
        try:
            entier_positif = int(saisie)
            if int(entier_positif) >= 0: break
        except ValueError:
            pass
        colored_print("Veuillez saisir un entier positif.", "red", attributs=["bold"])

    return entier_positif


def lire_entier_impair(question: str) -> int:
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            if entier % 2 != 0:
                break
        except ValueError:
            pass
        colored_print("Veuillez saisir un entier impair.", "red", attributs=["bold"])
    return entier


def lire_entier_intervalle(question: str, minimum: int, maximum: int) -> int:
    """
    Pose la question et retourne un entier validé, selon l'intervalle spécifié.

    :param question:  La question à poser
    :param minimum: La valeur minimum inclusivement
    :param maximum: Inclusivement aussi
    :return: L'entier validé selon l'intervalle.
    """
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            if minimum <= entier <= maximum: break
        except ValueError:
            pass
        colored_print(f"Veuillez saisir un entier entre {minimum} et {maximum}.", "red", attributs=["bold"])
    return entier


def lire_entier_minimum(question: str, minimum: int) -> int:
    """
    Pose la question et retourne un entier validé, selon l'intervalle spécifié.

    :param question:  La question à poser
    :param minimum: La valeur minimum inclusivement
    :return: L'entier validé selon l'intervalle.
    """
    while True:
        saisie = input(question)
        try:
            entier = int(saisie)
            if minimum <= entier: break
        except ValueError:
            pass
        colored_print(f"Veuillez saisir un entier supérieur à {minimum}.", "red", attributs=["bold"])
    return entier  # test


def lire_réel(question: str) -> float:
    """
    Cette fonction s'assure que le bon séparateur décimal est utilisé
    et obtient un nombre réel validé.

    :param question:
    :return: Le nombre réel
    """
    while True:
        saisie = input(question)
        try:
            réel = float(saisie)
            break
        except ValueError:
            colored_print("Veuillez saisir un réel seulement.", "red", attributs=["bold"])

    return réel


# important de mettre une garde d'importation
if __name__ == '__main__':
    print(
        "Vous ne devriez pas démarrer ce fichier directement. Utilisez le sondage pour tester vos fonctions "
        "utilitaires")