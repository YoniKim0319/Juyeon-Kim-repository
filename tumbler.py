import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def draw_rectangle_with_text(image, text):
    # 이미지에 사각형과 텍스트 추가
    draw = ImageDraw.Draw(image)
    width, height = image.size
    # 사각형 좌표 설정
    rectangle_start = (width // 4, height // 4)
    rectangle_end = (3 * width // 4, 3 * height // 4)
    # 사각형 그리기
    draw.rectangle([rectangle_start, rectangle_end], outline="red", width=10)
    # 텍스트 위치 및 폰트 설정
    font = ImageFont.load_default()
    text_position = (width // 2, height // 2)
    draw.text(text_position, text, font=font, fill="white")
    return image

st.title('이미지 업로드 및 확인')
uploaded_file = st.file_uploader("이미지를 업로드하세요.", type=['png', 'jpg', 'jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # 이미지 처리
    processed_image = draw_rectangle_with_text(image, "tumbler")
    # 이미지 보여주기
    st.image(processed_image, caption='Processed Image')
    # 확인 버튼
    if st.button('Verify'):
        st.write("이미지가 확인되었습니다.")
