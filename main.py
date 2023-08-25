import requests
from bs4 import BeautifulSoup

song_list_url = "https://j-lyric.net/artist/a001fed"
response = requests.get(url=song_list_url)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")
title_list = soup.select("p.ttl > a")

url_header = "https://j-lyric.net/"
for title in title_list:
    href = title.get("href")
    song_title = title.text
    song_url = url_header + href
    song_response = requests.get(url=song_url)
    song_response.raise_for_status()
    song_soup = BeautifulSoup(song_response.content, "html.parser")
    lyric = song_soup.select_one("#Lyric")
    lyric_text_list = []
    lyric_text_list.append(song_title + "\n\n\n")
    for l in lyric.contents:
        lyric_text_list.append(str(l))

    lyric_text = "".join(lyric_text_list).replace("<br/>", "\n")
    with open(f"results/{song_title}.txt", mode="w", encoding="utf-8") as f:
        f.write(lyric_text)

    print(song_title, "processed!")
