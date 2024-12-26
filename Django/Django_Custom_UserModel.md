# Custom UserModel 활용하기

## Custom User Model

### 현재 User Model

- Django의 기본 User Model을 사용
- 대부분 프로젝트에서는 User Model에 더 많은 기능이 필요
- Django는 `AUTH_USER_MODEL` setting을 변경하여 기본 User Model 대체 가능
- 만약 기본 User Model을 사용하더라도 Custom User Model을 사용하는 것이 권장

### 적용하기

#### 주의 점

- `AUTH_USER_MODEL` 설정은 반드시 프로젝트 최초 마이그레이션에서 함께 진행 권장
- User Model은 비즈니스 로직 깊숙히 관여되기에 중간에 변경하면 많은 변경사항을 야기함

#### User Model 정의

- 기본 유저를 변경하지 않더라도 확장성 위해 Custom User Model을 작성

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass
```

```python
# settings.py
...
AUTH_USER_MODEL = 'accounts.User'
...
```

```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

- migration 적용하기

- 프로젝트 중간에 진행되므로 DB를 초기화하고 진행 -> 그렇지 않을 경우, 마이그레이션이 뒤엉킴

- `db.sqlite3` 파일 삭제 및 모든 `migration` 삭제 후 다시 마이그레이션 함

### 회원가입 로직 수정

```python
def signup(request):
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

- 기존의 `UserCreationForm`은 Django의 기본 User 모델을 사용중이믈로 해당 부분 수정이 필요

- `accounts.User`를 바라보도록 상속을 통한 클래스 재정의

```python
# forms.py
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (필요시 추가필드)
```

## 1:N 관계 확장하기

### User(1) - Article(N) 확장하기

```python
# articles/models.py
...
from django.conf import settings


class Article(models.Model):
...
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
...
```

- 코드 변경 후 마이그레이션 `python manage.py makemigrations`

- 작성자를 제외해주는 것이 필요

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        exclude = ("author",)
```

```python
# articles/views.py
def create(request):
    if request.method == "POST":
        form =ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("articles:article_detail", article.pk)
        else:
            form =ArticleForm()
        
        context = {"form":form}
        return reder(request, "articles/create.html", context)
```
