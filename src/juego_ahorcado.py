import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    # TODO: Implementa esta función (y elimina la instrucción pass)
    texto = cadena.lower().strip()

    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("Á", "A")
    texto = texto.replace("É", "E")
    texto = texto.replace("Í", "I")
    texto = texto.replace("Ó", "O")
    texto = texto.replace("Ú", "U")
    texto = texto.replace("ä", "a")
    texto = texto.replace("ë", "e")
    texto = texto.replace("ï", "i")
    texto = texto.replace("ö", "o")
    texto = texto.replace("ü", "u")
    texto = texto.replace("Ä", "A")
    texto = texto.replace("Ë", "E")
    texto = texto.replace("Ï", "I")
    texto = texto.replace("Ö", "O")
    texto = texto.replace("Ü", "U")

    return texto



def ocultar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    # TODO: Implementa esta función (y elimina la instrucción pass)
    resultado = ""
    for letra in palabra_secreta:
        if letra in letras_usadas:
            resultado += letra
        else:
            resultado += "_"

    return resultado
            



def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    # TODO: Implementa esta función (y elimina la instrucción pass)
    abecedario = "abcdefghijklmnñopqrtukvwxyz"
    for letra in palabra_enmascarada.lower():
        if letra not in abecedario:
            return(False)
    return(True)

# TODO: Implementa la función mostrar_estado
def mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes):
    abecedario = "abcdefghijklmnñopqrtukvwxyz"
    for letras_usadas in abecedario:
        if letras_usadas 

# TODO: Implementa la función pedir_letra

# TODO: Implementa la función jugar

# TODO: Escribe el programa principal