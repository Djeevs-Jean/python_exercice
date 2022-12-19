class Vivant:
    """Class Vivant."""

    def __init__(self, pied, main, nom, age) -> None:
        self.__pied = pied
        self.__main = main
        self.__nom = nom
        self.__age = age
   
    def __str__(self) -> str:
        return f"Humain: Nom:{self.__nom} Pied:{self.__pied} Age:{self.__age} Main:{self.__main}"
