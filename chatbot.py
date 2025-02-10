import streamlit as st
import os
import subprocess

# transformers 라이브러리가 설치되어 있는지 확인하고, 없다면 설치
try:
    from transformers import pipeline
except ImportError:
    # GitHub에서 transformers 라이브러리 클론
    subprocess.run(["git", "clone", "https://github.com/huggingface/transformers.git"])
    # 디렉토리 변경
    os.chdir('transformers')
    # transformers 라이브러리 설치
    subprocess.run(["pip", "install", "."])
    # 설치 후 import
    from transformers import pipeline

# 질문-답변 파이프라인 한 번만 초기화
qa_pipeline = pipeline("question-answering")

def get_answer(question):
    if "귤 껍데기" in question:
        context = "귤 껍데기는 음식물 쓰레기에 버려야 합니다."
    elif "오존층" in question:
        context = "오존층이 아예 없어지면 지구에 도달하는 자외선의 양이 증가하여 피부암, 백내장 등 건강 문제와 생태계에 심각한 영향을 미칠 수 있습니다."
    else:
        context = "자세한 정보를 제공해주세요."
    
    try:
        answer = qa_pipeline(question=question, context=context)
        return answer['answer']
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

# 스트림릿 앱 생성
st.title("환경 관련 챗봇")
user_question = st.text_input("질문을 입력해 주세요:")

if user_question:
    answer = get_answer(user_question)
    st.write("답변:", answer)
