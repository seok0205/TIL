from fastapi import FastAPI

# FastAPI 인스턴스 생성
app = FastAPI()

# 루트 경로에 GET 요청이 들어왔을 때 "Hello World!"를 반환하는 엔드포인트 정의
@app.get("/")
def read_root():
    return {"message": "Hello World!"}