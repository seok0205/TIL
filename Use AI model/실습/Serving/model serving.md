# 모델 서빙

- 학습된 머신러닝 모델을 실제 애플리케이션에서 사용할 수 있도록 제공하는 과정.  
- 서빙된 모델은 외부에서 입력 데이터를 받아ㅏ 예측을 수행하고, 그 결과를 응답으로 반환한다. 이를 위해 API(Application Programming Interface)를 활용해 모델에 접근할 수 있도록 한다.  

## 주요 개념

1. __RESTful API__ :  
    REST(Representational State Transfer) 아키텍처 스타일을 따르는 API로, HTTP를 통해 클라이언트와 서버 간에 데이터를 주고받는 방식이다.

2. __FastAPI__ :  
    Python으로 작성된 빠르고 간단한 웹 프레임워크, RESTful API를 구축하는 데 매우 적합함.

### RESTful API 개요

- HTTP 프로토콜을 사용하여 클라이언트와 서버 간에 데이터를 주고받는 방식.

- GET : 서버에서 데이터를 가져올 때 사용.
- POST : 서버에 데이터를 보낼 때 사용.
- PUT : 서버의 데이터를 업데이트할 때 사용.
- DELETE : 서버의 데이터를 삭제할 때 사용.

RESTful API는 경로(Path)를 통해 리소스(Resource)에 접근하며, 경로에 포함된 매개변수를 통해 다양한 작업 수행 가능.  

### FastAPI를 활용한 API 구축

FastAPI 활용해 "Hello World" API 구축.

1. Fast API 설치 및 기본 설정

    - FastAPI, Uvicorn(ASGI server)를 설치.

    ```shell
    pip install fastapi uvicorn
    ```

2. "Hello World" API 작성

    ```python
    from fastapi import FastAPI

    # FastAPI 인스턴스 생성
    app = FastAPI()

    # 루트 경로에 GET 요청이 들어왔을 때 "Hello World!"를 반환하는 엔드포인트 정의
    @app.get("/")
    def read_root():
        return {"message": "Hello World!"}
    ```

3. FastAPI 서버 실행

    ```shell
    uvicorn your_script_name:app --reload
    ```

    - your_script_name : 위 작성한 파이썬 파일의 이름.
    - --reload : 코드가 변경될 때 서버를 자동으로 다시 로드.

    서버 정상 시작 시, 터미널은 아래 메시지가 표시됨.

    ```shell
    INFO:     Uvicorn running on <http://127.0.0.1:8000> (Press CTRL+C to quit)
    ```

4. API 호출 및 테스트

    - 브라우저 or Postman 같은 API 테스트 도구에서 다음 URL을 입력해 API 호출이 가능하다.  

    ```shell
    <http://127.0.0.1:8000/>
    ```

    이 요청을 보내면 아래의 JSON 응답이 반환.  

    ```shell
    {
        "message": "Hello World!"
    }
    ```

    FastAPI 사용한 API 구축 완료.

5. FastAPI 문서화 기능 활용

    - FastAPI는 자동으로 API 문서를 생성해주는 기능 제공. 서버가 실행된 상태에서 아래 URL로 접속.  

    ```url
    <http://127.0.0.1:8000/docs>
    ```

    이 페이지에서는 API의 엔드포인트와 요청/응답 스키마를 Swagger UI 형태로 확인 가능. 또한, 아래 URL에서는 ReDoc으로 문서화된 API를 확인 가능.  

    ```url
    <http://127.0.0.1:8000/redoc>
    ```  
