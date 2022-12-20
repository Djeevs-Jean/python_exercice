import string

def dict_letters_numbers()->dict[str, str]:
    num_1 = [str(i) for i in list(range(0, 26))]
    num_2 = [f"0{i}" for i in num_1]
    list_num  = list(num_1 + num_2) 
    return dict(zip(list_num, string.ascii_letters))


def encrypt_words_lower_upper(word:str):
    """function -> encrypt words."""
    word = str(word)
    dict_let_num = dict(zip(dict_letters_numbers().values(), dict_letters_numbers().keys()))

    print(dict_let_num)
    res = '-'.join([dict_let_num.get(i) for i in word if i in dict_let_num.keys()])
    print(res)

# test decrypt_words
encrypt_words_lower_upper("ALO")

def decrypt_words_lower_upper(word:str):
    """function -> decrypt words."""
    dict_num_letter = dict_letters_numbers()
    word = word.split("-") 
    res = ''.join([dict_num_letter.get(i) for i in word if i in dict_num_letter.keys()])
    print(res)

# test decrypt_words
decrypt_words_lower_upper("0-011-014")
