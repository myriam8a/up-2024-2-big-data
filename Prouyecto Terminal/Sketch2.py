import requests

def buscar_libros(query):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": query}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f"Error al buscar libros: {response.status_code}")
        return None
def buscar_peliculas(query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": "a4412dbf9bc0eb4ac74d7c950b4e5cb1",
        "query": query
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error al buscar películas: {response.status_code}")
        return None
def buscar_musica(query):
    # Para utilizar la API de Spotify, necesitarás manejar la autenticación OAuth.
    # Este es un ejemplo simplificado.
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": "7ad31e1d10704a7483c8e8ca183b6144"
    }
    params = {
        "q": query,
        "type": "track"
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()['tracks']['items']
    else:
        print(f"Error al buscar música: {response.status_code}")
        return None
def main():
    libros = buscar_libros("Harry Potter")
    if libros:
        print(libros)

    peliculas = buscar_peliculas("Inception")
    if peliculas:
        print(peliculas)

    musica = buscar_musica("Beatles")
    if musica:
        print(musica)

if __name__ == "__main__":
    main()
