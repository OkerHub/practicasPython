import os
import request
import json


    #Esta función obtiene datos de la PokeAPI para un Pokémon dado.

def obtener_datos_pokemon(nombre_pokemon):
    url_base = "https://pokeapi.co/api/v2/pokemon/{}".format(nombre_pokemon.lower())
    respuesta = request.get(url_base)


#validacion de status

    if respuesta.status_code == 404:
        print("¡Error! Pokémon no encontrado.")
        return None
    else:
        datos_pokemon = respuesta.json()
        return datos_pokemon



    

 #esta funcion muestra en pantalla la informacion del pokemon
   
def mostrar_info_pokemon(datos_pokemon):
    imagen_url = datos_pokemon['sprites']['front_default']
    peso = datos_pokemon['weight'] / 10.0 #Correccion de decimales
    altura = datos_pokemon['height'] / 10.0 # correccion de decimales
    movimientos = [movimiento['move']['name'] for movimiento in datos_pokemon['moves']]
    habilidades = [habilidad['ability']['name'] for habilidad in datos_pokemon['abilities']]
    tipos = [tipo['type']['name'] for tipo in datos_pokemon['types']]

    print("Imagen: {}".format(imagen_url))
    print("Peso: {} kg".format(peso))
    print("Altura: {} m".format(altura))
    print("Movimientos: {}".format(", ".join(movimientos)))
    print("Habilidades: {}".format(", ".join(habilidades)))
    print("Tipos: {}".format(", ".join(tipos)))

    return imagen_url, peso, altura, movimientos, habilidades, tipos

    #Esta funcion guarda la información del Pokémon en un archivo .json y la envia a una carpeta que se crea en el escritorio

def guardar_en_json(nombre_pokemon, info_pokemon):
    carpeta_pokedex = os.path.join(os.path.expanduser('~'), 'Desktop', 'Python')
    if not os.path.exists(carpeta_pokedex):
        os.makedirs(carpeta_pokedex)

    ruta_archivo = os.path.join(carpeta_pokedex, "{}.json".format(nombre_pokemon))

    with open(ruta_archivo, 'w') as archivo:
        json.dump(info_pokemon, archivo, indent=4)

  

# Este es el comienzo de ejecucion del programa
if __name__ == "__main__":
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")
    datos_pokemon = obtener_datos_pokemon(nombre_pokemon)

    if datos_pokemon:
        info_pokemon = mostrar_info_pokemon(datos_pokemon)
        guardar_en_json(nombre_pokemon, {
            "imagen": info_pokemon[0],
            "peso": info_pokemon[1],
            "altura": info_pokemon[2],
            "movimientos": info_pokemon[3],
            "habilidades": info_pokemon[4],
            "tipos": info_pokemon[5]
        })
