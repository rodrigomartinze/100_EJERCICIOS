"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

def area_poligono(tipo, base, altura):
    if tipo == "triangulo":
        return (base * altura) / 2
    elif tipo == "cuadrado":
        return base * base
    elif tipo == "rectangulo":
        return base * altura
    else:
        return "Tipo de polígono no soportado"
    
print(area_poligono("triangulo", 5, 10))
print(area_poligono("cuadrado", 12, 0))
print(area_poligono("rectangulo", 4, 10))


