import random
LETTERS = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
NUMBERS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25")

def random_alpha(num:int):
    if int(num) >= 0 and int(num) <= 26:
        data = []
        d = [data.append(i) for i in LETTERS if i not in data]
        random.shuffle(data)
        return '_'.join(data[0:num])
    else: return "Entrer entrer un nombre compris la taille de l'alphabet"

# test random_alpha

def random_alphanumeric(num:int):
    if int(num) >= 0 and int(num) <= 26:
        H = LETTERS + NUMBERS
        data = []
        d = [data.append(i) for i in H if i not in data]
        random.shuffle(data)
        return '_'.join(data[0:num])
    else: return "Entrer entrer un nombre compris la taille de l'alphabet"

# test random_alphanumeric

def slugify(word:str):
    word = '-'.join(word.split()) 
    word = ''.join([i for i in word if i.isalnum() or i == '-'])
    return word

# test slugify

def separate_letter_with_commas(word:str)->None:
    return ','.join(word)

# test separate_letter_with_commas

def encrypt_words(word:str):
    """function -> encrypt words."""
    word = str(word).lower()
    dict_let_num = dict(zip(LETTERS, NUMBERS))
    res = '-'.join([str(dict_let_num.get(i)) for i in word if i in dict_let_num.keys()])
    return res

# test encrypt_words

def decrypt_words(word:str):
    """function -> decrypt words."""
    dict_num_letter = dict(zip(NUMBERS, LETTERS))
    word = word.split("-") 
    res = ''.join([dict_num_letter.get(i) for i in word if i in dict_num_letter.keys()])
    return res

# test decrypt_words

def swap_values(a, b)-> tuple:
    """function -> swap 2 values return tuple"""
    return b, a

# test swap_values

def compound_names(nom:str)->str:
    """function -> Nom Composé."""
    name = [i[0] for i in nom.replace("-", " ").split()]
    return "".join(name)
    
# test compound_names

print(
    random_alpha(22), "\n\n",
    random_alphanumeric(17), "\n\n",
    slugify("Kreye yon fonksyon^ ki ap dekripte$$ yon mo ki fèt ak endèks chak lèt nan alfabè a"), "\n\n",
    separate_letter_with_commas("fonksyon fonksyon"), "\n\n",
    encrypt_words("CHRIST IS MY LIFE"), "\n\n",
    encrypt_words("DIEU EST VIVANT"), "\n\n",
    decrypt_words("25"), "\n\n",
    decrypt_words("2-7-17-8-18-19-8-18-12-24-11-8-5-4"), "\n\n",
    decrypt_words("3-8-4-20-4-18-19-21-8-21-0-13-19"), "\n\n",
    swap_values(4,5), "\n\n",
    compound_names("Jean-Baptiste Jean"), "\n\n",
)