def buscar_por_nombre(pokelista, pokemon, poke_indice):
    """
    Recibe la pokelista, poke-indice y el pokemon y devuelve
    el diccionario con la info de ese pokemon (tiempo cte)
    """
    pokemon = pokemon[0].upper() + pokemon[1:].lower()
    indice = poke_indice[pokemon]
    return(pokelista[int(indice)-1])

def buscar_por_indice(pokelista, indice):
    """
    Recibe la pokelista y el indice del pokemon a buscar
    y devuleve el diccionario con la info de ese pokemon (tiempo lineal)
    """
    for dic in pokelista:
        if dic["numero"] == str(indice):
            return dic