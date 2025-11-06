
"""
* Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""


#Función que determina si dos textos son anagramas
def es_un_anagrama(texto1, texto2):
    if texto1.lower() == texto2.lower():
        return False
    
    texto1 = texto1.replace(" ", "").lower()
    texto2 = texto2.replace(" ", "").lower()
    return sorted(texto1) == sorted(texto2)

#main
continua = True

while continua:
    Texto1 = input("Ingrese el texto #1: ")
    Texto2 = input("Ingrese el texto #2: ")
    
    print(es_un_anagrama(Texto1, Texto2))
    
    seguir = input("¿Desea continuar? (s/n): ")
    if seguir.lower() != 's':
        continua = False






