# Django Static & Media

## Static Files

- 정적 파일(멈춰있는 파일)을 의미
- 서비스 로직에서 별도의 처리 없이 보여주기만 하면 되는 파일
- ex. 서비스 이미지 파일(로고, 광고 이미지), 자바스크립트 파일, CSS 파일 등
- 이런 서비스 로직과 다르게 그냥 무조건 주기만 하면 되는 파일들이라 모아서 따로 제공할 수 있음.

### 사용_static

1. `STATIC_URL` : static 파일 참조 시 사용 url
    - 개발 단계에서는 `app/static` 경로 및 settings의 `STATICFILES_DIRS`에 정의된 경로 참조
    - 실제 디렉토리 경로가 아님에 주의. URL로만 존재하는 경로임.

2. `STATIC_ROOT`
    - 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
    - django 프로젝트에서 사용하는 모든 정적 파일을 이곳으로 모아서 적용(단, `DEBUG=True`인 경우 동작 X(개발 단계))
    - 추후 배포 시 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함

    - collectstatic
        - `python manage.py collectstatic`
        - STATIC_ROOT에 모든 정적 파일을 수집하는 명령어
        - 배포 과정에서 사용

- 각 앱의 `static` 디렉토리 : `<app_name>/static/<app_name>`

- 각 템플릿에서 정적파일 사용 : `{% load static %}`, `{% static ‘file_path’ %}`

#### 순서_Static

1. settings.py 설정 및 static 디렉토리 생성
2. `articles/static/articles` 생성하고 파일 넣기
3. 로드하고 싶은 html 파일에 사용

## Media Files

- 유저가 웹에서 업로드한 모든 파일(static file을 제외한 모든 파일)

### 사용_Media

1. `MEDIA_ROOT`
    - 업로드한 파일이 저장되는 디렉토리 경로를 지정
    - 업로드 파일은 DB에 저장되지 않으며 실제 저장되는 것을 파일의 경로

2. `MEDIA_URL` : 미디어 처리를 위한 URL

#### 순서_Media

1. settings.py 설정 및 media 디렉토리 생성

### Artiles에 사진 필드 넣기

#### Image Field

- 이미지 업로드에 사용되는 모델 필드
- 기본적으로 FileField지만 이미지인지 검사
- `upload_to` : 이미지가 업로드 되는 경로를 지정, `MEDIA_ROOT`의 하위 경로 지정

#### pillow 설치

- `ImageField`를 사용하기 위해선 `pillow` 라이브러리 설치가 필요.

- `null`, `blank` 차이 : blank는 form에서 해당 값을 입력하지 않아도 괜찮다. null은 DB에 null을 저장해도 된다.

- migration 진행

#### 수정하기

- 사진이 잘 전송되지 않음. create.html의 변형

```html
{% extends "base.html" %}


{% block content %}
<h1>New Article</h1>

<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">저장</button>
</form>
{% endblock content %}
```

- form의 enctype 속성 : form의 데이터 전송 형식을 지정하는 것으로 기본적으로는 텍스트 형식의 데이터 교환이 이루어짐.

- `mutipart/form-data` : 전송 형식을 지정하는 것으로 file, image 전송 시 사용. `<input>`의 `type=file` 사용 시 `application/x-www-form-urlencoded`가 기본값

- article/view.py 변경

```python
@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES) # request.FILES 인자 설정 이유는 BaseModelForm()의 기본 인자(data, files)가 None이라서.
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.id)
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "articles/create.html", context)
```

- Article에 사진 넣기(image가 있는 article인 경우에 이미지 출력)

```html
{% if article.image %}
<img src="{{ article.image.url }}">
{% endif %}
```

## runserver의 비밀

- `runserver`는 개발용 서버를 실행하는 것
- 순수 python으로 작성, django에 포함되어 있어 개발을 편히 도와줌
- 개발 서버를 운영 환경에서 사용해선 안됨.
- 만약 배포를 `python manage.py runserver`를 통해 하면 문제 발생. 동시 접속이 늘면 서버가 터질 수 있음.
- Django는 Web Framework이며 실제 운영시 웹 서버를 앞쪽에 달아야 함.
