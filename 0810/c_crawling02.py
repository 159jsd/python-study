### 웹 페이지 분석 및 추출하기 ###

# cmd (명령 프롬프트) & vsc (터미널 창)에서 bs4 라이브러리 설치
# pip install BeautifulSoup4

#! 1. BeautifulSoup4 객체 생성 기본 방법

import requests
from bs4 import BeautifulSoup

url = '검색 대상 URL'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#! 2. BeautifulSoup4 메소드 사용

#? 2-1. find()메소드
# : 지정된 태그들 중에서 가장 첫 번째 태그만 가져오는 메소드
# : 일반적으로 하나의 태그만 존재하는 경우에 사용
