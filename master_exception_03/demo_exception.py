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


def renter_digit():
    num = input("Entrer un chiffre: ")
    if not num.isdigit(): 
        raise Exception("Vous devriez entrer un nombre.")
# test
renter_digit()

def index_list_value(value):
    liste = list(range(1, 10))
    try:
        return liste[value]
    except IndexError:
        print("Vous avez depasse la limite de l'index.")
# test
index_list_value(11)

def index_dict_value(value):
    num_1 = [str(i) for i in list(range(0, 26))]
    num_2 = [f"0{i}" for i in num_1]
    list_num  = list(num_1 + num_2) 
    dict_1 = dict(zip(list_num, string.ascii_letters))

    try:
        print(dict_1["0112"])
    except:
        print("Key: None Value: None")
        dict_1["None"] = 'None'
        print(dict_1["None"])
# test
index_dict_value(3)


""" Test Instance """
def exception_instance():
    instance_test = Vivant(2, 2, "JESUS", 33)
    try:
        print(instance_test._pray)
    except:
        print("Attributes doesn't exit, it will be add.")
        setattr(instance_test, '_pray', 'i pray God')
        print(instance_test._pray)
# test
exception_instance()

def exception_attributes_instance():
    n = Vivant(2, 2, "JESUS", 33)
    try:
        n_1 = n.__age()
    except AttributeError:
        print("Ce n'est pas une fonction.")
# test
exception_attributes_instance()

class MyOwnException(Exception):
    pass

def roman_numeral():
    
    num = input("Entrer un chiffre: ")
    if num not in "IVXLCDM":
        raise MyOwnException("Value not exists.")
# test
roman_numeral()