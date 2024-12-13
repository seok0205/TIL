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
