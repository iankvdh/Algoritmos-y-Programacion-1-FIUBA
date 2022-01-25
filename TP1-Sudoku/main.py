from sudoku import crear_juego, es_movimiento_valido, insertar_valor, esta_terminado
from mapas import MAPAS
import random

def imprimir_fila(lista):
    """dada una lista, la imprime con referencias para cada fila y separaciones horizontales"""
    texto = "abcdefghi"
    for i in range(len(lista)):
        if i == 3 or i == 6:
            print("  [──────────────────────────]  ")
        print(texto[i] + " " + str(lista[i])+ " " + texto[i])

def imprimir_juegos(lista):
    """Dada una lista con 9 listas, de nueve elementos. 
    Imprime un sudoku con referencias verticales y horizontales y divisiones por regiones"""
    #INVOCA A: imprimir_fila()
    lista2 = []
    juego = lista
    numeracion = ("    0 1 2    3 4 5    6 7 8  ")
    print(numeracion)
    borde_horizontal = "  ────────────────────────────  " 
    print(borde_horizontal)
    for filas in juego:
        cadena = ""
        cadena_nueva = ""
        for element in filas:
            cadena += str(element) + " "
        for i in range(len(cadena)):
            if i == 5 or i == 10:
                cadena_nueva += cadena[i] + " | "
            else:
                cadena_nueva += cadena[i]
        lista = []
        lista.append(cadena_nueva)
        lista2.append(lista)
    imprimir_fila(lista2)
    print(borde_horizontal)
    print(numeracion)

def elegir_mapa(MAPAS):
    """elige un mapa random"""
    return random.choice(MAPAS)

def sudoku_crear(mapa):
    """Dado un mapa, crea un sudoku random y lo imprime"""
    #INVOCA A: imprimir_juegos() 
    juego = crear_juego(mapa)
    imprimir_juegos(juego)

def es_numero(cadena):
    """verifica que lo ingresado sea un numero entre 0 y 9"""
    numeros = "123456789"
    if len(cadena) == 1 and cadena != "":
        if cadena in numeros:
            return True
    return False

def es_letra_valida(l):
    """verifica que lo ingresado sea una letra entre a e i"""
    texto = "abcdefghi"
    if l in texto:
        return True

def convertir_letra_a_numero(l):
    """convierte las primeras nueve letras del abecedario en su posición equivalente en el mismo"""
    numeros = (0,1,2,3,4,5,6,7,8)
    letras = "abcdefghi"
    posicion = letras.index(l) 
    return numeros[posicion]

def pedir_valores():
    """pide al usuario ingresar fila, columna, y valor y verifica que los datos ingresados 
    sean válidos. En caso de haber ingresado salir, devuelve -1 para cada elemento"""
    #INVOCA A: es_letra_valida(), es_numero()
    while True:
        fila = input("ingrse fila / salir: ")
        if fila == "salir":
            break
        if not es_letra_valida(fila):
            print("POR FAVOR INGRESE UN VALOR VÁLIDO: ")
            continue
        else:
            columna = input("ingrese columna / salir: ")
            if columna == "salir":
                break
            if not es_numero(columna) or columna == "9":
                print("POR FAVOR INGRESE UN VALOR VÁLIDO: ")
                continue
            else:
                valor = input("ingrese valor / salir: ")
                if valor == "salir":
                    break
                if not es_numero(valor):
                    print("POR FAVOR INGRESE UN VALOR VÁLIDO: ")
                    continue
        return fila, columna, valor
    return (-1, -1, -1)

def main():
    """ejecuta el sudoku y mezcla las funciones anteriores"""
    mapa = elegir_mapa(MAPAS)
    sudoku_crear(mapa)
    juego = crear_juego(mapa)

    while True:
        fila, columna, valor = pedir_valores()
        if fila == -1 or columna == -1 or valor == -1:
            break
        fila = convertir_letra_a_numero(fila)
        columna = int(columna)
        valor = int(valor)
        if es_movimiento_valido(juego, fila, columna, valor):
            juego = insertar_valor(juego, fila, columna, valor)
            imprimir_juegos(juego)
        else:
            print("El movimiento no es valido: ")
        if esta_terminado(juego):
            print("¡¡¡¡¡FELICIDADES, GANASTE!!!!!")
            break
main()