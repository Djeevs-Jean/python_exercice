class Vivant:
    """Class Vivant."""

    def __init__(self, pied, main, nom, age) -> None:
        self.__pied = pied
        self.__main = main
        self.__nom = nom
        self.__age = age
   
    def __str__(self) -> str:
        return f"Humain: Nom:{self.__nom} Pied:{self.__pied} Age:{self.__age} Main:{self.__main}"

class Student(Vivant):
    """Class Student."""

    def __init__(self, pied, main, nom, age, prenom, nationaliter, degree) -> None:
        self._prenom = prenom
        self._nationaliter = nationaliter
        self._degree = degree
        super().__init__(pied, main, nom, age)

    def __str__(self) -> str:
        return super().__str__()+ f" Student: Prenom {self._prenom} Nationaliter:{self._nationaliter} Degree:{self._degree}."

class Poule(Vivant):
    """Class Poule."""

    def __init__(self, pied, nom, age, couleur) -> None:
        self._couleur = couleur
        super().__init__(pied, None, nom, age)

    def __str__(self) -> str:
        return super().__str__() + f" Poule: de couleur {self._couleur}."

# test 

obj_1 = Vivant(2, 2, "HUMAN", 23)
obj_2 = Student(2,2,"Jhon", 22, "Doe", "Haitien", "LICENCE")

print(obj_1)
print(obj_2)

obj_poule = Poule(2, "Poule Haitienne", 2, "Brown")
print(obj_poule)