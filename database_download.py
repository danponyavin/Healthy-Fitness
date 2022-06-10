import requests
from urllib.parse import urlencode
import os

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = os.environ['DB_URL']

print("Yandex link to database:", public_key)

final_url = base_url + urlencode(dict(public_key=public_key))
response = requests.get(final_url)
download_url = response.json()['href']

download_response = requests.get(download_url)
with open('./healthyfitness/db.sqlite3', 'wb') as f:
    f.write(download_response.content)
