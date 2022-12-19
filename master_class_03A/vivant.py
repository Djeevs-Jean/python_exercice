class Vivant:
    """Class Vivant."""

    def __init__(self, pied, main, nom, age) -> None:
        self.__pied = pied
        self.__main = main
        self.__nom = nom
        self.__age = age
   
    def __str__(self) -> str:
        return f"Humain: Nom:{self.__nom} Pied:{self.__pied} Age:{self.__age} Main:{self.__main}"

class Me(Vivant):
    """Class Me."""

    def __init__(self, pied, main, nom, age, prenom, nationaliter) -> None:
        self._prenom = prenom
        self._nationaliter = nationaliter
        super().__init__(pied, main, nom, age)

    def __str__(self) -> str:
        return super().__str__()+ f" Me: Prenom {self._prenom} Nationalier {self._nationaliter}."

class Poule(Vivant):
    """Class Poule."""

    def __init__(self, pied, nom, age, couleur) -> None:
        self._couleur = couleur
        super().__init__(pied, None, nom, age)

    def __str__(self) -> str:
        return super().__str__() + f"\tPoule: de couleur {self._couleur}."


obj_1 = Vivant(2, 2, "HUMAN", 23)
obj_2 = Me(2,2,"DJeevs", 22, "Jean-Yves", "Haitien")

print(obj_1)
print(obj_2)

obj_poule = Poule(2, "Poule Haitien", 2, "Brown")
print(obj_poule)
