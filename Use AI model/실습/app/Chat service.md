# ChatGPT 웹 챗봇 서비스 구축

- ChatGPT, FastAPI 활용.
- 사용자가 웹 페이지에서 대화할 수 있는 챗봇 서비스.

## 웹 인터페이스 구성

- HTML, CSS 활용해 사용자 메시지 입력창과 대화 내역 표시 페이지 구축.

## 대화 흐름 관리

- 사용자 입력 받아 ChatGPT API로 대화 요청을 보내고, 응답을 저장해 대화 내역 유지.

## API 통신 및 응답 처리

- 사용자가 입력한 텍스트를 ChatGPT API에 전달, AI의 응답을 받아 UI에 반영.

## 정적 파일 처리 및 스타일링

- 템플릿과 정적 CSS 파일을 통해 챗봇의 외형을 구성.

## 실행

- main 파일 실행 후 터미널에 아래 문장 입력.

```bash
uvicorn "Use AI model.실습.app.main:app" --reload
```

- "INFO: Uvicorn running on" 옆에 뜨는 링크 접속.
- 모두 사용하면 링크 닫고 터미널에서 컨트롤 + C 입력.(종료)

![실행 예시](./chat%20service.png)
