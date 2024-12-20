# Django Auth

## Auth

- 인증(Authentication), 권한(Authorization)을 합쳐서 Auth. 인증시스템.
- 인증 : 내가 누구인지를 입증
- 권한 : 수행할 수 있는 자격 여부

## HTTP, 쿠키(cookie)와 세션(session)

- Django의 settings.py의 미들웨어 부분을 확인하면 세션과 Auth이 있는 걸 확인 가능.

### HTTP 특징

- 웹은 HTTP 방식을 사용해 통신을 주고받고 데이터 교환의 기초이기 때문에 중요.

1. 비연결지향(Connectionless) : 한 번 요청에 대한 응답을 하면 연결이 끊어짐.
2. 무상태(Stateless) : 연결이 끊어지면 통신이 끝나고 서로 잊어버림. 모든 메세지는 독립적.
3. 만약 쿠키와 세션이 없다면 이전 요청 기억하지 못하고, 요청 보낼 때 마다 로그인 해야함.

### 쿠키(Cookie)

- 서버 -> 웹 브라우저에 전달하는 작은 데이터 조각 : 유저가 웹을 방문 시 서버로부터 쿠키를 전달 받음

- Key-Value 형태로 데이터가 저장

- 이후 동일한 서버에 보내는 모든 요청에 쿠키가 함께 전달

- 쿠키 데이터는 유저의 로컬에 저장되는 정보

#### Cookie TMI

- 광고시장에서 중요하게 활용됨
- 검색 기록 추적으로 쉽게 유저별 맞춤형 광고를 할 수 있음
- 쿠키에 대해 개인정보이슈에 대해 논의가 이루어지는 중(구글 크롬도 쿠키 제제를 24년 발효)(광고 시장이 크게 바뀔 수 있음)

### 세션(session)

- 쿠키만 있다면 누구나 가입된 유저인 것처럼 행동할 수 있음. 유저의 로컬에 저장된 단순한 문자열 정보라서 유저가 맘대로 바꿀 수 있음.

- 세션은 서버와 클라이언트간 상태를 기억하기 위한 것

#### 세션과 쿠키가 쓰이는 방법

1. 클라이언트가 서버에 접속
2. 서버가 특정 세션 ID를 발급, 기억
3. 세션 ID 전달받아 쿠키에 저장
4. 이후 클라이언트는 해당 쿠키를 이용해 요청
5. 서버에서는 쿠키에서 세션 ID를 꺼내서 검증
6. 검증에 성공 시 알맞은 로직 처리

- 쿠키에 민감 정보 저장 X, 세션 ID만 저장하고 서버에서 검증하는 방식으로 사용(이것이 로그인 절차)

#### 쿠키의 수명

- 세션쿠키(Session Cookie) : 현재 세션이 종료되면(브라우저 닫힘) 삭제됨
- 지속쿠키(Persistent Cookie) : 디스크 저장, 브라우저 닫거나 컴퓨터 재시작해도 남아있음. Max-Age 지정해 해당 기간이 지나면 삭제 가능.

## Django의 Authentication System

### 로그인 구현하기

- Authentication Form : Django의 Built-in Form으로 로그인을 위한 기본적 form을 제공

#### login()

- login() 함수로 로그인 구현
- 사용자 로그인 처리를 해주고 내부적으로 session 사용해 user 정보 저장.

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.login, name="login"),
]
```

```python
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:index ")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


```

#### superuser

- User/ Staff/ Superuser 세 가지로 구분

- `python manage.py createsuperuser`으로 Admin 기능에 접근할 수 있는 최고 권한 유저 생성 가능

#### logout

- DB를 조작하므로 POST로 요청.

```python
# accounts/views.py
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect("index")
```

### HTTP 요청을 처리하는 다양한 방법

#### Django shortcut functions

1. `render()` : 템플릿을 렌더링해서 전달
2. `redirect()` : 특정 경로로 요청을 전달
3. `get_object_or_404()` : GET을 호출한 후 객체가 없다면 404 에러를 raise하여 404 페이지로 이동시킴
4. `get_list_or_404()` : filter를 호출한 후 빈 리스트라면 404 에러를 raise하여 404 페이지로 이동

#### View Decorators

- 여러가지 다양한 HTTP 기능 제공 위해 데코레이터 존재

1. `require_http_methods()` : view 함수 특정한 method 요청에 대해서만 허용
2. `require_POST()` : POST 요청만 허용

#### Template with Auth

- 템플릿으로는 우리가 context를 넘기지 않아도 자동으로 넘어가는 context들이 존재.

- `request.user`도 그 중의 하나. 템플릿을 랜더링할 때 현재 로그인한 사용자를 나타내는 `auth.User` 클래스의 인스턴스 또는 `AnonymousUser` 인스턴스를 `request.user로 접근 가능.`

#### 접근 제한하기

- `is_authenticated` 활용 예시.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <div class="navbar">
        {% if request.user.is_authenticated %}
            <h3>안녕하세요, {{ user }}님</h3>
            <form action="{% url 'accounts:logout' %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="로그아웃">
            </form>
        {% else %}
            <a href="{% url 'accounts:login'%}">로그인</a>
        {% endif %}
    </div>

    <div class="container">
        {% block content %}
        {% endblock content %}
    </div>

</body>
</html>
```

```python
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("index")
```

- `@login_required` 활용 예시

```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect("articles:articles")

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/update.html", context)
```
