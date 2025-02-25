# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
#
# browser = webdriver.Chrome("chromedriver.exe")
# browser.get("https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201")
# time.sleep(1)
#
# html = browser.page_source
# soup = BeautifulSoup(html, "html.parser")
# product_detail_area = soup.find_all('div', class_='css-34da54 e91dh069')
#
# result = []
# for index, product_detail in enumerate(product_detail_area):
#     if index == 30:
#         break
#
#     title = product_detail.find('div', class_='css-34da54 e91dh069')
#     title_text = title.text if title else "N/A"
#
#     price = product_detail.find('div', class_='css-vrtxib e91dh063')
#     price_text = price.text if price else "N/A"
#
#     review = product_detail.find('div', class_='css-1t95g2m e13zfay42')
#     review_text = review.text if review else "N/A"
#
#     thumbnail = product_detail.find('img', class_='css-178chr5 e1qdearl0')
#     thumbnail_src = thumbnail['src'] if thumbnail else "N/A"
#
#     result.append([title_text, thumbnail_src, price_text, review_text])
#
# df = pd.DataFrame(result, columns=['title', 'thumbnail', 'price', 'review'])
# print(df)

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
#
# browser = webdriver.Chrome("chromedriver.exe")
# browser.get("https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201")
# time.sleep(1)
#
# html = browser.page_source
# soup = BeautifulSoup(html, "html.parser")
# product_detail_area = soup.select('div.css-34da54.e91dh069')
#
# result = []
# for index, product_detail in enumerate(product_detail_area):
#     if index == 30:
#         break
#
#     title = product_detail.select_one('div.CAPTION_12.REGULAR.css-4me7r9.e91dh064')
#     title_text = title.text if title else "N/A"
#
#     price = product_detail.select_one('div.css-vrtxib.e91dh063')
#     price_text = price.text if price else "N/A"
#
#     review = product_detail.select_one('div.css-1t95g2m.e13zfay42')
#     review_text = review.text if review else "N/A"
#
#     thumbnail = product_detail.select_one('div.css-1hlt7si.e81k49g0')
#     thumbnail_src = thumbnail['src'] if thumbnail else "N/A"
#
#     result.append([title_text, thumbnail_src, price_text, review_text])
#
# df = pd.DataFrame(result, columns=['title', 'thumbnail', 'price', 'review'])
# print(df)

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

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
#
# # Chrome WebDriver 초기화
# browser = webdriver.Chrome("chromedriver.exe")
#
# # 크롤링할 대상 페이지의 URL
# url = 'https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201'
#
# # 해당 페이지 열기
# browser.get(url)
#
# # 현재 페이지의 HTML 가져오기
# html = browser.page_source
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # 상위 30개의 <a> 태그 찾기
# for index, link in enumerate(soup.select('a')[:30], start=1):
#     # <a> 태그 안의 href 속성 확인
#     href = link.get('href')
#
#     # href 속성이 존재하는 경우에만 처리
#     if href:
#         if href.startswith('/catalog/products/'):
#             # href 속성을 이용하여 실제 상세 페이지의 URL 생성
#             detail_page_url = 'https://zigzag.kr/' + href
#
#             # 상세 페이지의 HTML 가져오기
#             browser.get(detail_page_url)
#
#             # 스크롤 다운하여 리뷰 영역 로딩
#             for _ in range(3):  # 예시로 3번 스크롤 다운
#                 browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#                 time.sleep(1)
#
#             # 리뷰 페이지의 HTML 가져오기
#             review_html = browser.page_source
#             soup_review = BeautifulSoup(review_html, "html.parser")
#
#             # 리뷰 영역 선택
#             review_area = soup_review.select('div.css-70rfrb.e1hi9732') # 수정이 필요한 부분
#
#             result = []
#             for index, review_detail in enumerate(review_area):
#                 if index == 5:
#                     break
#
#                 review_name = review_detail.select_one('div.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0') #고쳐
#                 review_name_text = review_name.text if review_name else "N/A"
#
#                 review_date = review_detail.select_one('span.BODY_13.MEDIUM.css-1he5u5.e1okf4zi0') #고쳐
#                 review_date_text = review_date.text if review_date else "N/A"
#
#                 review_content = review_detail.select_one('div.BODY_14.REGULAR.css-1huf8iy.eox2jl02') #고쳐
#                 review_content_text = review_content.text if review_content else "N/A"
#
#                 result.append([review_name_text, review_date_text, review_content_text])
#
#     # 30개의 링크를 찾았으면 종료
#     if index == 30:
#         break
#
# df = pd.DataFrame(result, columns=['리뷰어', '리뷰날짜', '리뷰텍스트'])
# df.index.name = 'id'
# print(df)
#
# # 브라우저 닫기
# browser.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ...

more_button = browser.find_element(By.XPATH, '더보기 버튼의 XPATH')
more_button.click()

# 대기 시간 설정 (10초로 예시)
wait = WebDriverWait(browser, 10)
# 로드가 완료될 때까지 대기
wait.until(EC.presence_of_element_located((By.XPATH, '로드가 완료된 후의 요소의 XPATH')))
-------------

try:
    more_btn = box.find_element_by_css_selector('').click
    time.sleep(3)
except:
    continue

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
#
# # Chrome WebDriver 초기화 (webdriver_manager를 사용)
# browser = webdriver.Chrome(ChromeDriverManager().install())
#
# # 크롤링할 대상 페이지의 URL
# url = 'https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201'
#
# # 해당 페이지 열기
# browser.get(url)
#
# # 현재 페이지의 HTML 가져오기
# html = browser.page_source
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # 결과를 담을 리스트 초기화
# result = []
#
# # 상위 30개의 <a> 태그 찾기
# for index, link in enumerate(soup.select('a')[:30], start=1):
#     # <a> 태그 안의 href 속성 확인
#     href = link.get('href')
#
#     # href 속성이 존재하는 경우에만 처리
#     if href and href.startswith('/catalog/products/'):
#         # href 속성을 이용하여 실제 상세 페이지의 URL 생성
#         detail_page_url = 'https://zigzag.kr' + href
#
#         # 상세 페이지의 HTML 가져오기
#         browser.get(detail_page_url)
#
#         # 스크롤 다운하여 리뷰 영역 로딩
#         for _ in range(5):  # 5번 스크롤 다운
#             browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(1)
#
#         # 리뷰 페이지의 HTML 가져오기
#         review_html = browser.page_source
#         soup_review = BeautifulSoup(review_html, "html.parser")
#
#         # 리뷰 영역 선택
#         review_area = soup_review.select('div.css-70rfrb.e1hi9732')  # 수정이 필요한 부분
#
#         for review_detail in review_area[:5]:
#             review_name = review_detail.select_one('div.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0')
#             review_name_text = review_name.text if review_name else "N/A"
#
#             review_date = review_detail.select_one('span.BODY_13.MEDIUM.css-1he5u5.e1okf4zi0')
#             review_date_text = review_date.text if review_date else "N/A"
#
#             review_content = review_detail.select_one('div.BODY_14.REGULAR.css-1huf8iy.eox2jl02')
#             review_content_text = review_content.text if review_content else "N/A"
#
#             result.append([review_name_text, review_date_text, review_content_text])
#
# # 결과를 DataFrame으로 변환
# df = pd.DataFrame(result, columns=['리뷰어', '리뷰날짜', '리뷰텍스트'])
# df.index.name = 'id'
# print(df)
# df.to_excel('3조_지그재그_크롤링_리뷰데이터.xlsx', encoding='utf-8-sig', index=True)
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
#
# # Chrome WebDriver 초기화 (webdriver_manager를 사용)
# browser = webdriver.Chrome(ChromeDriverManager().install())
#
# # 크롤링할 대상 페이지의 URL
# url = 'https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201'
#
# # 해당 페이지 열기
# browser.get(url)
#
# # 현재 페이지의 HTML 가져오기
# html = browser.page_source
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # 결과를 담을 리스트 초기화
# result = []
#
# # 상위 30개의 <a> 태그 찾기
# for index, link in enumerate(soup.select('a')[:30], start=1):
#     # <a> 태그 안의 href 속성 확인
#     href = link.get('href')
#
#     # href 속성이 존재하는 경우에만 처리
#     if href and href.startswith('/catalog/products/'):
#         # href 속성을 이용하여 실제 상세 페이지의 URL 생성
#         detail_page_url = 'https://zigzag.kr' + href
#
#         # 상세 페이지의 HTML 가져오기
#         browser.get(detail_page_url)
#
#         # 스크롤 다운하여 리뷰 영역 로딩
#         for _ in range(5):  # 5번 스크롤 다운
#             browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(1)
#
#         # 리뷰 페이지의 HTML 가져오기
#         review_html = browser.page_source
#         soup_review = BeautifulSoup(review_html, "html.parser")
#
#         # 리뷰 영역 선택
#         review_area = soup_review.select('div.css-70rfrb.e1hi9732')  # 수정이 필요한 부분
#
#         for review_detail in review_area[:5]:
#             # 더보기 버튼이 존재하면 클릭하여 모든 리뷰 텍스트 노출
#             more_button = review_detail.select_one('span.BODY_13.BOLD.css-1aa4nqt.eox2jl01')
#             if more_button and callable(getattr(more_button, "click", None)):
#                 more_button.click()
#                 time.sleep(1)
#
#             review_name = review_detail.select_one('div.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0')
#             review_name_text = review_name.text if review_name else "N/A"
#
#             review_date = review_detail.select_one('span.BODY_13.MEDIUM.css-1he5u5.e1okf4zi0')
#             review_date_text = review_date.text if review_date else "N/A"
#
#             review_content = review_detail.select_one('div.BODY_14.REGULAR.css-1huf8iy.eox2jl02')
#             review_content_text = review_content.text if review_content else "N/A"
#
#             result.append([review_name_text, review_date_text, review_content_text])
#
# # 결과를 DataFrame으로 변환
# df = pd.DataFrame(result, columns=['리뷰어', '리뷰날짜', '리뷰텍스트'])
# df.index.name = 'id'
# print(df)
# df.to_excel('3조_지그재그_크롤링_리뷰데이터.xlsx', index=True)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

# Chrome WebDriver 초기화 (webdriver_manager를 사용)
browser = webdriver.Chrome(ChromeDriverManager().install())

# 크롤링할 대상 페이지의 URL
url = 'https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201'

# 해당 페이지 열기
browser.get(url)

# 현재 페이지의 HTML 가져오기
html = browser.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 결과를 담을 리스트 초기화
result = []

# 상위 30개의 <a> 태그 찾기
for index, link in enumerate(soup.select('a')[:30], start=1):
    # <a> 태그 안의 href 속성 확인
    href = link.get('href')

    # href 속성이 존재하는 경우에만 처리
    if href and href.startswith('/catalog/products/'):
        # href 속성을 이용하여 실제 상세 페이지의 URL 생성
        detail_page_url = 'https://zigzag.kr' + href

        # 상세 페이지의 HTML 가져오기
        browser.get(detail_page_url)

        # 스크롤 다운하여 리뷰 영역 로딩
        for _ in range(5):  # 5번 스크롤 다운
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        # 클릭할 더보기 버튼 요소 가져오기
        more_button = browser.find_element_by_css_selector('span.BODY_13.BOLD.css-1aa4nqt.eox2jl01')

        # 더보기 버튼이 존재하면 JavaScript를 사용하여 클릭
        if more_button.is_displayed():
            browser.execute_script("arguments[0].click();", more_button)
            time.sleep(2)

        # 리뷰 페이지의 HTML 가져오기
        review_html = browser.page_source
        soup_review = BeautifulSoup(review_html, "html.parser")

        # 리뷰 영역 선택 (상위 5개 리뷰 영역)
        review_area = soup_review.select('div.css-70rfrb.e1hi9732:nth-child(1), div.css-70rfrb.e1hi9732:nth-child(2), div.css-70rfrb.e1hi9732:nth-child(3), div.css-70rfrb.e1hi9732:nth-child(4), div.css-70rfrb.e1hi9732:nth-child(5)')

        for review_detail in review_area[:5]:
            review_name = review_detail.select_one('div.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0')
            review_name_text = review_name.text if review_name else "N/A"

            review_date = review_detail.select_one('span.BODY_13.MEDIUM.css-1he5u5.e1okf4zi0')
            review_date_text = review_date.text if review_date else "N/A"

            review_content = review_detail.select_one('div.BODY_14.REGULAR.css-1huf8iy.eox2jl02')
            review_content_text = review_content.text if review_content else "N/A"

            result.append([review_name_text, review_date_text, review_content_text])

# 결과를 DataFrame으로 변환
df = pd.DataFrame(result, columns=['리뷰어', '리뷰날짜', '리뷰텍스트'])
df.index.name = 'id'
print(df)
df.to_excel('3조_지그재그_크롤링_리뷰데이터.xlsx', index=True)

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
#
# # 크롤링할 대상 페이지의 URL
# url = 'https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201'
#
# # 해당 페이지 열기
# driver.get(url)
#
# # 현재 페이지의 HTML 가져오기
# html = driver.page_source
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # 결과를 담을 리스트 초기화
# result = []
#
# # 상위 30개의 <a> 태그 찾기
# for index, link in enumerate(soup.select('a')[:30], start=1):
#     # <a> 태그 안의 href 속성 확인
#     href = link.get('href')
#
#     # href 속성이 존재하는 경우에만 처리
#     if href and href.startswith('/catalog/products/'):
#         # href 속성을 이용하여 실제 상세 페이지의 URL 생성
#         detail_page_url = 'https://zigzag.kr' + href
#
#         # 상세 페이지의 HTML 가져오기
#         driver.get(detail_page_url)
#
#         # 스크롤 다운하여 리뷰 영역 로딩
#         for _ in range(5):  # 5번 스크롤 다운
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(1)
#
#         # 기다리기
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#             (By.XPATH, '//div[contains(., "더보기")]/span[@class="BODY_13 BOLD css-1aa4nqt eox2jl01"]')))
#
#         # 클릭할 더보기 버튼 요소 가져오기
#         more_button = driver.find_element(By.XPATH, '//div[contains(., "더보기")]/span[@class="BODY_13 BOLD css-1aa4nqt eox2jl01"]')
#
#         # 클릭
#         driver.execute_script("arguments[0].click();", more_button)
#
#         # 리뷰 페이지의 HTML 가져오기
#         review_html = driver.page_source
#         soup_review = BeautifulSoup(review_html, "html.parser")
#
#         # 리뷰 영역 선택
#         review_area = soup_review.select('div.css-70rfrb.e1hi9732')
#
#         for review_detail in review_area[:5]:
#             review_name = review_detail.select_one('div.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0')
#             review_name_text = review_name.text if review_name else "N/A"
#
#             review_date = review_detail.select_one('span.BODY_13.MEDIUM.css-1he5u5.e1okf4zi0')
#             review_date_text = review_date.text if review_date else "N/A"
#
#             review_content = driver.find_element(By.CSS_SELECTOR, 'div.BODY_14.REGULAR.css-1huf8iy.eox2jl02').text
#             review_content_text = review_content if review_content else "N/A"
#
#             result.append([review_name_text, review_date_text, review_content_text])
#
# # 결과를 DataFrame으로 변환
# df = pd.DataFrame(result, columns=['리뷰어', '리뷰날짜', '리뷰텍스트'])
# df.index.name = 'id'
# print(df)
# df.to_excel('3조_지그재그_크롤링_리뷰데이터.xlsx', index=True)

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
#
# # Chrome WebDriver 초기화
# browser = webdriver.Chrome("chromedriver.exe")
#
# # 크롤링할 대상 페이지의 URL
# url = 'https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201'
#
# # 해당 페이지 열기
# browser.get(url)
#
# # 현재 페이지의 HTML 가져오기
# html = browser.page_source
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # 결과를 담을 리스트 초기화
# result = []
#
# # 상위 30개의 <a> 태그 찾기
# for index, link in enumerate(soup.select('a')[:30], start=1):
#     # <a> 태그 안의 href 속성 확인
#     href = link.get('href')
#
#     # href 속성이 존재하는 경우에만 처리
#     if href and href.startswith('/catalog/products/'):
#         # href 속성을 이용하여 실제 상세 페이지의 URL 생성
#         detail_page_url = 'https://zigzag.kr' + href
#
#         # 상세 페이지의 HTML 가져오기
#         browser.get(detail_page_url)
#
#         # 리뷰 페이지의 HTML 가져오기
#         review_html = browser.page_source
#         soup_review = BeautifulSoup(review_html, "html.parser")
#
#         # 리뷰 영역 선택
#         review_area = soup_review.select('div.css-1uql0ux.e1pdzmd01')  # 수정이 필요한 부분
#
#         for review_detail in review_area[:5]:
#             review_name = review_detail.select_one('div.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0')
#             review_name_text = review_name.text if review_name else "N/A"
#
#             review_date = review_detail.select_one('span.BODY_17.REGULAR.BODY_13.MEDIUM.css-1w6topb.e1cn5bmz0')
#             review_date_text = review_date.text if review_date else "N/A"
#
#             review_content = review_detail.select_one('div.BODY_14.REGULAR.css-epr5m6.e1j2jqj72')
#             review_content_text = review_content.text if review_content else "N/A"
#
#             result.append([review_name_text, review_date_text, review_content_text])
#
# # 결과를 DataFrame으로 변환
# df = pd.DataFrame(result, columns=['리뷰어', '리뷰날짜', '리뷰텍스트'])
# df.index.name = 'id'
# print(df)
# df.to_excel('3조_지그재그_크롤링_리뷰데이터.xlsx', index=True)

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
#
# # Chrome WebDriver 초기화
# browser = webdriver.Chrome("chromedriver.exe")
#
# # 크롤링할 대상 페이지의 URL
# url = 'https://zigzag.kr/categories/-1?title=%EC%95%84%EC%9A%B0%ED%84%B0&category_id=-1&middle_category_id=436&sub_category_id=438&sort=201'
#
# # 해당 페이지 열기
# browser.get(url)
# soup = BeautifulSoup(url, 'html.parser')
#
# # 결과를 담을 리스트 초기화
# result = []
#
# # 상위 30개의 <a> 태그 찾기
# for index, link in enumerate(soup.select('a')[:30], start=1):
#     # <a> 태그 안의 href 속성 확인
#     href = link.get('href')
#
#     # href 속성이 존재하는 경우에만 처리
#     if href and href.startswith('/catalog/products/'):
#         # href 속성을 이용하여 실제 상세 페이지의 URL 생성
#         detail_page_url = 'https://zigzag.kr' + href
#
#         # 상세 페이지의 HTML 가져오기
#         browser.get(detail_page_url)
#
#         # 리뷰 페이지의 HTML 가져오기
#         review_html = browser.page_source
#         soup_review = BeautifulSoup(review_html, "html.parser")
#
#         # 리뷰 영역 선택
#         review_area = soup_review.select('div.css-1uql0ux.e1pdzmd01')  # 수정이 필요한 부분
#
#         for review_detail in review_area[:5]:
#             # Create a new soup object for each review page
#             review_soup = BeautifulSoup(str(review_detail), 'html.parser')
#
#             review_name = review_soup.select_one('div.BODY_16.SEMIBOLD.css-1k3hx0v.e1fnwskn0')
#             review_name_text = review_name.text if review_name else "N/A"
#
#             review_date = review_soup.select_one('span.BODY_17.REGULAR.BODY_13.MEDIUM.css-1w6topb.e1cn5bmz0')
#             review_date_text = review_date.text if review_date else "N/A"
#
#             review_content = review_soup.select_one('div.BODY_14.REGULAR.css-epr5m6.e1j2jqj72')
#             review_content_text = review_content.text if review_content else "N/A"
#
#             result.append([review_name_text, review_date_text, review_content_text])
#
# # 결과를 DataFrame으로 변환
# df = pd.DataFrame(result, columns=['리뷰어', '리뷰날짜', '리뷰텍스트'])
# df.index.name = 'id'
# print(df)
# df.to_excel('3조_지그재그_크롤링_리뷰데이터.xlsx', index=True)
