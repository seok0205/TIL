'''
1. 사이드바와 컬럼 레이아웃, 확장이 가능 창 활용.
2. CSV 파일 업로드 및 데이터 확인.
3. 여러 차트로 데이터 표현.
'''

import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns

# 사이드바 구성
st.sidebar.title("옵션 선택")
page = st.sidebar.selectbox("페이지를 선택하세요", ["홈", "데이터", "시각화"])

st.write(f"현재 선택된 페이지: {page}")

# 컬럼 레이아웃
col1, col2 = st.columns(2)
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

# 확장 가능 컨텐츠
with st.expander("자세히 보기"):
    st.write("여기에 숨겨진 내용을 작성합니다.")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("데이터 미리보기:")
    st.dataframe(df)

if uploaded_file:
    st.write("컬럼별 데이터 요약:")
    st.write(df.describe())

# 데이터 필터링
if uploaded_file:
    column = st.selectbox("필터링할 컬럼 선택", df.columns)
    value = st.text_input(f"{column}의 값을 입력하세요")
    if value:
        filtered_df = df[df[column].astype(str).str.contains(value)]
        # df라는 데이터프레임 안에서
        # df[column](예를 들면, df["이름"], df["학점"], df["학과"])에서
        # df[column] 값을 문자열(str)로 변경한 다음에
        # 문자열에서 쓰이는 함수만 쓸거야.
        # contains라는 함수를 쓸게.
        # value가 포함된 값만 뽑아줘.
        st.write("필터링된 데이터:")
        st.dataframe(filtered_df)

if uploaded_file:
    fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title="Scatter Plot")
    st.plotly_chart(fig)

if uploaded_file:
    plt.figure(figsize=(10, 5))
    plt.hist(df[df.columns[0]], bins=20)    # 히스토그램
    st.pyplot(plt)

if uploaded_file:
    chart = alt.Chart(df).mark_bar().encode(    # 막대그래프, mark_line은 꺾은선.
        x=df.columns[0],
        y=df.columns[1]
    )
    st.altair_chart(chart, use_container_width=True)    # 웹사이트 가로 길이와 같음.

if uploaded_file:
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, ax=ax) # boxplot은 최대,최소값 표시된 막대그래프.
    st.pyplot(fig)