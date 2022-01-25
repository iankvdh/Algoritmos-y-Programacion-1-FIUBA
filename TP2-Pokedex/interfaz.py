from tkinter.constants import NW
import gamelib
import manejador_archivos
import busqueda_pokemon
import manejador_equipos
import constantes

# Constantes utiles
RUTA_ARCHIVO_POKEMONES = constantes.RUTA_ARCHIVO_POKEMONES
RUTA_ARCHIVO_MOVIMIENTOS = constantes.RUTA_ARCHIVO_MOVIMIENTOS
RUTA_ARCHIVO_EQUIPOS = constantes.RUTA_ARCHIVO_EQUIPOS
# Tamaño ventana
ANCHO_VENTANA = 1300
ALTO_VENTANA = 800

# Posiciones
POS_X_TEXTO_POKEMONES = 465

# PRINTEAR EN PANTALLA
def printear_info_pokemon(pokemon):
    """Recibe un pokemon como diccionario e imprime su informacion en pantalla"""
    
    gamelib.draw_image(pokemon["imagen"], 60, 170)
    gamelib.draw_text(pokemon["nombre"], 230, 550, "Courier", 25, True, False, fill="black")
    gamelib.draw_text(f"Tipos: {pokemon['tipos']}", POS_X_TEXTO_POKEMONES, 225, "Courier", 20,  fill="black", anchor =NW)
    gamelib.draw_text(f"Hp: {pokemon['hp']}", POS_X_TEXTO_POKEMONES, 265, "Courier", 20, fill="black", anchor=NW)
    gamelib.draw_text(f"Atk: {pokemon['atk']}", POS_X_TEXTO_POKEMONES, 305,  "Courier",20, fill="black", anchor=NW)
    gamelib.draw_text(f"Def: {pokemon['def']}", POS_X_TEXTO_POKEMONES, 345,  "Courier",20, fill="black", anchor=NW)
    gamelib.draw_text(f"Spa: {pokemon['spa']}", POS_X_TEXTO_POKEMONES, 385,  "Courier",20, fill="black", anchor=NW)
    gamelib.draw_text(f"Spd: {pokemon['spd']}", POS_X_TEXTO_POKEMONES, 425, "Courier", 20,fill="black", anchor=NW)
    gamelib.draw_text(f"Spe: {pokemon['spe']}", POS_X_TEXTO_POKEMONES, 465,  "Courier",20, fill="black", anchor=NW)
    gamelib.draw_rectangle(625, 565, 920, 610)
    gamelib.draw_text("Presione 'B' para buscar un pokemon por nombre", 630, 570, None, 10, fill="black", anchor=NW)
    gamelib.draw_text("Presione 'I' para buscar un pokemon por indice", 630, 590, None, 10, fill="black", anchor=NW)

def printear_info_equipos(equipos, nombre):
    """
    Recibe los equipos y un nombre. Muestra la informacion
    de ese equipo en pantalla y los botones para modificarlo.
    """
    if nombre:
        cont = 80
        gamelib.draw_text(f"{nombre}", 80, cont, None, 40, True, fill="black", anchor=NW)
        cont += 80
        for j, pokemones in enumerate(equipos[nombre].keys()):
            gamelib.draw_text(pokemones, 100, cont, None, 20, fill="black", anchor=NW)

            for k, movimientos in enumerate(equipos[nombre][pokemones]):
                gamelib.draw_text(movimientos, 250+k*150, cont, None, 15, fill="black", anchor=NW)
            cont += 50

    # BOTON CREAR EQUIPO
    gamelib.draw_oval(ANCHO_VENTANA-125, ALTO_VENTANA-340, ANCHO_VENTANA-75, ALTO_VENTANA-390, fill="#0DFFE9", outline="#0DFFE9")
    gamelib.draw_oval(ANCHO_VENTANA-75, ALTO_VENTANA-340, ANCHO_VENTANA-25, ALTO_VENTANA-390, fill="#0DFFE9", outline="#0DFFE9")
    gamelib.draw_rectangle(ANCHO_VENTANA-100, ALTO_VENTANA-340, ANCHO_VENTANA-50, ALTO_VENTANA-390, fill="#0DFFE9", outline="#0DFFE9")
    gamelib.draw_text("Crear",ANCHO_VENTANA-75, ALTO_VENTANA-375, fill="black")
    gamelib.draw_text("Equipo",ANCHO_VENTANA-75, ALTO_VENTANA-355, fill="black")

    # BOTON AGREGAR POKEMON
    gamelib.draw_oval(ANCHO_VENTANA-125, ALTO_VENTANA-265, ANCHO_VENTANA-75, ALTO_VENTANA-315, fill="#CFFF0D", outline="#CFFF0D")
    gamelib.draw_oval(ANCHO_VENTANA-75, ALTO_VENTANA-265, ANCHO_VENTANA-25, ALTO_VENTANA-315, fill="#CFFF0D", outline="#CFFF0D")
    gamelib.draw_rectangle(ANCHO_VENTANA-100, ALTO_VENTANA-265, ANCHO_VENTANA-50, ALTO_VENTANA-315, fill="#CFFF0D", outline="#CFFF0D")
    gamelib.draw_text("Agregar",ANCHO_VENTANA-75, ALTO_VENTANA-300, fill="black")
    gamelib.draw_text("Pokemon",ANCHO_VENTANA-75, ALTO_VENTANA-280, fill="black")

    # BOTON AGREGAR MOVIMIENTO
    gamelib.draw_oval(ANCHO_VENTANA-125, ALTO_VENTANA-190, ANCHO_VENTANA-75, ALTO_VENTANA-240, fill="#32FF00", outline="#32FF00")
    gamelib.draw_oval(ANCHO_VENTANA-75, ALTO_VENTANA-190, ANCHO_VENTANA-25, ALTO_VENTANA-240, fill="#32FF00", outline="#32FF00")
    gamelib.draw_rectangle(ANCHO_VENTANA-100, ALTO_VENTANA-190, ANCHO_VENTANA-50, ALTO_VENTANA-240, fill="#32FF00", outline="#32FF00")
    gamelib.draw_text("Agregar",ANCHO_VENTANA-75, ALTO_VENTANA-225, fill="black")
    gamelib.draw_text("Movimiento",ANCHO_VENTANA-75, ALTO_VENTANA-205, fill="black")

    # BOTON BORRAR EQUIPO
    gamelib.draw_oval(ANCHO_VENTANA-125, ALTO_VENTANA-115, ANCHO_VENTANA-75, ALTO_VENTANA-165, fill="#E000FF", outline="#E000FF")
    gamelib.draw_oval(ANCHO_VENTANA-75, ALTO_VENTANA-115, ANCHO_VENTANA-25, ALTO_VENTANA-165, fill="#E000FF", outline="#E000FF")
    gamelib.draw_rectangle(ANCHO_VENTANA-100, ALTO_VENTANA-115, ANCHO_VENTANA-50, ALTO_VENTANA-165, fill="#E000FF", outline="#E000FF")
    gamelib.draw_text("Borrar",ANCHO_VENTANA-75, ALTO_VENTANA-150, fill="black")
    gamelib.draw_text("Equipo",ANCHO_VENTANA-75, ALTO_VENTANA-130, fill="black")

    # BOTON BORRAR POKEMON
    gamelib.draw_oval(ANCHO_VENTANA-125, ALTO_VENTANA-40, ANCHO_VENTANA-75, ALTO_VENTANA-90, fill="#FF9E00", outline="#FF9E00")
    gamelib.draw_oval(ANCHO_VENTANA-75, ALTO_VENTANA-40, ANCHO_VENTANA-25, ALTO_VENTANA-90, fill="#FF9E00", outline="#FF9E00")
    gamelib.draw_rectangle(ANCHO_VENTANA-100, ALTO_VENTANA-40, ANCHO_VENTANA-50, ALTO_VENTANA-90, fill="#FF9E00", outline="#FF9E00")
    gamelib.draw_text("Borrar",ANCHO_VENTANA-75, ALTO_VENTANA-75, fill="black")
    gamelib.draw_text("Pokemon",ANCHO_VENTANA-75, ALTO_VENTANA-55, fill="black")

def mostrar_tablero():
    """Imprime el fondo y los botones de vistas"""

    # FONDO
    gamelib.draw_rectangle(0,0,ANCHO_VENTANA,ALTO_VENTANA, fill='red')
    gamelib.draw_rectangle(50,50,ANCHO_VENTANA-140,ALTO_VENTANA-50, fill='grey')
    gamelib.draw_rectangle(60,60,ANCHO_VENTANA-150,ALTO_VENTANA-60, fill='white')

    # BOTON PANTALLA POKEMONES
    gamelib.draw_oval(ANCHO_VENTANA-125, ALTO_VENTANA-600, ANCHO_VENTANA-75, ALTO_VENTANA-650, fill="green", outline="green")
    gamelib.draw_oval(ANCHO_VENTANA-75, ALTO_VENTANA-600, ANCHO_VENTANA-25, ALTO_VENTANA-650, fill="green", outline="green")
    gamelib.draw_rectangle(ANCHO_VENTANA-100, ALTO_VENTANA-600, ANCHO_VENTANA-50, ALTO_VENTANA-650, fill="green", outline="green")
    gamelib.draw_text("Ver",ANCHO_VENTANA-75, ALTO_VENTANA-635, fill="black")
    gamelib.draw_text("Pokemones",ANCHO_VENTANA-75, ALTO_VENTANA-615, fill="black")

    # BOTON PANTALLA EQUIPOS
    gamelib.draw_oval(ANCHO_VENTANA-125, ALTO_VENTANA-525, ANCHO_VENTANA-75, ALTO_VENTANA-575, fill="#3E00FF", outline="#3E00FF")
    gamelib.draw_oval(ANCHO_VENTANA-75, ALTO_VENTANA-525, ANCHO_VENTANA-25, ALTO_VENTANA-575, fill="#3E00FF", outline="#3E00FF")
    gamelib.draw_rectangle(ANCHO_VENTANA-100, ALTO_VENTANA-525, ANCHO_VENTANA-50, ALTO_VENTANA-575, fill="#3E00FF", outline="#3E00FF")
    gamelib.draw_text("Ver",ANCHO_VENTANA-75, ALTO_VENTANA-560, fill="black")
    gamelib.draw_text("Equipos",ANCHO_VENTANA-75, ALTO_VENTANA-540, fill="black")

    # BOTON GUARDAR
    gamelib.draw_oval(ANCHO_VENTANA-125, ALTO_VENTANA-450, ANCHO_VENTANA-75, ALTO_VENTANA-500, fill="yellow", outline="yellow")
    gamelib.draw_oval(ANCHO_VENTANA-75, ALTO_VENTANA-450, ANCHO_VENTANA-25, ALTO_VENTANA-500, fill="yellow", outline="yellow")
    gamelib.draw_rectangle(ANCHO_VENTANA-100, ALTO_VENTANA-450, ANCHO_VENTANA-50, ALTO_VENTANA-500, fill="yellow", outline="yellow")
    gamelib.draw_text("Guardar",ANCHO_VENTANA-75, ALTO_VENTANA-475, fill="black")


# DATOS
def datos_validos(dato, lista_todos_pokemones):
    """
    Recibe input de pokemon o indice
    y devuelve True si el dato es valido,
    False si no es valido
    """
    if dato.isdigit():
        if 1 <= int(dato) <= len(lista_todos_pokemones):
            return True
    if dato.isalpha():
        if dato.lower() in lista_todos_pokemones:
            return True
    return False

def chequear_todos_los_archivos():
    """
    Abre los archivos pokemons.csv y movimientos.csv y muestra 
    un mensaje en caso de error
    """
    try:
        pokemons = open(RUTA_ARCHIVO_POKEMONES, "r")
        movimientos = open(RUTA_ARCHIVO_MOVIMIENTOS, "r")
        return True
    except FileNotFoundError as err:
        print(err)
        return False
    except IOError as err:
        print(err)
        return False
    
# INTERACCION
def busqueda(tecla, pokemon, indice, Pokelista, lista_todos_pokemones, poke_indice):
    "Busca pokemon por nombre o índice"

    if tecla == 'b' or tecla == 'B':
        dato = gamelib.input("Nombre del pokemon")

        if dato and datos_validos(dato, lista_todos_pokemones) and dato.isalpha():
            return busqueda_pokemon.buscar_por_nombre(Pokelista, dato, poke_indice), int(pokemon["numero"])
        else:
            gamelib.say("Entrada inválida.")

    elif tecla == 'i' or tecla == 'I':
        dato = gamelib.input("Indice del pokemon")
        
        if dato and datos_validos(dato, lista_todos_pokemones) and dato.isnumeric():
            return busqueda_pokemon.buscar_por_indice(Pokelista, int(dato)), int(dato)
        else:
            gamelib.say("Entrada inválida.")

    return pokemon, indice

def mouse(posicion, equipos, nombres_equipos, indice_equipos, pantalla_actual, lista_todos_pokemones, todos_los_mov):
    "Se encarga del manejo de todos los botones"
    # VER POKEMONES
    if  ALTO_VENTANA-650 < posicion < ALTO_VENTANA-600:
        return "pokemones"
    # VER EQUIPOS
    if  ALTO_VENTANA-575 < posicion < ALTO_VENTANA-525:
        return "equipos"
    # GUARDAR
    if  ALTO_VENTANA-500 < posicion < ALTO_VENTANA-450:
        manejador_equipos.guardar(equipos)
    
    if pantalla_actual == "equipos": 
        # CREAR EQUIPO
        if  ALTO_VENTANA-390 < posicion < ALTO_VENTANA-340:
            cant_equipos_vieja = len(equipos)
            equipos = manejador_equipos.equipo_crear(equipos, lista_todos_pokemones, todos_los_mov)

            if cant_equipos_vieja != len(equipos):
                return len(nombres_equipos) 
        if equipos: 
            # AGREGAR POKEMON
            if  ALTO_VENTANA-315 < posicion < ALTO_VENTANA-265:
                equipos = manejador_equipos.agregar_pokemon(equipos, nombres_equipos[indice_equipos], lista_todos_pokemones, todos_los_mov)
            # AGREGAR MOVIMIENTO
            if  ALTO_VENTANA-240 < posicion < ALTO_VENTANA-190:
                pokemon_a_agregar = gamelib.input("Pokemon a agregar un movimiento")
                manejador_equipos.agregar_movimiento(equipos, nombres_equipos[indice_equipos], pokemon_a_agregar, todos_los_mov)
            # BORRAR EQUIPO
            if  ALTO_VENTANA-165 < posicion < ALTO_VENTANA-115:
                if equipos:
                    manejador_equipos.equipo_borrar(equipos, nombres_equipos[indice_equipos])
                    return  -1
            # BORRAR POKEMON
            if  ALTO_VENTANA-90 < posicion < ALTO_VENTANA-40:
                if not equipos[nombres_equipos[indice_equipos]]:
                    gamelib.draw_text("El equipo esta vacio!", 500, 500, fill="black")
                else:
                    poke_a_borrar = gamelib.input("Pokemon a borrar")
                    manejador_equipos.borrar_pokemon(equipos, nombres_equipos[indice_equipos], poke_a_borrar)

def avanzar_y_atrasar_pokemon(tecla, pantalla_actual, Pokelista, indice, pokemon, lista_todos_pokemones):
    """
    permite desplazarse entre los pokemones
    """

    if pantalla_actual != "pokemones":
        return indice, pokemon

    if tecla == 'd' or tecla == 'D':
        # Avanzar pokemon
        indice += 1
        if indice > len(lista_todos_pokemones):
            indice = 1
        pokemon = busqueda_pokemon.buscar_por_indice(Pokelista, indice)
        
    if tecla == 'a' or tecla == 'A':
        # Atrasar pokemon
        indice -= 1
        if indice < 1:
            indice = len(lista_todos_pokemones)
        pokemon = busqueda_pokemon.buscar_por_indice(Pokelista, indice)
    
    return indice, pokemon

def avanzar_y_atrasar_equipo(tecla, equipos, nombres_equipos, indice_equipos, pantalla_actual):
    """
    permite desplazarse entre los equiopos
    """

    if pantalla_actual == "equipos" and len(equipos) > 1:
        if tecla == 'd' or tecla == 'D':
            # Avanzar equipo
            indice_equipos += 1
            if indice_equipos >= len(nombres_equipos):
                indice_equipos = 0
        if tecla == 'a' or tecla == 'A':
            # Atrasar equipo
            indice_equipos -= 1
            if indice_equipos < 0:
                indice_equipos = len(nombres_equipos)-1
    
    return indice_equipos

# MAIN
def main():
    if not chequear_todos_los_archivos():
        return

    # Antes de hacer cualquier cosa vemos que los archivos esten bien
    # 
    lista_todos_pokemones = manejador_archivos.lista_todos_pokemones(RUTA_ARCHIVO_POKEMONES)
    Pokelista = manejador_archivos.cargar_pokemones(RUTA_ARCHIVO_POKEMONES)
    poke_indice = manejador_archivos.cargar_pokemon_indice(RUTA_ARCHIVO_POKEMONES)
    todos_los_mov = manejador_archivos.todos_los_movimientos(RUTA_ARCHIVO_MOVIMIENTOS)
    indice = 1

    if not Pokelista:
        pokemon = None
    pokemon = busqueda_pokemon.buscar_por_indice(Pokelista, indice)
    pantalla_actual = "pokemones"
    equipos = manejador_archivos.cargar(constantes.RUTA_ARCHIVO_EQUIPOS)

    # Esta lista es para iterar por las claves del diccionario equipos
    nombres_equipos = list(equipos.keys()) 
    indice_equipos = 0

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    
    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        gamelib.draw_begin()
        mostrar_tablero() # Imprime la interfaz con la pantalla en blanco
        # Imprime la pantalla pokemones o equipos segun elija el usuario
        # Al iniciar el programa imprime la pantalla pokemones por defecto
        if pantalla_actual == "pokemones":
            printear_info_pokemon(pokemon)
        elif pantalla_actual == "equipos":
            if nombres_equipos:
                printear_info_equipos(equipos, nombres_equipos[indice_equipos])
            else:
                printear_info_equipos(equipos, None) # Si no hay equipos, pasamos None como nombre
        gamelib.draw_end()

        # Cerrar Ventana
        ev = gamelib.wait()
        if not ev:
            # El usuario cerró la ventana.
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        # Ir a pantalla pokemones
        if gamelib.EventType.KeyPress and ev.key == 'p' or ev.key == 'P':
            pantalla_actual = "pokemones"
        # Ir a pantalla equipos
        if gamelib.EventType.KeyPress and ev.key == 'e' or ev.key == 'E':
            pantalla_actual = "equipos"

        #Desplazarse entre equipos y pokemones
        if ev.type == gamelib.EventType.KeyPress:
            indice_equipos = avanzar_y_atrasar_equipo(ev.key, equipos, nombres_equipos, indice_equipos, pantalla_actual)
            indice, pokemon = avanzar_y_atrasar_pokemon(ev.key, pantalla_actual, Pokelista, indice, pokemon, lista_todos_pokemones)

        #Búsqueda de pokemon por nombre o índice
        if pantalla_actual == "pokemones":
            if ev.type == gamelib.EventType.KeyPress:
                pokemon, indice = busqueda(ev.key, pokemon, indice, Pokelista, lista_todos_pokemones, poke_indice)

        #Botonera (mouse)
        if ev.type == gamelib.EventType.ButtonPress:
            if ANCHO_VENTANA-125 < ev.x < ANCHO_VENTANA-25:   
                x = mouse(ev.y, equipos, nombres_equipos, indice_equipos, pantalla_actual, lista_todos_pokemones, todos_los_mov)
                if x != None:
                    if x == "equipos":
                        pantalla_actual = "equipos"
                    elif x == "pokemones":
                        pantalla_actual = "pokemones"
                    elif x == -1:
                        indice_equipos -= 1
                    else: indice_equipos = x

        nombres_equipos = list(equipos.keys())    

gamelib.init(main)