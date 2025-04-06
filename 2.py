"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """

def anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")

    if len(palabra1) != len(palabra2):
        print(False)
        exit()
    palabra1 = sorted(palabra1)
    palabra2 = sorted(palabra2)
    for i in palabra1:
        if palabra1.count(i) != palabra2.count(i):
            print(False)
            exit()

    print(True)

anagramas("gfedacb", "abcdefg")