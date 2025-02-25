#상품 리뷰: 유저 id, 평점, 유저 신체정보, 구매 옵션, 리뷰 텍스트 뽑아오기

#첫번째 방법 - 리뷰 본문 내용만 긁어오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import re
import time

def get_reviews(browser):
    html = browser.page_source
    soup = bs(html, 'html.parser')
    reviews = soup.find_all('li', class_='list_review_inner')
    review_list = []
    for review in reviews:
        review_text = review.find('div', class_='text-14').get_text(strip=True) #아마 아이디랑 별점은 여기 클래스를 바꿔주면 될 듯?
        review_list.append(review_text)
    return review_list

browser = webdriver.Chrome()
browser.get('https://bnostore.co.kr/Speaker/?idx=418')
time.sleep(1)

reviews = []  # 리뷰를 저장할 리스트

# 페이지 번호를 클릭하여 리뷰 가져오기
for page_number in range(1, 3):  # 1페이지부터 3페이지까지
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, str(page_number)))).click()
        time.sleep(2)  # 페이지 로딩을 기다립니다.
        reviews.extend(get_reviews(browser))  # 현재 페이지의 리뷰를 가져와서 리스트에 추가합니다.
    except Exception as e:
        print("페이지 로딩 실패:", e)

print(reviews)  # 모든 리뷰를 출력합니다.

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import re
import time

def get_reviews(browser):
    html = browser.page_source
    soup = bs(html, 'html.parser')
    reviews = soup.find_all('li', class_='list_review_inner')
    review_list = []
    for review in reviews:
        try:
            # 별점
            stars = len(review.select('.bts.bt-star.active'))

            # 아이디
            user_id = review.find(class_='use_summary').find(class_='body_font_color_50').text

            # 리뷰 내용
            review_text = review.find('div', class_='text-14').get_text(strip=True)

            review_data = {
                'Stars': stars,
                'User_ID': user_id,
                'Review_Text': review_text
            }

            review_list.append(review_data)
        except Exception as e:
            print("리뷰 데이터를 가져오는 중 오류 발생:", e)

    return review_list

browser = webdriver.Chrome()
browser.get('https://bnostore.co.kr/Speaker/?idx=418')
time.sleep(3)  # 초기 페이지 로딩을 기다립니다.

reviews = []  # 리뷰를 저장할 리스트

# 페이지 번호를 클릭하여 리뷰 가져오기
for page_number in range(1, 4):  # 1페이지부터 3페이지까지
    try:
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, str(page_number))))
        element.click()
        time.sleep(5)  # 페이지 로딩을 기다립니다.
        reviews.extend(get_reviews(browser))  # 현재 페이지의 리뷰를 가져와서 리스트에 추가합니다.
    except Exception as e:
        print("페이지 로딩 실패:", e)

for review in reviews:
    print("Stars:", review['Stars'])
    print("User ID:", review['User_ID'])
    print("Review Text:", review['Review_Text'])
    print("------------------------")
'''


