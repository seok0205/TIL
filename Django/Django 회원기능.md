# 회원기능 구현하기

## 회원 가입

- Django는 기본 auth.User를 가지고 있기에 이를 기반으로 기본적 회원가임 ModelForm을 제공하고 있음.
- `UserCreationForm`으로 `username`, `password`로 새로운 user 생성하는 모델폼
- `forms.py`에 폼 정의

```python
from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

- `views.py`에 뷰 정의. 가입 후 바로 로그인이 될 수 있게.

```python
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)
```

- `signup.html` 구성

```html
{% extends "base.html" %}

{% block content %}
    <h1>회원가입</h1>
    <form action="{% url 'accounts:signup' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">회원가입</button>
    </form>
{% endblock %}
```

## 회원 탈퇴

- `url.py`에 path 추가
- 탈퇴하면서 해당 유저의 세션도 지우기 위해 `logout()` 사용

```python
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("index")
```

- html파일에 버튼 추가

```html
<form action="{% url `accounts:delete` %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="회원탈퇴"></input>
</form>
```

## 정보 수정

- 기본 User Model에 대한 기본적인 수정 ModelForm 제공.
- UserChangeForm : 기본 User Model에 대한 Form을 제공.

### 구현

- `url.py`에 path 추가
- `views.py`에 update()정의

```python
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import (
    ...
    UserChangeForm,
)

...
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        pass
    else:
        form = UserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)
```

- `update.html` 작성

```html
{% extends "base.html" %}

{% block content %}
    <h1>회원정보수정</h1>
    
    <form action="{% url 'accounts:update' %}" method="POST">
        {{ form.as_p }}
        {% csrf_token %}
        <button type="submit">수정하기</button>
    </form>

{% endblock %}
```

- `base.html`에 버튼 추가

- `<a href="{% url "accounts:update" %}">회원정보수정</a>`

### CustomUserChangeForm 만들기

- `forms.py`에 customUserChangeForm()정의

```python
from django.contrib.auth.forms import  UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
```

- `get_user_model()` : 현재 프로젝트에서 활성화 되어있는 유저모델을 반환, 직접 User 모델 임포트도 가능하지만 이 함수 활용을 권장함. django는 다중 User모델을 지원해 확장에 용이. 프로젝트의 유연성과 확장성을 높임.

### CustomUserChangForm() 활용해 views.py 완성

```python
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)
```

## 비밀번호 변경

- PasswordChangeForm : 유저의 비밀번호를 변경할 수 있는 Form 제공

## 구현하기

- `urls.py` path 추가
- `views.py` change_password() 정의 : CustomUserUpdateForm()를 `forms.py`에서 정의. 기존 UserChangeForm을 상속.

```python
# views.py
@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)
```

```python
# forms.py
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields.get("password"):
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text
```

- `change_password.html` 작성

```html
{% extends "base.html" %}

{% block content %}
<h1>비밀번호 변경</h1>

<form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">비밀번호 변경</button>
</form>
{% endblock content %}
```
