# /*
#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.
#  */

def caracteres_no_repetidos(str1,str2):

    out1=''.join(c for c in str1 if c not in str2)
    out2=''.join(c for c in str2 if c not in str1)


    print(out1,' ',out2)


caracteres_no_repetidos('hola','mundo')