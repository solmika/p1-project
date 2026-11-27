import requests
import json

def if_null(results_list):
    """If a search result field is null, this function will display a message instead"""
    for r in results_list:
        r.get("title") or "Title unknown"
        r.get("artist_title") or "Artist unknown"
        r.get("thumbnail") or "Thumbnail unavailable"
    return results_list

def search_art(term):
    try:
        FIELDS = "title,artist_title,thumbnail"
        headers = {"AIC-User-Agent": "HCDE310 student project"}
        url = "https://api.artic.edu/api/v1/artworks/search"
        params ={"q": term, "fields": FIELDS}
        r = requests.get(url,params=params,headers=headers,timeout=10)

    except requests.RequestException:
        return None

    if r.status_code != 200:
        return None

    data = (r.json())
    
    complete_results = if_null(data["data"])
    return complete_results