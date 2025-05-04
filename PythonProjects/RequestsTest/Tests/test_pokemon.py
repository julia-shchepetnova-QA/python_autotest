import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7766eb4ad109efa535ba5005581b9a0e'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN}
trainer_id = '30667'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', headers=HEADER)
    assert response.status_code == 200
    print(response.json())