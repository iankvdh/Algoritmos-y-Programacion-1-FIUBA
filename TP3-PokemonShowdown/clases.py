import random

class Equipo:
    def __init__(self, jugador, pokemones_equipo, nombre):
        self.jugador = jugador
        self.poke_activo = None
        self.pokemones_equipo = pokemones_equipo
        self.nombre = nombre

    def __str__(self):
        return f"***Equipo de {self.jugador}***\nPokemones: {self.pokemones_equipo}\n"

    def elegir_pokemon(self, poke_elegido):
        self.poke_activo = poke_elegido
 

class Pokemon:
    def __init__(self, numero, imagen, nombre, tipos, hp, atk, defe, spa, spd, spe):
        self.numero = numero
        self.imagen = imagen
        self.nombre = nombre
        self.tipos = tipos
        self.hp = int(hp)
        self.atk = int(atk)
        self.defe =  int(defe)
        self.spa =  int(spa)
        self.spd =  int(spd)
        self.spe =  int(spe)
        self.hp_max = int(hp) + 110
        
    def __str__(self):
        return f"{self.nombre}"


    def ataque(self, otro, detalle_movimientos, ataque, dic_tipos):

        info_movimiento = detalle_movimientos[ataque]

        if info_movimiento["categoria"] == "Special":
            ataque = self.spa
            defensa = otro.spd
        else:
            ataque = self.atk
            defensa = otro.defe

        daño_base = 15 * float(info_movimiento["poder"]) * (ataque / defensa) // 50 + 1
        
        # STAB 
        if info_movimiento["tipo"] in self.tipos:
            daño_base *= 1.5
        
        # BOOST TIPOS POKEMONES
        self_tipos = self.tipos.split(",")
        otro_tipos = otro.tipos.split(",")

        multiplicador = 1
        for tipo_s in self_tipos:
            for tipo_o in otro_tipos:
                    multiplicador *= float(dic_tipos[tipo_o][tipo_s])

        daño_base *= multiplicador

        # ALEATORIEDAD
        rand = random.uniform(0.8, 1.0)
        daño_base *= rand
        daño_base //= 1
        
        #Baja vida adversario
        otro.hp -= int(daño_base)

    def stat_booster(self, movimiento, otro, detalle_movimientos): #aca entra si tiene stats
        stat = detalle_movimientos[movimiento]["stats"].split(",")
        if detalle_movimientos[movimiento]["objetivo"] == "self":
            if "atk" in stat:
                self.atk *= 2
            if "def" in stat:
                self.defe *= 2
            if "spe" in stat:
                self.spe *= 2
        else:
            if "atk" in stat:
                otro.atk //= 2
            if "def" in stat:
                otro.defe //= 2
            if "spe" in stat:
                otro.spe //= 2

    def curacion(self): #aca entra si no tiene statrs y el objetivo es self
        self.hp += self.hp_max//2
        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def lista_stats(self):
        return ["atk " + str(self.atk), "def " + str(self.defe), "spa " + str(self.spa), "spd " + str(self.spd), "spe " + str(self.spe)]
