# URL Namespace

- articles, users 두개의 앱에서 `articles/url.py`, `users/urls.py` 에도 `hello/`가 있다면?

- Django는 서로 다른 앱에서 동일한 URL Name을 사용하는 경우, 고유하게 구분할 수 있도록 namespace를 지원함.

- url에 이름 공간을 만들어주고 나면, namespace:url_name형태로 사용

```python
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("hello/", view.hello, name="hello"),
]
```

- 아래와 같은 형식으로 사용

```python
{% url 'articles:hello' %}

redirect('articles:hello')
```

- app_name을 지정하면 url들의 name을 참조하고 있는 모든 곳들을 수정해야함.

## Templates 구조

- `views.py`에서 `index.html`만 입력해도 django가 알아서 찾아온다.

- users, articles 앱 모두 `index.html`이 있다면?

- 각 앱의 templates 폴더 안에 `users`, `articles`라는 이름의 새 폴더를 만들고 그안에 모든 html 파일들을 넣는다.

- 그 후, 정의해놨던 파일명 앞에 `users/index.html`, `articles/index.html`처럼 입력한다.
