# Django_2

## Django Template

- HTML 파일을 작성하고 뷰로 사용.

```python
# my_first_pjt/articles/views.py
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
```

- templates 폴더를 만들고 그 안에 `index.html` 생성.
- `my_first_pjt/articles/templates/index.html` 경로.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My First Django PJT</title>
  </head>
  <body>
    <h1>My First Django Project</h1>
    <p>My first Django project is working!</p>
  </body>
</html>
```

- VScode 에서 !입력 후 Tab을 누르면 기본 HTML파일 구조가 자동 완성.
- 대체적 과정은 `HttpRequest → URLs → View→ Template → View → HttpResponse`.

```python
render(request, template_name, context)
```

- 주어진 템플릿을 context와 결합해서 렌더링 거친 후 완성된 html을 HttpResponse로 돌려주는 함수.

## Django Template System

- Data를 보여주는 로직을 작성하는 부분
- 템플릿의 기본 경로는 `setting.py`의 `TEMPLATES`의 `APP_DIRS`를 보고 찾을 수 있음.

### Django Template Language(DTL)

- Django Template에서 사용하는 문법. Python과 비슷하게 구성.

#### DTL 문법

1. 변수(Variable)
    - 기본형태 : `{{ variable }}`
    - view의 context로 넘긴 데이터를 접근할 수 있음.
    - `.`을 사용해 변수의 속성값에 접근 가능.
    - `render()`의 세번째 인자인 context에 `dict` 형태롤 넘겨진 데이터 중 `key` 값이 template에서 사용 가능한 변수가 됨.

2. 필터(filters)
    - 기본형태 : `{{ variable|filter }}`
    - 변수에 어떤 작업을 추가적으로 더해 수정하고 싶을 때 사용
    - 약 60개의 built-in template filter가 제공, 일부 필터는 인자를 받기도 함.
    - ex : view에서 넘겨준 데이터는 `Seok`이지만 보일 때 소문잘로 하고 싶다면 `{{ first_name|lower }}`

3. 태그(tags)
    - 기본 형태 : `{% tag %}`
    - 반복문 or 논리, 조건문을 수행해 제어 흐름을 만들거나 특수한 기능 수행
    - 일부는 시작 태그와 종료 태그가 있음
    - ex : `{% if ~ %}`, `{% endif %}`

4. 주석(comments)

```html
{# 한 줄 주석 #}

{% comment %}
 여러줄
 주석
{% endcomment %}
```

#### Tempalte Inheritance

- 중복 문제 해결 위해 템플릿 상속을 지원
- 코드의 재사용성에 초점이 맞춰져 있으며, 상위 템플릿에 공통이 될 부분을 정의하고 하위 템플릿에서 달라질 부분을 블록(Block)으로 만드는 스켈레톤 형태

1. `{% block block_name %} {% endblock block_name %}`
    - 상위 템플릿에서 하위 템플릿 마다 달라질 부분을 정의

2. `{% extends 'template_name' %}`
    - 하위 템플릿에서 상위 템플릿 상속해서 확장한다는 것
    - 템플릿의 가장 최상단에 위치해야 함
    - 다중상속을 지원하지 않음

## 데이터 주기

### HTTP Form

- `action` : 데이터를 어디로, 전송될 URL 지정. 지정 안하면 현재 페이지로.
- `method` : 어떤 방식을 이용하여 보내는지, HTTP Form은 GET or POST로만 가능.

- `label for`, `input id`는 일치해야 함. 동일 시 `label`, `input`을 묶기 가능. (label 클릭시 input 선택되도록 만들기 가능)

- button의 type을 submit로 해야 버튼이 전송 기능을 가짐.

#### input 요소

1. input
    - form에서 사용자의 입력을 받기 위해 사용.
    - `type` 속성에 따라 입력 동작 방식 달라짐. 지정 않을 시 text로 인식.
    - 데이터 전송에서 핵심은 `name`. 이를 향해 서버에 데이터 전달, 서버는 이를 보고 데이터 판단.

2. name
    - form을 submit하면 `name` 속성에 설정된 값이 서버로 전송.
    - 서버에서는 `name` 속성을 사용해 값에 접근. 없으면 서버가 데이터 못받음.
    - `name`속성의 값이 key가 되고, 사용자가 입력한 값이 value가 되어 전송.

#### HTTP methods

1. HTTP
    - 하이퍼텍스트 전송 프로토콜(Hyper Text Transfer Protocol)
    - 여러가지 리소스 보내고 받을 때 사용하는 프로토콜(통신규약)
    - 요청과 응답으로 이루어진 통신
    - 웹에서 데이터 교환의 기초

2. HTTP Methods
    - HTTP에서 수행할 작업
    - 특정 자원에 대해 수행하고자 하는 동작을 method로 정의
    - GET, POST, PUT, DELETE 등이 존재

3. GET
    - 특정 자원 조회에 사용
    - 데이터를 서버로 전송할 때 쿼리스트링을 사용해서 전송(URL에 데이터 포함되어 전송)
    - 기본적으로 method 명시하지 않으면 GET으로 처리

#### 쿼리스트링(Query String Parameter)

- 데이터를 URL 주소에 포함시켜 전송하는 방식
- `?` 뒤에 데이터가 위치
- `&`로 연결된 `key=value` 형태로 구성

#### 요청이 처리되는 과정

1. 요청이 들어오면 Django는 HttpRequest 객체 생성
2. urls에서 지정하나 view 함수의 첫번째 인자자로 전달
3. view는 처리 후, HttpResponse 전달

## 데이터 받기

- 클라에서 GET 방식으로 보낸 데이터를 서버에서 받음(쿼리스트링 방식)
- 이런 데이터를 받는 방식은 도구(프레임워크)마다 구현방식 다름

- 똑같이 템플릿(html파일)과 `urls.py`, `view.py` 수정을 통해 페이지 생성 뒤 view에서 데이터를 받아 Context를 넘김.

- `<a>`와 `href=""` 를 활용하여 하이퍼링크도 추가 가능

### request

- request는 WSGIRequest 클래스의 인스턴스로 요청에 대한 모든 메타데이터가 들어있음.
- request.GET은 QueryDict 타입
  - 타입 == 클래스
  - QueryDict는 Dict를 상속한 클래스. request.GET, POST 속성은 모두 QueryDict의 인스턴스
  - 일반적인 dict보다 HTTP특성의 필요한 기능들이 있어 추가적으로 구현한 클래스
