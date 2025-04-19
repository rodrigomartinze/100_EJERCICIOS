# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */

def a_biniario(n):
    if n == 0:
        return '0'
    n_biniario = ''
    
    while n > 0:
        n_biniario = (str(n % 2)+ n_biniario)
        n = n // 2
    return n_biniario


print(a_biniario(42))

