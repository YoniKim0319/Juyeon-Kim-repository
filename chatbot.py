import streamlit as st

def create_chat_bubble(text, is_user=True):
    """채팅 버블 스타일을 생성하는 함수입니다."""
    color = "light" if is_user else "success"
    st.markdown(
        f"<div style='background-color: {'#f0f2f6' if is_user else '#dbf0d8'}; padding: 10px; border-radius: 25px; width: fit-content; "
        f"max-width: 70%; margin: {'10px 20px 10px auto' if is_user else '10px auto 10px 20px'}; text-align: left; float: {'right' if is_user else 'left'};'>"
        f"<span style='color: black;'>{text}</span>"
        "</div>",
        unsafe_allow_html=True
    )

# 사전에 정의된 질문과 답변
recycling_faq = {
    "우유팩": "우유팩은 재활용이 가능합니다. 내용물을 깨끗이 비우고, 잘 헹군 후 말려서 재활용 쓰레기통에 버려주세요.",
    "귤 껍질": "귤 껍질은 음식물 쓰레기입니다. 음식물 쓰레기 전용 쓰레기통에 버려주세요.",
    "종이류": "신문지, 책류, 종이상자류, 봉투류, 포장지는 재활용 가능합니다. 비닐 코팅된 종이류, 테이프, 기타 이물질이 섞인 경우, 영수증, 파쇄지는 재활용할 수 없습니다.",
    "종이컵, 종이팩": "이물질이나 음식물이 묻어 있지 않은 경우에만 재활용이 가능합니다.",
    "고철류": "고철, 알루미늄, 철판은 재활용 가능합니다. 고무나 플라스틱이 합성된 제품은 재활용할 수 없습니다.",
    "유리병류": "맥주, 소주, 음료수, 드링크병류는 재활용 가능합니다. 병뚜껑을 제거하고 내용물을 헹군 후에 배출하세요. 식기류, 도자기류, 깨진 유리는 재활용할 수 없습니다.",
    "캔류": "음료수 캔, 부탄가스, 에어졸 캔은 재활용이 가능합니다. 구멍을 뚫어 내용물을 완전히 비우고 배출하세요. 페인트나 오일이 묻어있는 캔은 재활용할 수 없습니다.",
    "플라스틱류": "PET, PE, PP, PS, PSP 재질의 용기는 재활용이 가능합니다. 투명 페트병은 별도로 분리배출해야 합니다.",
    "스티로폼": "흰색 스티로폼 포장용기는 재활용 가능합니다. 음식물이나 이물질이 많이 묻어 있거나 코팅된 스티로폼은 재활용할 수 없습니다.",
    "비닐류": "위생팩, 과자 라면 봉지 등은 비닐류로 분류되어 목요일에만 배출이 가능합니다. 이물질이 묻어 있는 경우 재활용할 수 없습니다.",
    "의류": "의류는 의류수거함 또는 투명 비닐에 담아 배출합니다. 솜이불류는 재활용할 수 없습니다.",
    "재활용 안 되는": "PVC 제품, FRP, 공업용 플라스틱, 폐비닐, 석고, 어린이 장난감, 부스러기 스티로폼, 유리조각, 가방류, 도자기, 비닐장판, 신발, 가죽제품, 코팅된 물질, CD, 깨진 폐형광등, 고무호스, 카세트·비디오테이프, 옷걸이, 페인트 통, 사용한 도배지는 특수규격 마대에 담아 배출해야 합니다."
}

def get_answer(question):
    # 질문에서 키워드 추출하여 답변하는 로직
    for keyword in recycling_faq:
        if keyword.lower() in question.lower():
            return recycling_faq[keyword]
    return "해당 질문에 대한 답변을 찾을 수 없습니다. 더 구체적인 질문을 해주세요."

# 스트림릿 앱 생성 및 설정
st.title("쓰레기 분리수거 FAQ 챗봇")
st.subheader("쓰레기 분리수거에 대한 궁금증을 해결해드립니다. 질문을 입력해주세요!")

user_question = st.text_input("", placeholder="예: 귤 껍질은 어디에 버려야 하나요?", key="user_input")

if st.button("질문하기"):
    create_chat_bubble(user_question, is_user=True)
    answer = get_answer(user_question)
    create_chat_bubble(answer, is_user=False)

# 페이지 초기화용
if st.button("채팅 초기화"):
    st.experimental_rerun()

# 스크롤을 항상 아래로 유지 (JavaScript 활용)
st.markdown(
    "<script>window.scrollTo(0, document.body.scrollHeight);</script>",
    unsafe_allow_html=True
)
