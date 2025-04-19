""" * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente."""

def contar_palabras(texto): 
    texto = texto.lower()
    palabras = ""
    for i in range(len(texto)):
        if texto[i] == " " or texto[i] == "," or texto[i] == ".":
            palabras += " "
        else:
            palabras += texto[i]
    palabras = palabras.split(" ")
    contador = {}
    for palabra in palabras:
        if palabra != "":
            if palabra in contador:
                contador[palabra] += 1
            else:
                contador[palabra] = 1
    return print( contador)

contar_palabras("Hola, mundo. Hola tierra mundo. Hola, mundo. jaja que tal")



