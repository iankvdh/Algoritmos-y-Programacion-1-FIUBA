RUTA_ARCHIVO_POKEMONES = 'pokemons.csv'
RUTA_ARCHIVO_MOVIMIENTOS = 'movimientos.csv'
RUTA_ARCHIVO_EQUIPOS = 'equipos.txt'

def movimientos_pokemon(pokemon, todos_los_mov):
    """
    Recibe un pokemon y retorna una lista
    de sus movimientos
    """
    pokemon = pokemon[0].upper() + pokemon[1:].lower()
    for dic_poke_mov in todos_los_mov:
        for clave in dic_poke_mov:
            if clave == pokemon:
                return dic_poke_mov[pokemon]
