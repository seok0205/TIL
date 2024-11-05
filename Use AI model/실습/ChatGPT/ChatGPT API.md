# ChatGPT API 호출

- API 인증, API 키 발급이 필수.(OpenAI 플랫폼)  

## OpenAI API

- OpenAI에서 제공하는 다양한 인공지능 모델을 쉽게 사용할 수 있도록 해주는 API.
- 텍스트 생성, 대화형 AI, 텍스트 요약, 번역 등 작업 수행 가능.
- ChatGPT는 자연스러운 대화 생성에 사용, 챗봇 or 고객 지원 시스템 구축 가능.

### 호출 기본 단계

1. OpenAI 계정 생성 및 로그인

    - [OpenAI login](https://platform.openai.com/signup)

2. API 키 발급

    - 로그인 후, 대시보드 메뉴에서 API Keys 찾기.
    - 'Create new secret key' 클릭, API 키 생성.(안전한 곳에 복사.)

3. API 호출 환경 설정

    - 호출할 프로그래밍 언어 선택 후, 라이브러리 설치.

        ```shell
        pip install openai
        ```

4. ChatGPT API 키 등록

    - 환경 변수로 등록 후 아래 형태로 코드 작성.

        ```python
        from openai import OpenAI
        import os

        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )
        ```

5. API 호출 결과 처리.

### API 사용 시 주의 사항

1. API 키 보안 유지 : 공개적 공유나 코드 노출 X. 환경 변수로 관리 권장.

2. API 호출 제한 : OpenAI API에는 사용량 제한이 있음. 사용량 따라 요금 부과. 호출 빈도와 사용량 모니터링이 중요.

3. 적절한 에러 처리 : 다양한 에러에 대비해 적절한 예외 처리의 구현이 중요. 네트워크 오류, 인증 실패, 사용량 초과 등의 상황에 대한 대처가 필요.

    ```python
    try:
        completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "너는 환영 인사를 하는 인공지능이야, 농담을 넣어 재미있게해줘"},
        {"role": "user", "content": "안녕?"}  
        ]
    )
            print("Assistant: " + completion.choices[0].message.content)
    except openai.error.OpenAIError as e: # 오류 발생 시
        print(f"An error occurred: {e}")
    ```
