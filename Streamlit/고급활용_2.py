# 간단한 채팅
from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right

# 반복 실행.
import time
import streamlit as st

placeholder = st.empty()
for i in range(10):
    placeholder.write(f"Iteration {i}")
    time.sleep(1)

# 선형 회귀 머신러닝 예측 기능.
from sklearn.linear_model import LinearRegression
import numpy as np

# 모델 학습
model = LinearRegression()
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model.fit(X, y)

# 사용자 입력
user_input = st.number_input("Enter a value for prediction:")
if st.button("Predict"):
    prediction = model.predict([[user_input]])
    st.write(f"Prediction: {prediction[0]:.2f}")

# api 필요.
import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=YOUR_API_KEY")
if response.status_code == 200:
    data = response.json()
    st.write(f"Temperature: {data['main']['temp']}K")