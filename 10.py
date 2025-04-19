# /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */

# Diccionario de código morse a texto
# MORSE_TO_TEXT = {
#     '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
#     '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
#     '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
#     '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
#     '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
#     '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
#     '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
#     '----.': '9', '--.--': 'Ñ', '': ' '
# }

# def morse_a_texto(morse):
#     palabras = morse.strip().split('  ')

#     texto = ''
#     for palabra in palabras:
#         letras = palabra.strip().split()

#         texto += ''.join(MORSE_TO_TEXT.get(letra, '')for letra in letras)
#         texto += ' '
#     return texto


# print(morse_a_texto(".... --- .-.. .-  -- ..- -. -.. ---" )) 

TEXT_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', 'Ñ': '--.--', ' ': ' '
}

def a_morse(texto):
    palabras = texto.strip().split(' ')

    morse=''

    for palabra in palabras:
        letras = palabra
        morse += ' '.join(TEXT_TO_MORSE.get(letra, '')for letra in letras)
        morse += '  '

    return morse


print(a_morse('HOLA QUE TAL'))

print((TEXT_TO_MORSE.get('R', '')))