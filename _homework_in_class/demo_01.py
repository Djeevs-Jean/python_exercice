LETTERS = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
NUMBERS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "010", "011", "012", "013", "014", "015", "016", "017", "018", "019", "020", "021", "022", "023", "024", "025")

def encrypt_words_lower_upper(word:str):
    """function -> encrypt words."""
    word = str(word)
    dict_let_num = dict(zip(LETTERS, NUMBERS))
    res = '-'.join([str(dict_let_num.get(i)) for i in word if i in dict_let_num.keys()])
    print(res)

# test decrypt_words
encrypt_words_lower_upper("ALO")

def decrypt_words_lower_upper(word:str):
    """function -> decrypt words."""
    dict_num_letter = dict(zip(NUMBERS, LETTERS))
    word = word.split("-") 
    res = ''.join([dict_num_letter.get(i) for i in word if i in dict_num_letter.keys()])
    print(res)

# test decrypt_words
decrypt_words_lower_upper("0-011-014")
