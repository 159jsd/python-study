import requests
from bs4 import BeautifulSoup

url = 'https://www.cgv.co.kr/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#CGV 영화 예매 사이트 - 메인 페이지의 무비 차트의 영화 제목을 가져오기
# class: movieName

class_elements = soup.find_all(class_ = 'movieName')
for element in class_elements:
    print(element)