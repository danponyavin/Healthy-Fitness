"""Download db.sqlite3 from yandex disk"""

from urllib.parse import urlencode
import os
import requests


BASE_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = os.environ['DB_URL']

print("Yandex link to database:", public_key)

FINAL_URL = BASE_URL + urlencode(dict(public_key=public_key))
response = requests.get(FINAL_URL)
download_url = response.json()['href']

download_response = requests.get(download_url)
with open('./healthyfitness/db.sqlite3', 'wb') as f:
    f.write(download_response.content)
