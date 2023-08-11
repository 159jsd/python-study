### 인터넷 영화 데이터베이스에서 영화 정보 수집 ###

# IMDb: Internet Movie Database

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.imdb.com/?ref_=nv_home'
HEADERS = {
    'User-Agent': 'User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'
}

def fetch_movie_data(start):
    url = BASE_URL
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html-parser')

    movie = soup.select('.ipc-image')