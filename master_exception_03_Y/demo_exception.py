import string

class Vivant:
    """Class Vivant."""

    def __init__(self, pied, main, nom, age) -> None:
        self.__pied = pied
        self.__main = main
        self.__nom = nom
        self.__age = age
   
    def __str__(self) -> str:
        return f"Humain: Nom:{self.__nom} Pied:{self.__pied} Age:{self.__age} Main:{self.__main}"


def renter_digit(value):
    try:
        if not str(value).isdigit():
            raise ValueError
    except ValueError:
        print("ValueError: Entrer un nombre non une texte.")

# test renter_digit
renter_digit("+5")

def index_list_value(value):
    liste = list(range(1, 10))
    try:
        liste[value]
    except IndexError:
        print(f"IndexError: L'index({value}) ne doit pas depasser la longueure({len(liste)}) de la liste.")

# test index_list_value
index_list_value(11)

def index_dict_value(value):
    num_1 = [str(i) for i in list(range(0, 26))]
    num_2 = [f"0{i}" for i in num_1]
    list_num  = list(num_1 + num_2) 
    dict_1 = dict(zip(list_num, string.ascii_letters))

    try:
        print(dict_1[value])
    except KeyError:
        print(f"KeyError: Key({value}) n'existe pas dans le dictionnaire.")
        dict_1[value] = None

# test index_dict_value
index_dict_value(3)


# Test Instance 
def exception_instance():
    obj_1 = Vivant(2, 2, "JESUS", 33)
    try:
        obj_1._pray
    except AttributeError:
        print("AttributeError: Attribut N'existe pas.")
        setattr(obj_1, 'pray', 'I LOVE YOU JESUS')

# test exception_instance
exception_instance()

def exception_attributes_instance():
    n = Vivant(2, 2, "JESUS", 33)
    try:
        n.__age()
    except AttributeError:
        print("AttributeError: Ceci correspond a un attribut non une fonction.")

# test exception_attributes_instance
exception_attributes_instance()

# MyOwnException
class MyOwnException(Exception):
    pass

def roman_numeral(value):
    try:
        if value not in "IVXLCDM":
            raise MyOwnException
    except MyOwnException:
        print("OwnException: Caractere n'existe pas dans 'IVXLCDM'")

# test roman_numeral
roman_numeral("x")