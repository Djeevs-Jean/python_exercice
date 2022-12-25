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

    main = 2
    pied = 2
    def __init__(self, nom, age, degree) -> None:
        main = Student.main
        pied = Student.pied
        self._degree = degree
        super().__init__(pied, main, nom, age)

    def __str__(self) -> str:
        return super().__str__()+ f" Student: Degree:{self._degree}."

class Poule(Vivant):
    """Class Poule."""

    pied = 2
    main = 0
    def __init__(self, nom, age, couleur) -> None:
        pied = Poule.pied
        main = Poule.main
        self._couleur = couleur
        super().__init__(pied, main, nom, age)

    def __str__(self) -> str:
        return super().__str__() + f" Poule: de couleur {self._couleur}."

# test 

obj_1 = Vivant(2, 2, "HUMAN", 23)
obj_2 = Student("Jhon", 22, "LICENCE")

print(obj_1)
print(obj_2)

obj_poule = Poule("Poule Haitienne", 2, "Brown")
print(obj_poule)