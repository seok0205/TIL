# Django MTV(CR)

## Django MTV with CR

- Django Model + Template + View 활용.

1. url.py에 path 추가.
2. views.py에 추가.
3. html 파일 templates에 추가.

### 조회

- DB에서 모든 아티클 조회해서 /articles/에서 볼 수 있도록 하는 것.

1. view에서 model에 접근해 모든 아티클 가져오기
2. view에서 가져온 아티클 template로 넘기기
3. template에서 넘어온 context 보여주고
4. veiw에서 템플릿을 렌더링해서 리턴

### 새로운 글 작성

- 클라이언트에서 서버에 데이터를 전송하여 저장. (form 이용)

1. url.py에 path 추가
2. view.py에 추가
3. html파일 templates에 추가

### 넘어온 데이터 처리하기

1. create view에서 데이터 넘겨받기
2. 넘겨받은 데이터로 새로운 데이터 생성(view.py에서)
3. create.html으로 표현

#### 최신순 보여주기

- created_at을 사용하거나 pk를 사용하여 정렬 가능
- `articles = Article.objects.all().order_by("-id")`

## HTTP Method

### GET

- 원하는 리소스를 가져오는데 사용
- 생성할 때도 가능하지만, 리소스 조회용으로 사용하자는 암묵적
- DB에 변화를 주지 않는 요청임을 의미
- Read에 해당

### POST

- 서버로 데이터 전송할 때 사용
- 특정 리소스를 생성 혹은 수정하기 위해 사용
- DB에 변화를 주는 요청임을 의미
- Create, update, Delete에 해당

### 사이트간 요청 위조 CSRF(Cross-Site-Request-Forgery)

- CSRF : 유저가 실수로 해커가 작성한 로직을 따라 특정 웹페이지에 수정/삭제등의 요청을 보내게 되는 것. 유저가 의도한 요청인지 검증이 필요하므로.

- CSRF 공격은 인증이 된 상태에서 해커의 의도대로 서버에 요청을 보내게 되는 것.

- HTTPS가 데이터를 암호화하고 중간에서의 공격을 방지하는 것과는 다른 맥락에서 발생.

- CSRF Token 활용해 막을 수 있음. 유저가 서버에 요청을 보낼 때 함께 제공되는 특별한 토큰 값. 사용자의 세션과 연결되어 있음. 요청 전송될 때, 함께 제출되며 서버는 요청을 받을 때 이 토큰을 검증하여 요청이 유효한지 확인하는 방식으로 CSRF 방지

- 쉽게 말하면 서로 알아볼 수 있는 임의의 비밀번호를 만들어서 주고 받는다는 것.

- 일반적으로 GET을 제외한 데이터를 변경하는 Method에 적용.

- Django에서는 CSRF Token 방식을 구현할 수 있게 template tag로 제공.

- 이것은 settings.py의 미들웨어를 보면 어떻게 동작하는지 파악 가능.

### POST vs GET

- HEADER : HTTP 전송에 필요한 모든 부가정보를 담은 부분(메시지 크기, 압축, 인증, 요청 클라 정보, 서버 애플리케이션 정보, 캐시 관리 정보 등)

- BODY : 실제 전송할 데이터가 담긴 부분, 데이터 없으면 비어있음.

- GET은 데이터를 URL에 담아보내고 POST는 BODY에 담아 보냄.

- GET은 데이터 전송에 한계가 있지만, POST는 그렇지 않음.

- POST방식으로 데이터를 전송 시, CSRF Token이 필요!
