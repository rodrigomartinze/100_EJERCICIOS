import string
import re

def palabras_repetidas(text):
    # text = text.replace(",","").replace("-","").replace(".","").replace("!","")
    # text_sin_caracteres = re.sub(r'[@7rR]', '', text)

    sin_signos = str.maketrans('', '', string.punctuation)
    text = text.translate(sin_signos)

    text=tuple(text.lower().split())

    
    
    print(text)
    




    return















text="El viernes pasado fui a la cabaña, pero la cabaña como no tenia luz fui ese mismo viernes mejor a otra cabaña"
palabras_repetidas(text)