"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

for i in range(0,101):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)