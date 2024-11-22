import streamlit as st
import pandas as pd

st.title("AI 8기")
st.header("예제입니다.")
st.text("유정석")

st.markdown("안녕하세요.")
st.latex("E = mx^3")

if st.button("버튼 클릭"):
    st.write("버튼이 클릭되었습니다.")

agree_box = st.checkbox("동의하시겠습니까?")
if agree_box is True:
    st.write("동의하셨습니다!")

volume = st.slider("음악 볼륨", 0, 100, 50)
st.write("음악 볼륨은 " + str(volume) + "입니다.")

gender = st.radio("성별", ["남자", "여자", "밝힐 수 없음"])
st.write("성별은 " + gender + "입니다.")

st.container(border=False, height=20)  # 위 아래 빈 공간

movie = st.selectbox("좋아하는 영화", ["아이언맨", "헐크", "토르", "캡틴 아메리카"])

chart_data = pd.DataFrame({
    "관객": [700, 400, 500, 300],
    "예산": [1000, 300, 700, 400]
    })

st.line_chart(chart_data)