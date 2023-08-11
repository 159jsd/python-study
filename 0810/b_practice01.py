import requests

### 검색 결과 웹 페이지 정보 가져오기 실습 예제 ###
# 파이썬 웹 크롤링 코드 작성

# 롯데 자이언츠 기본 URL: base_url
base_url = 'https://www.giantsclub.com/html/'

# URL 파라미터 설정: params
params = {
    "pcode" : "257"
}
# User-Agent 설정: headers
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200"}

response = requests.get(base_url, params=params, headers=header)

# 웹 페이지가 정상적으로 응답을 반환했는지 확인
if response.status_code == 200:
    # 웹페이지 내용 출력
    response.text[:300]
else:
    print(f'Error {response.status_code}')