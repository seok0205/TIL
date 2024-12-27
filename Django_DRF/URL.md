# URL

## URI (Uniform Resource Identifier)

- 통합 자원 식별자
- 인터넷의 자원을 식별할 수 있는 유일한 문자열ㄹ
- 하위 개념 : URN, URL
- 일반적으로 URN을 사용하는 비중이 낮기 때문에 URI, URL을 같은 의미로 사용하기도 함

### URL (Uniform Resource Locator)

- 통합 자원 위치를 의미
- 웹상에 자원이 어디 있는지 나타내기 위한 문자열 -> 어디에서 어떻게 리소스를 가져와야 하는지 나타낸 문자열
- 흔히 말하는 웹 주소, 링크.

### URN (Uniform Resource Name)

- 통합 자원 이름을 의미
- 위치에 독립적인 자원을 위한 유일한 이름 역할을 함
- 리소스를 특정하는 이름(ISBN(국제표준도서번호))

## URI의 구조

- `https://www.aidenlim.dev:80/path/to/resource/?key=value#docs`

1. `http:/` : Scheme(Protocol)
    - 브라우저가 사용하는 프로토콜
    - http, https, ftp, file

2. `www.aidenlime.dev` : Host(Domain name)
    - 요청을 처리하는 웹 서버
    - IP 주소르 바로 사용할 수 있지만 도메인 이름을 받아서 사용하는 것이 일반적

3. `:80` : Port
    - 리소스 접근할 때 사용되는 일종의 게이트
    - HTTP:80/HTTPS:443이 표준 포트

4. `/path/to/resource/` : Path
    - 웹 서버에서의 리소스 경로
    - 웹 초기에는 실제 물리적인 위치를 나타냈으나 현재는 추상화된 형태 표현

5. `?key=value` : Query(Identifier)
    - 웹 서버에 제공하는 추가적인 변수
    - `&`로 구분되는 Key=Value 형태의 데이터

6. `#docs` : Fragment(Anchor)
    - 해당 자원 안에서의 특정 위치(북마크)를 나타냄
    - HTML 문서의 특정 부분을 보여주기 위한 방법
