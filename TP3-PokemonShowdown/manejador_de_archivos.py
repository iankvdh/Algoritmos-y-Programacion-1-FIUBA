import csv

def cargar_tipos(RUTA_ARCHIVO_TIPOS):
    """
    Abre tabla_tipos.csv y devuelve toda
    la info como dicionario de diccionarios
    """
    dic_tipos = {}
    lista = []
    with open(RUTA_ARCHIVO_TIPOS) as f:
        csv_read = csv.DictReader(f, delimiter= ";")
        for i, dic in enumerate(csv_read):
            lista.append(dic)
            mov = lista[i].pop("Types")
            dic_tipos[mov] = lista[i]
    return dic_tipos

def cargar_detalle_movimientos(RUTA_ARCHIVO_DETALLE):
    """
    Recibe detalle_movimientos.csv y devuelve
    una lista con todos los movimientos con
    sus atributos como diccionarios
    """
    lista_movimientos = []
    dic_detalle_mov = {}
    with open(RUTA_ARCHIVO_DETALLE) as f:
        csv_read = csv.DictReader(f, delimiter= ",")
        for i, dic in enumerate(csv_read):
            lista_movimientos.append(dic)
            mov = lista_movimientos[i].pop("nombre")
            dic_detalle_mov[mov] = lista_movimientos[i]
    return dic_detalle_mov

def cargar_pokemones(RUTA_ARCHIVO_POKEMONES):
    """
    Recibe pokemones.csv y devuelve
    un diccionario donde las claves son los pokemones y los valores 
    son diccionarios con sus caracteristicas
    """
    lista_movimientos = []
    dic_detalle_mov = {}
    with open(RUTA_ARCHIVO_POKEMONES) as f:
        csv_read = csv.DictReader(f, delimiter= ";")
        for i, dic in enumerate(csv_read):
            lista_movimientos.append(dic)
            mov = lista_movimientos[i].pop("nombre")
            dic_detalle_mov[mov] = lista_movimientos[i]
    return dic_detalle_mov

def cargar_equipos(RUTA_ARCHIVO_EQUIPOS):
    """
    Abre el archivo equipos.txt, copia
    la informacion a un diccionario
    y lo retorna.
    Si el archivo no existe lo crea y retorna
    un diccionario vacio.
    """
    informacion_equipos = {}
    with open(RUTA_ARCHIVO_EQUIPOS, "r") as f:
        for linea in f:
            equipo_a_agregar = {}
            equipo, pokemones = linea.split(";")
            lista_pokemones_con_movimientos = pokemones.split("*")
            for pokemon_movimientos in lista_pokemones_con_movimientos:
                if pokemon_movimientos != "\n": 
                    pokemon, movimientos = pokemon_movimientos.split(":")
                    movimientos = movimientos.rstrip().split(",")
                    equipo_a_agregar[pokemon] = movimientos
                informacion_equipos[equipo] = equipo_a_agregar 
    return informacion_equipos
