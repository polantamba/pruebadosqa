import requests

def obtener_cartas_blue_eyes():
    response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?archetype=Blue-Eyes")
    if response.status_code == 200:
        return response.json().get('data', [])
    return []

def obtener_carta_por_id(carta_id):
    response = requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?id={carta_id}")
    if response.status_code == 200:
        data = response.json().get('data', [])
        if data:
            return data[0]
    return None