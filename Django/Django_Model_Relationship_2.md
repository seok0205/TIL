# Model Relationship(M:N)

## ManyToMany Relationship

- `좋아요` 기능 : User가 Article에 좋아요를 누르는 것. User가 어떤 Article에 좋아요를 눌렀는지 저장

### 구현

- User는 여러 Article에 좋아요를 누를 수 있음

- 좋아요 테이블을 따로 생성

```python
# article/models.py
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles"
    )
    ...

class ArticleLike(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="likes"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
    )

    '''
    # 좋아요에 정도를 표현. 단, Article()에 M2MField에 through 사용해 중계테이블 지정.
    rating = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    '''
```

### ManyToMany

- 다대다 관계 설정시 사용하는 모델 필드 (ex. 좋아요 기능)
- 중계 테이블을 이용해서 관계를 표현
- `models.ManyToManyField(<classname>)`을 이용해서 설정
- M2M 관계가 설정되면 역참조시 사용가능한 `_set`이름의 RalationManager를 생성(`related_name`으로 변경 가능)
- `add()`, `remove()`를 이용해서 관련 객체를 추가, 삭제 가능

### 좋아요 구현하기

```python
# articles/models
class Article(models.Model):
    ...
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )   # through="ArticleLike" 추가로 중계테이블 지정 가능
```

- 마이그레이션 실행

- 중계테이블 : Django는 M2M 필드 추가 시 자동으로 중계테이블을 설정

#### ORM 연습하기

- article, user 가져오기

```bash
article_3 = Article.objects.get(id=3)
article_4 = Article.objects.get(id=4)
user_1 = User.objects.get(id=1)
user_2 = User.objects.get(id=2)
```

- 좋아요 추가, 조회하기

```bash
article_3.like_users.add(user_1)    # 유저 1 -> 기사 3 좋아요
article_3.like_users.add(user_2)    # 유저 2 -> 기사 3 좋아요
article_3.like_users.all()  # 기사 3을 좋아하는 모든 user 목록

article_4.like_users.add(user_1)    # 유저 1 -> 기사 4 좋아요
user_1.like_articles.all()  # 유저 1이 좋아하는 모든 기사 목록
```

```python
# articles/urls
urlpatterns = [
    ...
    path("<int:pk>/like/", views.like, name="like"),
    ...
]
```

```python
# articles/views
@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
    else:
        return redirect("accounts:login")

    return redirect("articles:articles")
```

- html 파일 수정

```html
{% for article in articles %}

...

<form actions="{% url 'article:like' article.pk %}" method="POST">
    {% csrf_token &}
    {% if user in article.like_users.all %}
        <input type="sumit" value="좋아요 취소">
    {% else %}
        <input type="sumit" value="좋아요">
    {% endif %}
</form>

{% endfor %}
```

### 팔로우

- M:N 관계(한명의 유저는 여러명 팔로우하면서 팔로워 가질 수 있음)
- 단 m2m 관계를 자신과 맺어야함(USER-USER)

```python
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    following = models.ManyToManyField('self', related_name='followers')
```

- `symmetrical` : M2M Field가 동일한 모델(self)과 관계를 맺는 경우 사용
- True(기본값)인 경우 한 방향에서 관계를 맺으면 반대 관계도 설정(대칭)

#### 팔로우 구현

```python
# accounts/models.py
# 코드 작성 후 마이그레이션 필요, 생성된 테이블도 확인 필요
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
```

```python
# users/url.py
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    ...
    path("<int:user_id>/follow/", views.follow, name="follow"),
]
```

```python
# users/views.py
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

def users(request):
    return render(request, "users/users.html")

def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    context = {
        "member": member,
    }
    return render(request, "users/profile.html", context)

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_pk)
        if request.user != member:
            if request.user in member.followers.all():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", member.username)
    return redirect("accounts:login")
```

- profile.html 파일 작성

```html
{% extends 'base.html' %}

{% block content %}
    <h1>{{ member.username }}의 프로필 페이지</h1>

    <div>
        <h2>username : {{ member.username }}</h2>
        <p>
            팔로워 : {{ member.followers.count }}명
            팔로잉 : {{ member.following.count }}명
        </p>
    </div>

    <div>
        <form action="{% url 'users:follow' member.pk %}" method="POST">
            {% csrf_token %}
            {% if user in member.followers.all %}
                <button type="submit">언팔로우</button>
            {% else %}
                <button type="submit">팔로우</button>
            {% endif %}
        </form>
    </div>

    <a href="/index/">홈으로 돌아가기</a>

{% endblock content %}
```
