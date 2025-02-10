import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def draw_rectangle_with_text(image, text, rect_start, rect_end):
    # 이미지에 사각형과 텍스트 추가
    draw = ImageDraw.Draw(image)
    # 사각형 그리기
    draw.rectangle([rect_start, rect_end], outline="red", width=10)
    # 텍스트 위치 및 폰트 설정
    try:
        # Try loading a TTF font if available (you might need to adjust the path to a TTF file on your machine)
        font = ImageFont.truetype("arial.ttf", 16)
    except IOError:
        # If TTF font is not available, fall back to default PIL font
        font = ImageFont.load_default()
    # 텍스트의 위치를 사각형의 상단 왼쪽에 배치
    text_position = (rect_start[0], rect_start[1] - font.getsize(text)[1])
    draw.text(text_position, text, font=font, fill="white")
    return image

st.title('다회용기 미션 프로토타입')
uploaded_file = st.file_uploader("이미지를 업로드하세요. 모델 연결 후 사진 찍어도 탐지되도록 수정 할 예정입니다.", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # 사각형 시작과 끝 좌표 설정 (실제 사용시 조정 필요)
    rect_start = (50, 100)  # 좌표 조정 예시
    rect_end = (250, 300)   # 좌표 조정 예시
    # 이미지 처리
    processed_image = draw_rectangle_with_text(image, "tumbler", rect_start, rect_end)
    # 이미지 보여주기
    st.image(processed_image, caption='Processed Image')
    # 확인 버튼
    if st.button('Verify'):
        st.write("물 지급 완료!")

