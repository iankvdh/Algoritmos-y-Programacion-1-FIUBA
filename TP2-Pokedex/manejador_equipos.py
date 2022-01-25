import gamelib
import constantes

def equipo_crear(equipos, lista_todos_pokemones, todos_los_mov):
    """
    Recibe los equipos y un nombre.
    Crea un nuevo equipo con ese nombre.
    """
    nombre_equipo = gamelib.input("Nombre del equipo")
    if not nombre_equipo:
        return equipos
    if not nombre_equipo in equipos:
        equipos[nombre_equipo] = {}
        agregar_pokemon(equipos, nombre_equipo, lista_todos_pokemones, todos_los_mov)
    else: 
        gamelib.say("Ese equipo ya existe")
    return equipos


def cancelar_agregar_pokemon(equipos, nombre_equipo):
    if not equipos[nombre_equipo]:
        equipos.pop(nombre_equipo)
    return equipos

def agregar_pokemon(equipos, nombre_equipo, lista_todos_pokemones, todos_los_mov):
    """
    Recibe equipos, nombre_equipo, lista_todos_pokemones y todos_los_mov.
    Pide un pokemon y lo agrega a el equipo cuando sea valido.
    """

    # Chequear limite maximo
    if len(equipos[nombre_equipo]) > 6:
        gamelib.say("Basta capo (max 6 pokemones)")
        return equipos
    
    pokemon_a_agregar = gamelib.input("Ingrese pokemon")

    # Chequeo input
    if pokemon_a_agregar: # Si se recibe input 
        pokemon_a_agregar = pokemon_a_agregar.lower()
    else: # Si se toca cancelar, devuelvo equipos como corresponda
        return cancelar_agregar_pokemon(equipos, nombre_equipo)
    
    
    while pokemon_a_agregar not in lista_todos_pokemones: # Si se recibio input invalido
        
        gamelib.say("Ese pokemon no existe")
        pokemon_a_agregar = gamelib.input("Ingrese pokemon")

        # Chequeo input (igual que antes)
        if pokemon_a_agregar: 
            pokemon_a_agregar = pokemon_a_agregar.lower()
        else:
            return cancelar_agregar_pokemon(equipos, nombre_equipo)
    
    equipos[nombre_equipo][pokemon_a_agregar] = [] # Si consigo input valido, lo agrego

    agregar_movimiento(equipos, nombre_equipo, pokemon_a_agregar, todos_los_mov)

    return equipos
    


def cancelar_agregar_movimiento(equipos, nombre_equipo, pokemon_a_agregar):
    print(equipos)
    print(equipos[nombre_equipo])
    print(equipos[nombre_equipo][pokemon_a_agregar])

    if len(equipos[nombre_equipo]) == 1 and not equipos[nombre_equipo][pokemon_a_agregar]: # Si estaba creando el equipo, borro todo
        equipos.pop(nombre_equipo)

    elif not equipos[nombre_equipo][pokemon_a_agregar] and equipos[nombre_equipo]: # Si ya existia el equipo, borro el pokemon
        equipos[nombre_equipo].pop(pokemon_a_agregar)

    return equipos
    
def agregar_movimiento(equipos, nombre_equipo, pokemon_a_agregar, todos_los_mov):
    """
    Hace muchas cosas magicas y no estamos seguros cuales, entre ellas
    recibir los equipos, el nombre de un equipo, y el nombre de un pokemon.
    Agrega un movimiento a el pokemon de ese equipo si el movimiento
    existe y no hay mas de 4 movimientos.
    """
    # Me aseguro que haya pokemon y este en el equipo
    if not pokemon_a_agregar:
        return equipos

    if not pokemon_a_agregar in equipos[nombre_equipo]:
        gamelib.say("Ese pokemon no está en el equipo")
        return equipos

    # Chequear limite maximo
    if len(equipos[nombre_equipo][pokemon_a_agregar]) >= 4:
        gamelib.say("Basta capo (max 4 movimientos)")
        return equipos

    # Mostrar lista de movimientos
    gamelib.draw_text('Movimientos:',120, 470, fill="black")
    for i in range(len(constantes.movimientos_pokemon(pokemon_a_agregar, todos_los_mov))//10+2):
        for j, elemento in enumerate(constantes.movimientos_pokemon(pokemon_a_agregar, todos_los_mov)[(i-1)*10:i*10]):
            gamelib.draw_text(elemento,140+(j*100), 485+(i*30), fill="black")
    
    movimiento_a_agregar = gamelib.input("Ingrese movimiento") 


    if movimiento_a_agregar: # Si se recibe input 
        movimiento_a_agregar = movimiento_a_agregar.lower()
    else: # Si se toca cancelar, devuelvo equipos como corresponda
        return cancelar_agregar_movimiento(equipos, nombre_equipo, pokemon_a_agregar)
    
    
    while not movimiento_a_agregar in constantes.movimientos_pokemon(pokemon_a_agregar, todos_los_mov):

        gamelib.say("Ese pokemon no tiene ese movimiento")
        movimiento_a_agregar = gamelib.input("Ingrese movimiento")

        if movimiento_a_agregar: # Si se recibe input 
            movimiento_a_agregar = movimiento_a_agregar.lower()
        else: # Si se toca cancelar, devuelvo equipos como corresponda
            return cancelar_agregar_movimiento(equipos, nombre_equipo, pokemon_a_agregar)

    equipos[nombre_equipo][pokemon_a_agregar].append(movimiento_a_agregar)

    return equipos
    
def borrar_pokemon(equipos, nombre_equipo, pokemon_a_sacar):
    """
    Recibe los equipos y el nombre de un equipo y de un pokemon
    Elimina el pokemon del equipo si pertenece a el mismo.
    """
    if not nombre_equipo in equipos: 
        gamelib.say("ese equipo aún no existe")
    else:
        if not pokemon_a_sacar in equipos[nombre_equipo]: 
            gamelib.say("ese pokemon no está en el equipo")
        else: equipos[nombre_equipo].pop(pokemon_a_sacar) 
    return equipos

def equipo_borrar(equipos, nombre_equipo):
    """
    Recibe los equipos y el nombre de un equipo.
    Elimina el equipo si existe
    """
    if not nombre_equipo in equipos:
        gamelib.say("ese equipo aún no existe")
    else:
        equipos.pop(nombre_equipo)
    return equipos

def guardar(info_nueva):
    """
    Recibe el diccionario equipos y lo carga a el
    archivo "equipos.txt"
    """
    with open("equipos.txt", "w") as f:
        for equipo in info_nueva:
            f.write(f"{equipo};")
            for pokemon in info_nueva[equipo]:
                f.write(f"{pokemon}:")
                for i, movimiento in enumerate(info_nueva[equipo][pokemon]):
                    if i < 3 and movimiento != "": 
                        f.write(f"{movimiento},") 
                    elif i == 3 and movimiento != "": 
                         f.write(f"{movimiento}")
                f.write("*")
            f.write("\n")
