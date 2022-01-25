import gamelib
import clases
import manejador_de_archivos
import manejador_de_objetos

RUTA_ARCHIVO_EQUIPOS = "equipos.txt"
RUTA_ARCHIVO_DETALLE_MOVIMIENTOS = "detalle_movimientos.csv"
RUTA_ARCHIVO_TABLA_TIPOS = "tabla_tipos.csv"
RUTA_ARCHIVO_POKEMONS = "pokemons.csv"
RUTA_ARCHIVO_MUSICA = "musica.wav"

ANCHO_VENTANA = 1000
ALTO_VENTANA = 700
POKE_WIDTH = 200

# PANTALLA
def mostrar_campo_batalla(equipo1, equipo2):
    gamelib.draw_image("imgs/campo_de_batalla.gif", 0, 0)
    gamelib.draw_text(equipo1.jugador, 120, 480, size=18, bold=True, fill='gray')
    gamelib.draw_image("imgs/trainer1.gif", 70, 530)
    gamelib.draw_text(equipo2.jugador, 820, 110, size=18, bold=True, fill='gray')
    gamelib.draw_image("imgs/trainer2.gif", 770, 160)

    mostrar_pokeballs(equipo1, 90, 505)
    mostrar_pokeballs(equipo2, 790, 135)

    mostrar_hp(equipo1.poke_activo, 250, 460, POKE_WIDTH) 
    gamelib.draw_image(equipo1.poke_activo.imagen, 250, 480)
    mostrar_hp(equipo2.poke_activo, 550, 120, POKE_WIDTH) 
    gamelib.draw_image(equipo2.poke_activo.imagen, 550, 140)

    mostrar_stats(equipo1,530 ,550)
    mostrar_stats(equipo2, 50, 100)
    #BOTON PARA SALIR:
    gamelib.draw_oval(ANCHO_VENTANA-210, ALTO_VENTANA-50, ANCHO_VENTANA,ALTO_VENTANA, fill="#CF0000", outline="#CF0000")
    gamelib.draw_oval(ANCHO_VENTANA-210, ALTO_VENTANA-50, ANCHO_VENTANA,ALTO_VENTANA, fill="#CF0000", outline="#CF0000")
    gamelib.draw_text("Presione ESC para salir", ANCHO_VENTANA-105, ALTO_VENTANA-25, size=13, bold=True, fill='white')
     #TEXTO CAMBIAR POKE:
    gamelib.draw_oval(ANCHO_VENTANA-580, ALTO_VENTANA-50, ANCHO_VENTANA-300,ALTO_VENTANA, fill="#CF0000", outline="#CF0000")
    gamelib.draw_text("Ingrese 'Poke' para cambiar de Pokemon", ANCHO_VENTANA-440, ALTO_VENTANA-25, size=10, bold=True, fill='white')

    
def mostrar_hp(poke, x, y, width):
    porcentaje_restante = poke.hp / poke.hp_max
    if porcentaje_restante > 0.7:
        color = "green"
    elif 0.2 < porcentaje_restante <= 0.7:
        color = "yellow"
    else:
        color = "red"
    gamelib.draw_text(f"Hp: {poke.hp}", x, y-15, size=15, bold=True, fill='black')
    gamelib.draw_rectangle(x, y, x + width, y + 10, fill='gray')
    gamelib.draw_rectangle(x, y, x + (width * porcentaje_restante), y + 10, fill=color)

def mostrar_pokeballs(equipo, x_inicial, y):
    for i, poke in enumerate(equipo.pokemones_equipo):
        if int(poke.hp) > 0:
            gamelib.draw_image("imgs/pokeball.gif", x_inicial + i * 20, y)
        if int(poke.hp) > 0:
            gamelib.draw_image("imgs/pokeball_gray.gif", x_inicial + i * 20, y)


# MOSTRAR INFO EN PANTALLA
def mostrar_stats(equipo, x, y):
    gamelib.draw_rectangle(x-30, y-15, x+450, y+50, fill="#CF0000")
    gamelib.draw_text('Stats:',x, y, fill="white", bold=True)
    stats_actuales = equipo.poke_activo.lista_stats()
    for i in range(len(stats_actuales)//10+2):
        for j, elemento in enumerate(equipo.poke_activo.lista_stats()[(i-1)*10:i*10]):
            gamelib.draw_text(elemento,x+(j*100), y+(i*30), fill="white")

def imprimir_equipos(dic_equipos):
    gamelib.draw_image("imgs/campo_de_batalla.gif", 0, 0)
    gamelib.draw_image("imgs/trainer1.gif", 70, 530)
    gamelib.draw_image("imgs/trainer2.gif", 770, 160)
    
    # Rectangulo rojo
    gamelib.draw_rectangle(ANCHO_VENTANA//2 - 350, ALTO_VENTANA//2-15, ANCHO_VENTANA//2 + 350,ALTO_VENTANA//2+50, fill="#CF0000", outline="#CF0000")
    gamelib.draw_oval(ANCHO_VENTANA//2 - 375, ALTO_VENTANA//2-15, ANCHO_VENTANA//2 - 325, ALTO_VENTANA//2+50, fill="#CF0000", outline="#CF0000")
    gamelib.draw_oval(ANCHO_VENTANA//2 + 325, ALTO_VENTANA//2-15, ANCHO_VENTANA//2 + 375, ALTO_VENTANA//2+50, fill="#CF0000", outline="#CF0000")

    # Texto
    gamelib.draw_text('Equipos:',ANCHO_VENTANA//2, ALTO_VENTANA//2, fill="white", bold=True)
    for i, elemento in enumerate(dic_equipos):
        gamelib.draw_text(elemento,ANCHO_VENTANA//2-250+(i*150), ALTO_VENTANA//2+(30), fill="white")
    
    #TEXTO PARA SALIR:
    gamelib.draw_oval(ANCHO_VENTANA-280, ALTO_VENTANA-50, ANCHO_VENTANA,ALTO_VENTANA, fill="#CF0000", outline="#CF0000")
    gamelib.draw_text("Presione ESC o Cancel para salir", ANCHO_VENTANA-140, ALTO_VENTANA-25, size=10, bold=True, fill='white')

    #TEXTO CAMBIAR POKE:
    gamelib.draw_oval(ANCHO_VENTANA-580, ALTO_VENTANA-50, ANCHO_VENTANA-300,ALTO_VENTANA, fill="#CF0000", outline="#CF0000")
    gamelib.draw_text("Ingrese 'Poke' para cambiar de Pokemon", ANCHO_VENTANA-440, ALTO_VENTANA-25, size=10, bold=True, fill='white')


def imprimir_pokemones_vivos(equipo):
    """Al cambiar de pokemon activo"""
    gamelib.draw_oval(ANCHO_VENTANA//2 - 450, -100, ANCHO_VENTANA//2 + 450, 80, fill="#CF0000")
    gamelib.draw_text('Pokemones:',ANCHO_VENTANA//2, 15, fill="white", bold=True)
    for i, pokemon in enumerate(equipo.pokemones_equipo):
        if pokemon.hp > 0:
            gamelib.draw_text(pokemon.nombre,ANCHO_VENTANA//2-250+(i*100), 45, fill="white")

def imprimir_movimientos_pokemon(lista_movimientos_poke_actual):
    # Rectangulo rojo    
    gamelib.draw_rectangle(ANCHO_VENTANA//2 - 250, ALTO_VENTANA//2-15, ANCHO_VENTANA//2 + 250,ALTO_VENTANA//2+50, fill="#CF0000", outline="#CF0000")
    gamelib.draw_oval(ANCHO_VENTANA//2 - 275, ALTO_VENTANA//2-15, ANCHO_VENTANA//2 - 225, ALTO_VENTANA//2+50, fill="#CF0000", outline="#CF0000")
    gamelib.draw_oval(ANCHO_VENTANA//2 + 225, ALTO_VENTANA//2-15, ANCHO_VENTANA//2 + 275, ALTO_VENTANA//2+50, fill="#CF0000", outline="#CF0000")
    # Texto
    gamelib.draw_text('Movimientos:',ANCHO_VENTANA//2, ALTO_VENTANA//2, fill="white", bold=True)
    for i, elemento in enumerate(lista_movimientos_poke_actual):
        gamelib.draw_text(elemento,ANCHO_VENTANA//2-150+(i*100), ALTO_VENTANA//2+(30), fill="white")

def imprimir_turno(equipo, movimiento, mensaje):
    gamelib.say(f'{equipo.poke_activo.nombre} {mensaje} {movimiento}')

# JUGABILIDAD
def elegir_equipos(jugador, dic_equipos, info_de_pokemones_csv):

    imprimir_equipos(dic_equipos)

    # Pido nombre
    nombre_jugador = gamelib.input(f"{jugador} ingresa tu nombre: ")
    if not nombre_jugador:
        nombre_jugador = jugador

    # Pido que elija un equipo
    equipo_jugador = gamelib.input(f"{nombre_jugador} elegi un equipo: ") 
    if equipo_jugador == None:
        return None
    while not equipo_jugador in dic_equipos: # Si ingreso algo invalido, se lo pido hasta que sea correcto
        equipo_jugador = gamelib.input(f"{nombre_jugador} elegi un equipo valido perejil: ") 
        if equipo_jugador == None:
            return None
        
    # Creo el objeto equipo con los objetos pokemones
    pokemones_equipo = manejador_de_objetos.crear_objetos_pokemones_equipo(dic_equipos, equipo_jugador, info_de_pokemones_csv)
    equipo = clases.Equipo(nombre_jugador, pokemones_equipo, equipo_jugador)

    #El usuario cerró el juego
    if not elegir_poke_activo(equipo, True):
        return None
    
    return equipo

def elegir_poke_activo(equipo, primera_vez = False): ##########################
    
    imprimir_pokemones_vivos(equipo)

    # Pido input por primera vez y chequeo
    poke_activo = gamelib.input(f"{equipo.jugador} elegí un pokemon: ")
    if primera_vez and poke_activo == None:
        return None   
    if poke_activo: 
        poke_activo = poke_activo[0].upper() + poke_activo[1:].lower()

    lista_de_nombres = []
    for nombre in equipo.pokemones_equipo:
        lista_de_nombres.append(nombre.nombre)
   
    # Si el input es invalido vuelvo a pedir y chequear
    while not poke_activo in lista_de_nombres: # Si ingreso algo invalido, se lo pido hasta que sea correcto
        poke_activo = gamelib.input(f"{equipo.jugador} elegí un pokemon: ")
        if primera_vez and poke_activo == None:
            return None
        if poke_activo: 
            poke_activo = poke_activo[0].upper() + poke_activo[1:].lower()

    for poke in equipo.pokemones_equipo:
        if poke.nombre == poke_activo:
            equipo.poke_activo = poke
    return True

def pedir_movimiento(dic_equipos, equipo):
    lista_movimientos_poke_actual = dic_equipos[equipo.nombre][equipo.poke_activo.nombre.lower()]
    imprimir_movimientos_pokemon(lista_movimientos_poke_actual)
    movimiento = gamelib.input(f"{equipo.jugador} selecciona un movimiento:")
    if movimiento and movimiento.isalpha():
        movimiento = movimiento.lower()
    if movimiento == None or movimiento == "poke":
        return movimiento
    while movimiento == "" or not movimiento in lista_movimientos_poke_actual: # Si ingreso algo invalido, se lo pido hasta que sea correcto
        movimiento = gamelib.input(f"{equipo.jugador} selecciona un movimiento:") 
        if movimiento and movimiento.isalpha():
            movimiento = movimiento.lower()
        if movimiento == None or movimiento == "poke":
            return movimiento
    return movimiento


# LOGICA
def hacer_movimiento(equipo_actual, equipo_en_espera, detalle_movimientos, dic_tipos, movimiento):
    if detalle_movimientos[movimiento]["stats"]:
        imprimir_turno(equipo_actual, movimiento, "utiliza")
        statbooster(equipo_actual, equipo_en_espera, detalle_movimientos, movimiento)

    elif detalle_movimientos[movimiento]["objetivo"] == "self": 
        imprimir_turno(equipo_actual, movimiento, "se cura con")
        curacion(equipo_actual)
    else:
        imprimir_turno(equipo_actual, movimiento, "ataca con")
        ataque(equipo_actual, equipo_en_espera, detalle_movimientos, movimiento, dic_tipos)
        
def ataque(equipo_actual, equipo_en_espera, detalle_movimientos, movimiento, dic_tipos):
    equipo_actual.poke_activo.ataque(equipo_en_espera.poke_activo, detalle_movimientos, movimiento, dic_tipos)

def curacion(equipo_actual):
    equipo_actual.poke_activo.curacion()

def statbooster(equipo_actual, equipo_en_espera, detalle_movimientos, movimiento):
    equipo_actual.poke_activo.stat_booster(movimiento, equipo_en_espera.poke_activo, detalle_movimientos)

def estado_pokemon(equipo):
    if not quedan_vivos(equipo):
        #Ganó el jugador actual
        return "Terminó el juego"
    elif equipo.poke_activo.hp <= 0:
        imprimir_turno(equipo, "", "murió")
        elegir_poke_activo(equipo)
        return "Cambio el pokemon"

def quedan_vivos(equipo):
    for pokemon in equipo.pokemones_equipo:
        if pokemon.hp > 0:
            return True
    return False

def jugar(dic_equipos, equipo_actual, equipo_en_espera, detalle_movimientos, dic_tipos):
    """Pide movimiento a ambos jugadores. Si el movimiento ingresado por el equipo actual es 'poke',
    cambia el pokemon activo de ese equipo. Si el movimiento ingresado es valido llama a hacer_movimiento para ejecutarlo. 
    En caso de que uno de los movimientos sea None cierra el juego"""

    #Pide movimientos a ambos equipos
    movimiento_equipo_actual = pedir_movimiento(dic_equipos, equipo_actual)
    if movimiento_equipo_actual == None:
        return "Terminó el juego"
    if movimiento_equipo_actual == "poke":
        elegir_poke_activo(equipo_actual)
        return

    movimiento_equipo_en_espera = pedir_movimiento(dic_equipos, equipo_en_espera)
    if movimiento_equipo_en_espera == None:
        return "Terminó el juego"
    while movimiento_equipo_en_espera == "poke":
        gamelib.say("Solo podes cambiar de Pokemon en tu turno")
        movimiento_equipo_en_espera = pedir_movimiento(dic_equipos, equipo_en_espera)
        
    #Comienza ejecutando el movimiento del pokemon más rápido, y luego el del más lento
    if equipo_actual.poke_activo.spe > equipo_en_espera.poke_activo.spe:
        hacer_movimiento(equipo_actual, equipo_en_espera, detalle_movimientos, dic_tipos, movimiento_equipo_actual)
        estado = estado_pokemon(equipo_en_espera)
        if estado == "Terminó el juego":
            gamelib.say(f'Ganó {equipo_actual.jugador}')
            return "Terminó el juego"
        if estado != "Cambio el pokemon":
            hacer_movimiento(equipo_en_espera, equipo_actual, detalle_movimientos, dic_tipos, movimiento_equipo_en_espera)
    else:
        estado = estado_pokemon(equipo_actual)
        hacer_movimiento(equipo_en_espera, equipo_actual, detalle_movimientos, dic_tipos, movimiento_equipo_en_espera)
        estado = estado_pokemon(equipo_actual)
        if estado == "Terminó el juego":
            gamelib.say(f'Ganó {equipo_en_espera.jugador}')
            return "Terminó el juego"
        if estado != "Cambio el pokemon":
            hacer_movimiento(equipo_actual, equipo_en_espera, detalle_movimientos, dic_tipos, movimiento_equipo_actual)

    #Si algun equipo se querda sin pokemones vivos, Termina el juego
    estado = estado_pokemon(equipo_actual)
    if estado == "Terminó el juego":
        gamelib.say(f'Ganó {equipo_en_espera.jugador}')
        return "Terminó el juego"

def chequear_todos_los_archivos():
    """
    Abre los archivos pokemons.csv y movimientos.csv y muestra 
    un mensaje en caso de error
    """
    try:
        with open(RUTA_ARCHIVO_EQUIPOS, "r") as equipos:
            pass
        with open(RUTA_ARCHIVO_DETALLE_MOVIMIENTOS, "r") as movs:
            pass
        with open(RUTA_ARCHIVO_TABLA_TIPOS, "r") as tipos:
            pass
        with open(RUTA_ARCHIVO_POKEMONS, "r") as pokes:
            pass
        with open(RUTA_ARCHIVO_MUSICA, "r") as musica:
            pass
        return True
    except FileNotFoundError as err:
        print(err)
        return False
    except IOError as err:
        print(err)
        return False

def main():
    if not chequear_todos_los_archivos():
        return
    
    info_de_pokemones_csv = manejador_de_archivos.cargar_pokemones(RUTA_ARCHIVO_POKEMONS)
    dic_equipos = manejador_de_archivos.cargar_equipos(RUTA_ARCHIVO_EQUIPOS)
    detalle_movimientos = manejador_de_archivos.cargar_detalle_movimientos(RUTA_ARCHIVO_DETALLE_MOVIMIENTOS)
    dic_tipos = manejador_de_archivos.cargar_tipos(RUTA_ARCHIVO_TABLA_TIPOS)

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    
    # Cargamos equipos
    equipo1 = elegir_equipos("Jugador 1", dic_equipos, info_de_pokemones_csv)
    if not equipo1:
        return
    equipo2 = elegir_equipos("Jugador 2", dic_equipos, info_de_pokemones_csv)
    if not equipo2:
        return

    gamelib.play_sound(RUTA_ARCHIVO_MUSICA)

    # TURNO ACTUAL
    equipo_actual = equipo1
    equipo_en_espera = equipo2

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        
        gamelib.draw_begin()

        mostrar_campo_batalla(equipo1, equipo2)

        estado = jugar(dic_equipos, equipo_actual, equipo_en_espera, detalle_movimientos, dic_tipos)
        
        # Cambio de turno
        equipo_actual = equipo2 if equipo_actual == equipo1 else equipo1
        equipo_en_espera = equipo1 if equipo_en_espera == equipo2 else equipo2
        
        gamelib.draw_end()

        # Cerrar Ventana
        ev = gamelib.wait()
        if estado == "Terminó el juego":
            break
        if not ev:
            # El usuario cerró la ventana.
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

gamelib.init(main)
