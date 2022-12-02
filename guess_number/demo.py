import random
import sys

def input_number() -> int:
    num = input("Entrer un nombre compris entre 0 et 500: ")
    if num.isdigit() and (int(num) >=0 and int(num) <=500):
        return int(num)
    else:
        print("Error input: entrer un nombre valide...\n") 
        return input_number() 

def random_number() -> int:
    return random.randint(0, 500)

def to_continue(value: int=2)-> bool:
    ch = input("Voulez-vous continuer (1: continuer; 2: quitter): ")
    if ch.isdigit(): return True if int(ch)==1 else False
    return to_continue()

def run():
    const = True
    luck = 5
    while const:
        print("-"*70)
        if luck > 0:
            random_num = random_number()
            user_input = input_number()
            if user_input < random_num:
                print(f"Le nombre aléatoire est: {random_num} - vous avez choisi {user_input} - le nombre que vous avez choisi est trop petit.")
            elif user_input > random_num:
                print(f"Le nombre aléatoire est: {random_num} - vous avez choisi {user_input} - le nombre que vous avez choisi est trop grand.")
            elif user_input == random_num:
                print(f"Le nombre aléatoire est: {random_num} - vous avez choisi {user_input} - vous avez gagnez.")
                luck = 5
                r = to_continue()
                if r: continue
                else: sys.exit()
            luck -= 1
            print(f"Il vous reste {luck} chances.\n".format())
        else: 
            const = False

run()