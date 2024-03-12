import re


def code_postal_valide(code_postal:str):
    return re.fullmatch(r"^[A-Z]\d[A-Z] ?\d[A-Z]\d$", code_postal) is not None


def num_téléphone_valide(num_téléphone: str):
    return re.fullmatch(r"[(]?\d\d\d[)]?[ -]\d\d\d-\d\d\d\d", num_téléphone) is not None


assert code_postal_valide("J3L 0C6")
assert num_téléphone_valide("450 447-7059")
