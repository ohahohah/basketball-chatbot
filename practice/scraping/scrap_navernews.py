# 웹페이지 요청을 위한 패키지
import requests
# 웹페이지 파싱을 위한 패키지
from bs4 import BeautifulSoup

# 네이버 뉴스 페이지 url
url = 'https://news.naver.com/'
# 네이버 뉴스 페이지 요청, 응답 저장
response = requests.get(url)

print(response) # 응답 형식은 <Response [200]>
print(response.status_code) # 응답 코드는 200 (정상 응답)
#print(response.text)    # 응답 내용 출력 (html, 엄청 긺)

# response로 부터 html 가져오기
html = response.text

# BeautifulSoup 으로 html 파싱
soup = BeautifulSoup(html, 'html.parser')

# CSS Selector 로 헤드라인 뉴스가 있는 항목 선택
hdline_titles = soup.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')

# 헤드라인 뉴스가 있는 a 태그에서 텍스트만 추출
for title in hdline_titles:
    print(title.get_text(strip=True))   # 결과 출력
