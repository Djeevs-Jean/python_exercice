import re

DATA_TEXT = "Je suis allé #visiter la tour #Eiffel hier! C'était incroyable #Paris. Je vais certainement y retourner! #"

def replace_hashtag_by_link(value):
    return re.sub("#[\w]+", lambda x: "<a href=''>{}</a>".format(x.group()), value)

print(replace_hashtag_by_link(DATA_TEXT))
