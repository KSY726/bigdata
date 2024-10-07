import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr.lst100')

    results = []


rank = []   # 리스트 변수
for i in range(1, 101):
    rank.append(i)
print(rank)


for song in songs:
        title = song.select_one('div.ellipsis.rank01 > span > a').text
        artist = song.select_one('div.ellipsis.rank02 > span > a').text
        results.append((title, artist))

for idx, (title, artist) in enumerate(results, start=1):
        print(f"{idx}. {title} - {artist}")

        import pandas as pd

f_name = "melon50.csv"

df3 = pd.DataFrame({'순위': rank,
                    '제목': tlist,
                    '가수': alist})

df3.to_csv('melon50.csv', index=False)