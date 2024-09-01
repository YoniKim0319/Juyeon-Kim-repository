#상품 정보: 제목, 썸네일, 브랜드 명, 가격(할인 전, 후), 배송 유형 등등의 상품 상세 정보 전부 크롤링
#예시: 뱅앤올룹슨 스피커로 진행함

import requests
from bs4 import BeautifulSoup
raw = requests.get('https://bnostore.co.kr/Speaker/?idx=418',
                   headers={'User-Agent': 'Mozilla/5.0'})
html = BeautifulSoup(raw.content, "html.parser", from_encoding='utf-8')
# print(html) - 제대로 페이지 f12내용들 긁어와지는 거 확인 됨

# f12로 뜯어보니까, 스포츠 기사 text_area처럼 아예 원하는 정보 다 담긴 변수 못 찾음. 따라서 섹션별로 변수-리스트 만들 것임

#1 제품 이미지 가져오기
product_image = html.select('img.xzoom')
#print(product_image) - 내가 원한 부분이 떼어졌는 지 확인(떼어짐)
for tag in product_image:
    src_url = tag.get('src')
    print(src_url)
#2 제품 이름 가져오기
product_name = html.select('.view_tit.no-margin-top.title_font_style')
# print(header_text) - 내가 원했던 부분이 떼어져 왔는 지 확인함(떼어짐!)
for element in product_name: #for문으로 제목 텍스트 추출
    print(element.text.replace('SALEBESTMD', ''))
''' 두번째 방법, 만약 "salebestmd"가 포함되어 있는 경우에만 지우고 싶다면 아래와 같이 조건문을 사용할 수 있습니다
    if 'salebestmd' in element.text:
        print(element.text.replace('salebestmd', ''))
    else:
        print(element.text)'''

#2 가격 정보 텍스트 리스트화
price_info = html.select('.holder.table-row .sale_percentage, .holder.table-row .real_price')
result_text = ""

for i in price_info:
    result_text += i.text + " "

print(result_text)

#3 배송 정보 및 제품 상세 정보 텍스트 리스트화

#div item_detail에 내가 긁어오고자 하는 내용들이 전부 들어가 있었어서 해당 html문서 부분만 따로 변수에 넣음
delivery_content = '''<div class="item_detail">
							<div class="_item_detail_wrap">
	<div class="margin-bottom-xxl">
					<div class="option_wrap" style="display: none; font-size:14px; ">
				<div class="inline-blocked vertical-middle">
					<span class="option_title text-bold">원산지</span>
				</div>
				<div class="inline-blocked vertical-middle">
					<span class="option_data">중국</span>
				</div>
			</div>
							<div class="option_wrap" style="display: none; font-size:14px; ">
				<div class="inline-blocked vertical-middle">
					<span class="option_title text-bold">제조사</span>
				</div>
				<div class="inline-blocked vertical-middle">
					<span class="option_data">뱅앤올룹슨</span>
				</div>
			</div>
							<div class="option_wrap" style="display: none; font-size:14px; ">
				<div class="inline-blocked vertical-middle">
					<span class="option_title text-bold">브랜드</span>
				</div>
				<div class="inline-blocked vertical-middle">
					<span class="option_data">뱅앤올룹슨</span>
				</div>
			</div>
				<div class="option_wrap" style="display: none; font-size:14px;">
			<div class="inline-blocked vertical-middle">
				<span class="option_title text-bold">구매혜택</span>
			</div>
			<div class="inline-blocked vertical-middle">
		<span class="option_data">
							0 적립금 적립예정				<a href="javascript:;" class="btn-popover" role="button" tabindex="0" data-trigger="focus" data-toggle="popover" title="" data-content="적립금액은 할인 쿠폰 적용 및 옵션 가격, 수량을 기준으로 적립되므로 최종 적립금액은 쿠폰 사용 여부 및 옵션 가격, 수량에 따라 달라질 수 있습니다." data-original-title="" data-placement="auto"><i aria-hidden="true" class="btm bt-question-circle"></i><span class="sr-only">적립예정</span></a>
					</span>
			</div>
		</div>

		<div class="option_wrap" style="display: none; font-size:14px;">
			<div class="inline-blocked vertical-middle">
				<span class="option_title text-bold">주문안내</span>
			</div>
			<div class="inline-blocked vertical-middle">
				<span class="option_data">최소 주문금액 0원</span>
			</div>
		</div>

		<div class="option_wrap" style="display: none; font-size: 14px;">
			<div class="inline-blocked vertical-middle">
				<span class="option_title text-bold">무게</span>
			</div>
			<div class="inline-blocked vertical-middle">
				<span class="option_data">0kg</span>
			</div>
		</div>
							<div class="option_wrap" style="display: block; font-size:14px;">
				<div class="inline-blocked vertical-middle">
					<span class="option_title text-bold">배송 방법</span>
				</div>
				<div class="inline-blocked vertical-middle">
					<span class="option_data">
						택배											</span>
				</div>
			</div>
							<div class="option_wrap" style="display: block; font-size:14px;">
					<div class="inline-blocked vertical-middle">
						<span class="option_title text-bold">배송비</span>
					</div>
					<div class="inline-blocked vertical-middle">
						<span class="option_data">무료 <span class="text-gray holder divider-wrap"><em class="divider">|</em>도서산간 배송비 추가 <a href="javascript:;" class="html-popover text-gray" role="button" tabindex="0" data-trigger="focus" data-toggle="popover" title="" data-content="제주 및 도서지역 추가 5,000원" data-original-title="" data-placement="auto"><i class="btm bt-question-circle" aria-hidden="true"></i><span class="sr-only">popover</span></a></span></span>					</div>
				</div>
							<div class="option_wrap" style="display:none; font-size:14px;">
					<div class="inline-blocked vertical-middle">
						<span class="option_title text-bold">배송 안내</span>
					</div>
					<div class="inline-blocked vertical-middle">
						<span class="option_data"></span>
					</div>
				</div>

            			</div>


		<div class="margin-bottom-xxl select_wrap  clearfix deliv" style=" display: none; ">			<div class="inline-blocked form-delivery" style="display: inline-block">
									<div class="form-select-wrap " style="display: none;">
						<select class="countryList" title="countryList">
							<option value="KR" selected=""></option>
						</select>
					</div>
							</div>
		</div>
	<div class="delivery_info margin-bottom-xxl disabled"> <!-- 주말 또는 해당 시간이 아닐경우 disabled class 추가 -->
	<div class="tabled full-width">
		<div class="table-cell vertical-top">
			<div class="delivery_ico text-brand"><i class="fas fa-truck"></i></div>
		</div>
		<div class="table-cell vertical-top">
			<div class="text-14 delivery_txt">
				<div class="type01">
					<strong>오늘출발 상품</strong><br>
					<span class="text-bold text-brand">오늘 9:00까지 결제</span>시 오늘 바로 발송됩니다.
				</div>
				<div class="type02">
					<strong>오늘출발 상품</strong><br>
					<span class="text-bold text-brand">오늘출발 마감</span>되었습니다. (평일 9:00까지)
				</div>
			</div>
		</div>
	</div>
</div>	<script>
		$('.btn-popover').popover();
		$('.html-popover').popover({html : true});
		SITE_SHOP_DETAIL.addDelivType('parcel');
		SITE_SHOP_DETAIL.addDelivPayType('price');
	</script>
	</div>
						</div>'''


def extract_product_details(delivery_content):
    soup = BeautifulSoup(delivery_content, 'html.parser')
    all_option_wrap = soup.find_all(class_="option_wrap") #option_wrap클래스의 모든 요소들을 찾아라

    product_details = {}  # 원산지, 제조사 등의 항목과 값을 매칭하기 위해 딕셔너리 사용

    for option_wrap in all_option_wrap:
        option_title = option_wrap.find(class_="option_title") #option_title text bold면 text bold는 클래스명에 넣는거 아님!
        option_data = option_wrap.find(class_="option_data")

        if option_title and option_data:
            key = option_title.get_text(strip=True)
            value = option_data.get_text(strip=True)
            product_details[key] = value

    for key, value in product_details.items():
        print(f"{key}: {value}")


# 원산지, 제조사 등의 텍스트 추출하여 출력
extract_product_details(delivery_content)


#추출한 모든 내용 리스트화 하기
# 1. 제품 이미지 가져오기
product_image = html.select('img.xzoom')
image_urls = []  # 이미지 URL을 저장할 리스트

for tag in product_image:
    src_url = tag.get('src')
    image_urls.append(src_url)

for url in image_urls:
    print('상품 사진:', url)

# 2. 제품 이름 가져오기
product_name = html.select('.view_tit.no-margin-top.title_font_style')
names = []  # 제품 이름을 저장할 리스트

for element in product_name:
    names.append(element.text.replace('SALEBESTMD', ''))

for name in names:
    print('상품 이름:', name)

# 3. 가격 정보 텍스트 리스트화
price_info = html.select('.holder.table-row .sale_percentage, .holder.table-row .real_price')
prices = []  # 가격 정보를 저장할 리스트

for i in price_info:
    prices.append(i.text)

for price in prices:
    print('가격:', price)

# 추출한 모든 내용 리스트화 하기
# 나머지 코드는 동일하게 유지하고, 수정되어야 할 부분만 아래에 기재되어 있습니다.
result_list = []

max_length = max(len(image_urls), len(names), len(prices))  # 최대 길이 계산

for i in range(max_length):
    result = {}
    if i < len(image_urls):
        result['상품 사진'] = image_urls[i]
    if i < len(names):
        result['상품 이름'] = names[i].strip() if names[i] else None
    if i < len(prices):
        result['가격'] = prices[i].strip() if prices[i] else None
    result_list.append(result)

print(result_list)

#추출한 모든 내용 df화 하기
# 1. 이미지 가져오기
'''product_image = html.select('img.xzoom')
image_urls = []  # 이미지 URL을 저장할 리스트

for tag in product_image:
    src_url = tag.get('src')
    image_urls.append(src_url)

# 2. 제품 이름 가져오기
product_name = html.select('.view_tit.no-margin-top.title_font_style')
names = []  # 제품 이름을 저장할 리스트

for element in product_name:
    names.append(element.text.replace('SALEBESTMD', ''))

# 3. 가격 정보 텍스트 리스트화
price_info = html.select('.holder.table-row .sale_percentage, .holder.table-row .real_price')
prices = []  # 가격 정보를 저장할 리스트

for i in price_info:
    prices.append(i.text)

# 데이터 프레임화
import pandas as pd

# 데이터 리스트들의 길이가 모두 동일한지 확인
data_length = [len(image_urls), len(names), len(prices)]
if len(set(data_length)) == 1:  # 모든 리스트의 길이가 같다면
    data = {
        'image': image_urls,
        'name': names,
        'price': prices
    }

    df = pd.DataFrame(data)
    print(df)
else:
    print("각 항목의 개수가 일치하지 않아 DataFrame으로 변환할 수 없습니다.")'''


