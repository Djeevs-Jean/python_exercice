import random

def random_alpha(num):
    if int(num) >= 0 and int(num) <= 26:
        data = []
        for i in "aabcdefghijklmnopqrstuvwxyz":
            if i not in data: data.append(i)
        random.shuffle(data)
        return data[0:num]
    else: print("Entrer entrer un nombre compris la taille de l'alphabet")

# print(random_alpha(27))

def rand_alphanumeric(num):
    if int(num) >= 0 and int(num) <= 36:
        data = []
        for i in "aabcdefghijklmnopqrstuvwxyz0123456789":
            if i not in data: data.append(i)
        random.shuffle(data)
        return data[0:num]
    else: print("Entrer entrer un nombre compris la taille de l'alphabet")

# print(rand_alphanumeric(27))

def generate_to_slug(texte):
    if len(texte)==1: return texte
    else: 
        data = [i for i in texte if str(i).isalnum() or str(i) == '-' or str(i) == ' ']
        return '-'.join(''.join(data).split())

data = "kreye yon fonksyon$ ki pou% jenere yon kòd aleyatwa ki gen n karaktè alfabetik"
# print(generate_to_slug(data))

def comma_string(texte):
    print(','.join(texte))

# data = "fonksyon"
# comma_string(data)

letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
num: int = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)


def letter_tonum(word):
    dict_letter_num = dict(zip(letter, num))
    word = str(word).lower()
    r = '-'.join([str(dict_letter_num.get(i)) for i in word if i in dict_letter_num.keys()])
    print(r)

letter_tonum("CHRIST IS MY LIFE")
letter_tonum("DIEU EST VIVANT")

def num_to_letter(word):
    dict_num_letter = dict(zip(num, letter))
    word = word.split("-") 
    r = '-'.join([str(dict_num_letter.get(int(i))) for i in word if int(i) in dict_num_letter.keys()])


    # if len(word) == 1: r = dict_num_letter.get(int(word))
    # elif len(word) >= 1:
    #     print("JESUS")
    #     r = '-'.join([str(dict_num_letter.get(int(i))) for i in word if int(i) in dict_num_letter.keys()])
    #     # r = [dict_num_letter.get(i) for i in word]
    #     # r = '-'.join([dict_num_letter.get(i) for i in word if i in dict_num_letter.keys()])
    print(r)

num_to_letter("25")
num_to_letter("2-7-17-8-18-19-8-18-12-24-11-8-5-4")
num_to_letter("3-8-4-20-4-18-19-21-8-21-0-13-19")
