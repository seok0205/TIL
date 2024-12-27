# RESTful API, JSON

## RESTful API

- REST(Representational State Transfer) : 웹에 대한 소프트웨어 설계 방법론
- 하나의 웹페이지를 하나의 상태로 본다면 유저가 링크를 입력하는 것은 상태 전이가 일어나는 것. 이때 유저가 받는 하나의 상태는 특정한 표현에 의해 조작된다는 개념

### 핵심

- 애플리케이션간 소통하는 방법에 REST적인 표현을 더한 것 : REST 원리 따라 설계한 API

- 결과를 보지 않고 요청 형식만 봐도 추론 가능.

- 자원은 URI로 표현, 행위는 HTTP Method로 표현. 자원과 행위를 통해 표현되는 결과물로 일반적으로 JSON 형식 사용. URI는 동사가 아닌 명사의 나열로 사용

- 따르지 않더라도 동작은 하지만 이득이 큼.

## JSON

- JS 표기법을 따른 일종의 데이터를 담는 형식
- 사람이 읽기 쉽고 프로그래밍으로 파싱하기 쉬움
- 파이썬의 dict처럼 key-value 형식의 구조

### 사용해보기

- `.json` 형식으로 사용
- 문자는 `"`으로 묶어야하고 `true`, `false`, 숫자 등을 사용 가능

```json
["리스트", 1, true, "다양한 자료를 담을 수 있어요"] // list
{ key: value } // object
```

```json
{
    "user1": {
        "name": "aiden",
        "age": 22,
        "tags": ["python", "javascript", "django"]
    },
    "user2": {
        ...
    },
    ...
}
```

- object 안에 또 object 등이 담길 수 있음
