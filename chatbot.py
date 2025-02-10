!pip install streamlit transformers

import streamlit as st
from transformers import pipeline

# 질문-답변 파이프라인 초기화
qa_pipeline = pipeline("question-answering")

def get_answer(question):
    # 질문에 따라 다른 컨텍스트를 제공
    if "귤 껍데기" in question:
        context = "귤 껍데기는 음식물 쓰레기에 버려야 합니다."
    elif "오존층" in question:
        context = "오존층이 아예 없어지면 지구에 도달하는 자외선의 양이 증가하여 피부암, 백내장 등 건강 문제와 생태계에 심각한 영향을 미칠 수 있습니다."
    else:
        context = "자세한 정보를 제공해주세요."
    return qa_pipeline(question=question, context=context)

# 스트림릿 앱 생성
st.title("환경 관련 챗봇")
user_question = st.text_input("질문을 입력해 주세요:")

if user_question:
    answer = get_answer(user_question)
    st.write("답변:", answer['answer'])

# 스트림릿 앱 실행
if __name__ == '__main__':
    st.run()
