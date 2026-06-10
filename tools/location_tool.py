import requests


def search_location(place):

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place,
        "format": "json",
        "limit": 5
    }

    response = requests.get(
        url,
        params=params,
        headers={
            "User-Agent": "travel-advisor"
        }
    )

    return response.json()