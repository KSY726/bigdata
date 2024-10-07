import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr.lst50')

    results = []

    for song in songs:
        title = song.select_one('div.ellipsis.rank01 > span > a').text
        artist = song.select_one('div.ellipsis.rank02 > span > a').text
        results.append((title, artist))

    for idx, (title, artist) in enumerate(results, start=1):
        print(f"{idx}. {title} - {artist}")