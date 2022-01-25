import clases

def crear_objetos_pokemones_equipo(dic_equipos, nombre_equipo, info_de_pokemones_csv):
    """Crea una lista compuesta por objetos de la clase Pokemon"""
    pokemones_equipo = []
    if nombre_equipo in dic_equipos:
        for pokemon in dic_equipos[nombre_equipo]:
            pokemon = pokemon[0].upper() + pokemon[1:].lower()
            poke_info = info_de_pokemones_csv[pokemon]
            pokemones_equipo.append(clases.Pokemon(poke_info["numero"], poke_info["imagen"],\
                    pokemon, poke_info["tipos"], poke_info["hp"], poke_info["atk"],\
                    poke_info["def"], poke_info["spa"], poke_info["spd"], poke_info["spe"]))
    return pokemones_equipo
