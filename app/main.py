import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

# Constantes de autenticación de la API de Spotify
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


def get_token() -> str:
    """
    Obtiene el token de acceso a la API de Spotify usando el flujo 'Client Credentials'.

    Realiza una solicitud POST al endpoint de autenticación de Spotify,
    codificando en base64 el CLIENT_ID y CLIENT_SECRET para obtener el token de acceso.

    Returns:
        str: El token de acceso obtenido.

    Raises:
        Exception: Si la solicitud a la API de Spotify falla.
    """
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo el token de Spotify: {response.json()}."
        )

    return response.json()["access_token"]


def search_artist(token: str, name: str) -> str:
    """
    Busca un artista en Spotify por su nombre y devuelve su ID.

    Realiza una búsqueda de artista en Spotify utilizando el token de acceso
    y devuelve el ID del primer artista encontrado.

    Args:
        token (str): El token de acceso de la API de Spotify.
        name (str): El nombre del artista a buscar.

    Returns:
        str: El ID del artista encontrado.

    Raises:
        Exception: Si el artista no se encuentra o la solicitud falla.
    """
    url = f"https://api.spotify.com/v1/search?q={name}&type=artist&limit=1"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo el artista: {response.json()}."
        )

    results = response.json()
    if results["artists"]["items"]:
        return results["artists"]["items"][0]["id"]
    else:
        raise Exception(
            f"El artista {name} no se ha encontrado."
        )


def get_artist_data(token: str, id: str) -> dict:
    """
    Obtiene datos de un artista de Spotify como el nombre, número de seguidores y popularidad.

    Args:
        token (str): El token de acceso de la API de Spotify.
        id (str): El ID del artista.

    Returns:
        dict: Un diccionario con los datos del artista: nombre, seguidores y popularidad.

    Raises:
        Exception: Si la solicitud a la API falla.
    """
    url = f"https://api.spotify.com/v1/artists/{id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo los datos del artista: {response.json()}."
        )

    results = response.json()
    return {
        "name": results["name"],
        "followers": results["followers"]["total"],
        "popularity": results["popularity"]
    }


def get_artist_top_track(token: str, id: str) -> dict:
    """
    Obtiene la canción más popular de un artista.

    Realiza una solicitud a Spotify para obtener la lista de canciones más populares de un artista,
    y devuelve la canción con mayor popularidad.

    Args:
        token (str): El token de acceso de la API de Spotify.
        id (str): El ID del artista.

    Returns:
        dict: Un diccionario con el nombre y la popularidad de la canción más popular.

    Raises:
        Exception: Si la solicitud a la API falla.
    """
    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Error obteniendo las canciones del artista: {response.json()}."
        )

    results = response.json()
    top_track = max(results["tracks"], key=lambda track: track["popularity"])

    return {
        "name": top_track["name"],
        "popularity": top_track["popularity"]
    }


# 1. Obtención del token de acceso
token = get_token()

# 2. Búsqueda de los IDs de los artistas
artist_1_name = input("Introduce el nombre del primer artista: ")
artist_2_name = input("Introduce el nombre del segundo artista: ")

artist_1_id = search_artist(token, artist_1_name)
artist_2_id = search_artist(token, artist_2_name)

print(artist_1_id)
print(artist_2_id)

# 3. Obtención de datos de los artistas

# 3.1. Seguidores y popularidad
artist_1 = get_artist_data(token, artist_1_id)
artist_2 = get_artist_data(token, artist_2_id)

# 3.2. Canción más popular
top_track_artist_1 = get_artist_top_track(token, artist_1_id)
top_track_artist_2 = get_artist_top_track(token, artist_2_id)

# 4. Comparativa entre ambos artistas
artist_1_counter = 0
artist_2_counter = 0

print(f"\nComparación de artistas:\n")
print(f"{artist_1['name']}")
print(f"{artist_2['name']}")

# 4.1. Comparación de seguidores
print(f"\nComparación de seguidores:\n")
print(f"Seguidores {artist_1['name']}: {artist_1['followers']}")
print(f"Seguidores {artist_2['name']}: {artist_2['followers']}")

if artist_1["followers"] > artist_2["followers"]:
    print(f"{artist_1['name']} es más popular en número de seguidores.")
    artist_1_counter += 1
else:
    print(f"{artist_2['name']} es más popular en número de seguidores.")
    artist_2_counter += 1

# 4.2. Comparación de popularidad general
print(f"\nComparación de popularidad general:\n")
print(f"Popularidad {artist_1['name']}: {artist_1['popularity']}")
print(f"Popularidad {artist_2['name']}: {artist_2['popularity']}")

if artist_1["popularity"] > artist_2["popularity"]:
    print(f"{artist_1['name']} es más popular a nivel general.")
    artist_1_counter += 1
else:
    print(f"{artist_2['name']} es más popular a nivel general.")
    artist_2_counter += 1

# 4.3. Comparación de canciones más populares
print(f"\nComparación de canciones más populares:\n")
print(f"Canción {top_track_artist_1['name']} ({artist_1['name']}): {top_track_artist_1['popularity']} de popularidad.")
print(f"Canción {top_track_artist_2['name']} ({artist_2['name']}): {top_track_artist_2['popularity']} de popularidad.")

if top_track_artist_1["popularity"] > top_track_artist_2["popularity"]:
    print(f"La canción {top_track_artist_1['name']} de {artist_1['name']} es más popular.")
    artist_1_counter += 1
else:
    print(f"La canción {top_track_artist_2['name']} de {artist_2['name']} es más popular.")
    artist_2_counter += 1

# 5. Resultado final de la comparativa
print(f"\nResultado final:\n")
print(f"{artist_1['name'] if artist_1_counter > artist_2_counter else artist_2['name']} es más popular.")
