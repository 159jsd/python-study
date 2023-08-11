### 웹 크롤링 ###

#! 1. 웹크롤링(web crawling)
# : 웹 페이지를 체계적으로 탐색하여 원하는 데이터를 추출하는 행위 

# 4-4. HTTP 상태 코드 (크롤링 중 발생할 수 있는 상태)
# 200 OK: 성공적으로 응답 받았음 (클롤링 대상 데이터를 가져오기 가능)
# 403 Forbidden: 접근 권한이 없음 (로봇 차단 정책 등으로 크롤링 제한)
# 404 Not Found
# : 요청한 URL에 해당하는 페이지가 없음.(링크가 끊긴 페이지 참조 시 발생)

#! User-Agent
# : 웹 브라우저나 기타 클라이언트가 서버에게 자신의 신분을 알리기 위해
# : HTTP 요청 헤더에 포함시키는 문자열

#! robots.txt
# : 웹 사이트의 어느 부분을 수집하거나 수집하지 않아야 하는지에 대한 지침을 제공

# User-agent: [user-agent name]
# Disallow: [URL string not to be fetched]
# Allow: [URL string to be fetched]

# [예시]
# User-agent *
# Disallow: /private/
# Disallow: /temp/

