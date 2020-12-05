# Fuente : https://www.ps84.es/tipos-fortalezas-y-debilidades-en-pokemon-espada-y-escudo/

def switch_fortaleza(tipo):
    switcher = {
        "bicho" : "psíquico, planta y siniestro",
        "eléctrico" : "volador y agua. No hace daño a tierra",
        "fuego" : "bicho, planta, hielo y acero",
        "planta" : "tierra, agua y roca",
        "normal" : "un poquito a roca y acero",
        "roca" : "bicho, fugo, volador y hielo",
        "siniestro" : "psíquico y fantasma",
        "hada" : "lucha, siniestro, dragón",
        "volador" : "bicho, planta y lucha",
        "tierra" : "veneno, fuego, acero, roca y eléctrico. No hace daño a volador",
        "veneno" : "planta y hada. No hace daño a acero.",
        "acero" : "roca, hielo y hada",
        "dragón" : "dragón. No hace daño a hada",
        "lucha" : "siniestro, hielo, normal, acero y roca. No hace daño a fantasma",
        "fantasma" : "fantasma y psíquico. No hace daño a normal",
        "hielo" : "tierra, volador, planta y dragón",
        "psíquico" : "lucha y veneno. No hace daño a siniestro",
        "agua" : "roca, tierra y fuego"
    }
    print (switcher.get(tipo, "no conozco ese tipo de Pokémon"))


def switch_debilidad(tipo):
    switcher = {
        "bicho" : "fuego, volador y roca",
        "eléctrico" : "tierra",
        "fuego" : "tierra, agua y roca",
        "planta" : "bicho, fuego, volador, hielo, veneno",
        "normal" : "lucha. Inmune a fantasma",
        "roca" : "lucha, planta, tierra, acero y agua",
        "siniestro" : "bicho, lucha y hada. Inmune a psíquico",
        "hada" : "veneno y acero. Inmune a dragón",
        "volador" : "eléctrico, hielo y roca. Inmune a tierra",
        "tierra" : "hielo, planta y agua. Inmune a eléctrico",
        "veneno" : "psíquico y tierra",
        "acero" : "lucha, fuego y tierra. Inmune a veneno",
        "dragón" : "hielo, dragón y hada",
        "lucha" : "hada, pśiquico y volador",
        "fantasma" : "siniestro y fantasma. Inmune a normal y lucha",
        "hielo" : "lucha, acero, fuego y roca",
        "psíquico" : "siniestro, fantasma y bicho",
        "agua" : "eléctrico y planta"
    }
    print (switcher.get(tipo, "no conozco ese tipo de Pokémon"))

switch_debilidad("lucha");
switch_fortaleza("lucha");
switch_fortaleza("cyborg");