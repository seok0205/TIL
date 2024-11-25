'''
1. 웹 상에 표현되는 여러 텍스트 표현 방법.
2. 버튼 및 체크박스 활용.
3. 게이지 조절(볼륨) 및 항목 체크, 공간 띄우기, 선택박스 활용법.
4. 데이터프레임 생성 및 간단한 차트를 통한 표현법.
'''

import streamlit as st
import pandas as pd

st.title("자기소개")
st.header("유정석")
st.text("그는 유능한 개발자가 될 사람입니다")

st.markdown("Python을 능숙히 활용할 수 있습니다.")
st.latex("livin da vida loca")

if st.button("버튼을 눌러 주세요."):
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