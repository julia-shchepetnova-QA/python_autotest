import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7766eb4ad109efa535ba5005581b9a0e'
HEADER = {'Content - Type' : 'application/json',
          'trainer_token': TOKEN}
body_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 38
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon)         
print(response.text)'''

pokemon_id = 308169
body_update = {
    'pokemon_id': '308169',
    'name':'Котик',
   "photo_id": 38
    }

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response.text)'''

data = {
    'pokemon_id': '308169'
    }

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = data)
print(response.text)