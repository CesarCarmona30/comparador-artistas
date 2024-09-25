# Comparador de popularidad de artistas de Spotify

## Descripción

Este pequeño proyecto permite comparar la popularidad de dos artistas en Spotify utilizando la API de Spotify.
La comparación se basa en los siguientes aspectos:

- Número de seguidores
- Popularidad general del artista
- Canción más popular del artista

## Requisitos

Para ejecutar este proyecto, necesitas:

- Python 3.8 o superior
- Cuenta de desarrollador en Spotify para obtener un `CLIENT_ID` y `CLIENT_SECRET`
- Instalar las bibliotecas específicadas en el archivo `requirements.txt`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/CesarCarmona30/SpotifyAPI.git
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
   ```env
   CLIENT_ID=tu_spotify_client_id
   CLIENT_SECRET=tu_spotify_client_secret
   ```

## Uso

1. Ejecuta el script principal:
   ```bash
   python main.py
   ```
2. Ingresa el nombre de los dos artistas que deseas comparar cuando te lo solicite el programa.
3. El resultado mostrará la comparación de seguidores, popularidad general y la canción más popular de cada artista.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
Es libre de utilizar, modificar y distribuir este software siempre que incluya el aviso de licencia original en cualquier parte sustancial del software.

---

Licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software as long as you include the original license notice in any substantial portions of the software.
