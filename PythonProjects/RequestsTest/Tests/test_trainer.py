import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7766eb4ad109efa535ba5005581b9a0e'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN}
TRAINER_ID = '30667'

def test_status_code_and_trainer_id():
    response = requests.get(url = f'{URL}/trainers', params={'id': TRAINER_ID})
    assert response.status_code == 200
    data = response.json()