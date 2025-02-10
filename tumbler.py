import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def draw_rectangle_with_text(image, text, rect_start, rect_end):
    draw = ImageDraw.Draw(image)
    draw.rectangle([rect_start, rect_end], outline="red", width=10)

    # Ensure compatibility with font size handling
    try:
        # Attempt to use a TrueType font with a specified size
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        # Fallback to a default font if TrueType fails
        font = ImageFont.load_default()
    
    # Calculate text size to adjust positioning
    text_width, text_height = draw.textsize(text, font=font)
    # Set text position at the upper left of the rectangle, above it
    text_position = (rect_start[0], rect_start[1] - text_height - 5)  # Adjusted to add a small gap above the rectangle

    draw.text(text_position, text, font=font, fill="white")
    return image

st.title('다회용기 미션 프로토타입')
uploaded_file = st.file_uploader("이미지를 업로드하세요.", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    rect_start = (50, 100)  # Coordinates may need adjustment
    rect_end = (250, 300)   # Coordinates may need adjustment
    processed_image = draw_rectangle_with_text(image, "tumbler", rect_start, rect_end)
    st.image(processed_image, caption='Processed Image')
    if st.button('Verify'):
        st.write("물 지급 완료!")

