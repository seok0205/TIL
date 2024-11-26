import streamlit as st
import pandas as pd

# ttl = time to live = 캐시 유지 시간 = 초 단위(600초)
@st.cache_data(ttl=600)

def fetch_data(): # 데이터 로딩 예시 
    return {"data": [1, 2, 3, 4]} 

st.write(fetch_data())

# 세션: 인터넷 연결이 유지되는 것(나갔다 들어와도 유지)
if "user_name" not in st.session_state:
    st.session_state.user_name = "Guest"

name = st.text_input("Your Name:", st.session_state.user_name)

if st.button("Save Name"):
    st.session_state.user_name = name
    
st.write(f"Hello, {st.session_state.user_name}!")

# 파일 불러오기
@st.cache_data
def load_file(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload a CSV File", type=["csv"])
if file:
    df = load_file(file)
    st.dataframe(df)

    # 필터링 기능 추가
    filter_value = st.text_input("Filter by column value")
    filtered_df = df[df.iloc[:, 0].astype(str).str.contains(filter_value, na=False)]
    st.write("Filtered Data:", filtered_df)

# css, html 문법으로 텍스트 색, 글씨체 변형 가능.
st.markdown(
    """
    <style>
    .custom-title {
        color: #4CAF50;
        font-size: 30px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True, # True 아닐 시, Warning이 뜸.
)

st.markdown('<p class="custom-title">Customized Title</p>', unsafe_allow_html=True)

# 버튼 클릭시 팝업창.
st.components.v1.html(
    """
    <button onclick="alert('Button clicked!')">Click Me</button>
    """,  # 삽입할 HTML 코드
)

# 탭 구현
tab1, tab2 = st.tabs(["게시판", "지도 화면"])
with tab1:
    st.write("이 화면은 게시판입니다.")
    # 게시판 화면 직접 구현
with tab2:
    st.write("이 화면은 지도입니다.")
    # 지도 화면 직접 구현

# 사이드 바(메뉴) 구현
st.sidebar.header("Sidebar")
st.sidebar.button("Sidebar Button")

# 페이지 컬럼 구현
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")

# 표 컬럼 추출.
df = pd.read_csv("file")

selected_columns = st.multiselect("Select columns to display", file.columns)
if selected_columns:
    st.write(file[selected_columns])