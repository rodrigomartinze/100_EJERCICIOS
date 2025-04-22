import unicodedata


def palindromo(texto):

    texto = unicodedata.normalize('NFD', texto)
    

    texto = ''.join(c.lower() for c in texto if c.isalnum())


    return texto == texto[::-1]



print(palindromo('oso'))