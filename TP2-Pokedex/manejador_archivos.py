import csv

"""
Si interfaz funciona, hay que ver que ande todo aca
borrando archivo_existe de todos lados
"""

# ABRIR POKEMONES.CSV
def cargar_pokemones(RUTA_ARCHIVO_POKEMONES):
    """
    Recibe pokemones.csv y devuelve
    una lista con todos los pokemones con
    sus atributos como diccionarios
    """
    pokelista = []
    with open(RUTA_ARCHIVO_POKEMONES) as f:
        csv_read = csv.DictReader(f, delimiter= ";")
        for pokedic in csv_read:
            pokelista.append(pokedic)
    return pokelista
   
# ABRIR MOVIMIENTOS.CSV
def todos_los_movimientos(RUTA_ARCHIVO_MOVIMIENTOS):
    """
    Recibe movimientos.csv y devuelve una lista
    de diccionarios donde la clave es el nombre
    de cada pokemon y el valor una lista
    de sus movimientos
    """
    lista = []
    with open(RUTA_ARCHIVO_MOVIMIENTOS) as f:
        csv_read = csv.DictReader(f, delimiter= ";")
        for dic in csv_read:
            pokemon = dic["pokemon"]
            pokemon = pokemon[0].upper() + pokemon[1:].lower()
            diccionario = {}
            diccionario[pokemon] = dic['movimientos'].split(",")
            lista.append(diccionario)
    return lista

def lista_todos_pokemones(RUTA_ARCHIVO_POKEMONES):
    """
    Recibe el archivo pokemones.csv y devuelve
    una lista con los nombres
    """
    nombres = [] 
    with open(RUTA_ARCHIVO_POKEMONES) as f:
        csv_read = csv.DictReader(f, delimiter= ";")
        for  dic in csv_read: 
            nombres.append(dic["nombre"].lower()) 
    return nombres

def cargar(RUTA_ARCHIVO_EQUIPOS):
    """
    Abre el archivo equipos.txt, copia
    la informacion a un diccionario
    y lo retorna.
    Si el archivo no existe lo crea y retorna
    un diccionario vacio.
    """
    informacion_equipos = {}
    try:
        with open(RUTA_ARCHIVO_EQUIPOS, "r") as f:
        # copio toda la info a una variable para poder usarla
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
    except:
        with open(RUTA_ARCHIVO_EQUIPOS, "w") as f:
            pass
    return informacion_equipos

def archivo_existe(archivo):
    """
    Recibe un archivo y verifica que
    exista
    """
    try:
        with open(archivo, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def cargar_pokemon_indice(RUTA_ARCHIVO_POKEMONES):
    """
    Recibe pokemones.csv y devuelve
    yb diccionario con todos los pokemones como clave 
    e indice como valor
    """
    pokedic = {}
    with open(RUTA_ARCHIVO_POKEMONES) as f:
        csv_read = csv.DictReader(f, delimiter= ";")
        for dic in csv_read:
            pokedic[dic["nombre"]] = dic["numero"]
    return pokedic
    