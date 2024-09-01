from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome("")

browser.get("https://zigzag.kr/catalog/products/100558905?tab=review")
time.sleep(1)

html = browser.page_source
soup = BeautifulSoup(html, "html.parser")

# 상위 5개의 리뷰어와 날짜를 담을 리스트
top_5_reviews = []

# 리뷰어 이름 (class) = css-19a0tmz e1okf4zi1
reviewer_names = soup.find_all('div', class_='css-19a0tmz e1okf4zi1')
for reviewer_name in reviewer_names:
    top_5_reviews.append(reviewer_name.text.strip())
print(top_5_reviews)

#리뷰 내용 담을 리스트
top_5_reviews_contents = []

# 리뷰 내용 가져오기
review_contents = soup.select('.BODY_14.REGULAR.css-1huf8iy.eox2jl02')
for review_content in review_contents:
    top_5_reviews_contents.append(review_content.text.strip())

print(top_5_reviews_contents)