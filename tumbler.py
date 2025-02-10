import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def draw_rectangle_with_text(image, text, rect_start, rect_end, text_position):
    # 이미지에 사각형과 텍스트 추가
    draw = ImageDraw.Draw(image)
    # 사각형 그리기
    draw.rectangle([rect_start, rect_end], outline="red", width=10)
    # 텍스트 위치 및 폰트 설정
    font = ImageFont.load_default()
    draw.text(text_position, text, font=font, fill="red")
    return image

st.title('다회용기 미션 프로토타입')
uploaded_file = st.file_uploader("이미지를 업로드하세요.", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # 사각형 시작과 끝 좌표 설정
    rect_start = (50, 50)  # 예시 좌표, 실제 사용시 조정 필요
    rect_end = (250, 250)  # 예시 좌표, 실제 사용시 조정 필요
    # 텍스트 위치 설정
    text_position = (150, 150)  # 예시 좌표, 실제 사용시 조정 필요
    # 이미지 처리
    processed_image = draw_rectangle_with_text(image, "tumbler", rect_start, rect_end, text_position)
    # 이미지 보여주기
    st.image(processed_image, caption='Processed Image')
    # 확인 버튼
    if st.button('Verify'):
        st.write("이미지가 확인되었습니다. 물 지급 완료")


